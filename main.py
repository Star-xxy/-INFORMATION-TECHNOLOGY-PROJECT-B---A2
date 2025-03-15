from pathlib import Path

from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QApplication, QFileDialog, QTableWidgetItem, QHeaderView
from PySide6.QtGui import QImage, QPixmap, Qt
from PySide6.QtCore import QTimer, QThread, Signal, QDateTime
from qfluentwidgets import Dialog, InfoBarPosition, InfoBar

from core import YoloPredictor
import numpy as np
import traceback
import sys
import cv2
import os

from tasks import TASK, INPUT_SOURCE
from config.config import cfg
from main_window import Window
from utils.signal_bus import signalBus
from collections import defaultdict

class MainWindow(Window):
    main2yolo_begin_sgl = Signal()  # 主视窗向 YOLO 实例发送执行信号
    input_source = None  # img video webcam

    def __init__(self):
        super().__init__()

        self.init_ui()
        self.init_yolo()
        self.init_signal()
        self.init_config()

    def init_config(self):
        self.detectInterface.iou_spinbox.setValue(cfg.get(cfg.iou))
        self.detectInterface.conf_spinbox.setValue(cfg.get(cfg.conf))
        self.detectInterface.speed_spinbox.setValue(cfg.get(cfg.delay))
        self.detectInterface.save_button.setChecked(cfg.get(cfg.is_save_results))
        self.detectInterface.LineEdit.setText(cfg.get(cfg.save_path))
        self.change_model()
        self.yolo_predict.task = TASK.detect

    def init_ui(self):
        self.show()
        QApplication.processEvents()

        self.select_model = self.detectInterface.model_box.currentText()  # 默认模型

        self.detectInterface.progress_bar.setValue(0)
        self.detectInterface.right_param_frame.setMinimumWidth(0)
        self.detectInterface.run_button.setChecked(False)

        self.pt_list = os.listdir('./models/detect/')
        self.pt_list = [file for file in self.pt_list if file.endswith(('.pt', 'onnx', 'engine'))]
        self.pt_list.sort(key=lambda x: os.path.getsize('./models/detect/' + x))  # 按文件大小排序
        self.detectInterface.model_box.clear()
        self.detectInterface.model_box.addItems(self.pt_list)
        self.detectInterface.TableWidget.setColumnWidth(0, 150)
        self.detectInterface.TableWidget.setColumnWidth(1, 150)
        self.detectInterface.TableWidget.setColumnWidth(2, 100)
        self.detectInterface.TableWidget.setColumnWidth(3, 100)
        self.detectInterface.TableWidget.setColumnWidth(4, 200)
        header = self.detectInterface.TableWidget.horizontalHeader()
        header.setStretchLastSection(True)  # 使最后一列填充剩余空间
        header.setStyleSheet("QHeaderView::section { font-weight: bold; }")

    def init_signal(self):
        # 卡片信号
        # self.homeInterface.det_card.clicked.connect(lambda: self.detect_page(TASK.detect))
        # self.homeInterface.cls_card.clicked.connect(lambda: self.detect_page(TASK.classify))
        # self.homeInterface.seg_card.clicked.connect(lambda: self.detect_page(TASK.segment))
        # self.homeInterface.track_card.clicked.connect(lambda: self.detect_page(TASK.track))
        # self.homeInterface.pose_card.clicked.connect(lambda: self.detect_page(TASK.pose))

        # 检测设置信号
        self.detectInterface.model_box.currentTextChanged.connect(self.change_model)
        self.detectInterface.iou_spinbox.valueChanged.connect(lambda x: self.change_val(x, 'iou_spinbox'))  # iou 文本框
        self.detectInterface.iou_slider.valueChanged.connect(lambda x: self.change_val(x, 'iou_slider'))  # iou 滚动条
        self.detectInterface.conf_spinbox.valueChanged.connect(
            lambda x: self.change_val(x, 'conf_spinbox'))  # conf 文本框
        self.detectInterface.conf_slider.valueChanged.connect(
            lambda x: self.change_val(x, 'conf_slider'))  # conf 滚动条
        self.detectInterface.speed_spinbox.valueChanged.connect(
            lambda x: self.change_val(x, 'speed_spinbox'))  # speed 文本框
        self.detectInterface.speed_slider.valueChanged.connect(
            lambda x: self.change_val(x, 'speed_slider'))  # speed 滚动条

        self.detectInterface.LineEdit.textChanged.connect(self.change_save_folder)
        self.detectInterface.choose_folder_button.clicked.connect(self.open_save_folder)
        self.detectInterface.save_button.checkedChanged.connect(self.is_save_results)  # 保存图片选项

        self.detectInterface.run_button.clicked.connect(self.run_or_continue)  # 暂停/开始
        self.detectInterface.stop_button.clicked.connect(self.stop)  # 终止

        self.chartInterface.refresh_button.clicked.connect(self.update_chart)
        self.chartInterface.ComboBox.currentTextChanged.connect(self.update_chart)
        self.chartInterface.ComboBox_2.currentTextChanged.connect(self.update_chart)
        self.chartInterface.ComboBox_3.currentTextChanged.connect(self.update_chart)
        self.chartInterface.start_date.dateChanged.connect(self.update_chart)
        self.chartInterface.end_date.dateChanged.connect(self.update_chart)
        self.update_chart()

        signalBus.switchToSampleCard.connect(self.switchToSample) # 卡片跳转界面
    def init_yolo(self):
        self.task = TASK.detect
        # YOLO-v8 线程
        self.yolo_predict = YoloPredictor()  # 创建 YOLO 实例
        self.yolo_predict.save_res = cfg.get(cfg.is_save_results)
        self.yolo_predict.save_dir = Path(cfg.get(cfg.save_path))
        self.yolo_thread = QThread()  # 创建 YOLO 线程
        self.yolo_predict.yolo2main_pre_img.connect(
            lambda x: self.show_image(x, self.detectInterface.pre_video, 'img'))
        self.yolo_predict.yolo2main_res_img.connect(
            lambda x: self.show_image(x, self.detectInterface.res_video, 'img'))
        self.yolo_predict.yolo2main_status_msg.connect(lambda x: self.show_status(x))

        self.yolo_predict.yolo2main_result.connect(lambda x: self.save_result(x))

        self.yolo_predict.yolo2main_progress.connect(lambda x: self.detectInterface.progress_bar.setValue(x))
        self.yolo_predict.yolo2main_stop.connect(self.stop)
        self.main2yolo_begin_sgl.connect(self.yolo_predict.run)
        self.yolo_predict.moveToThread(self.yolo_thread)
        self.Qtimer_ModelBox = QTimer(self)  # 定时器: 每 2 秒监控模型文件的变化
        self.Qtimer_ModelBox.timeout.connect(self.ModelBoxRefre)
        self.Qtimer_ModelBox.start(2000)



    def switchToSample(self, task):
        self.detect_page(task)

    def change_model(self):
        # 获取当前选择的模型名称
        self.select_model = self.detectInterface.model_box.currentText()

        # 设置 YOLO 实例的新模型名称
        if self.task == TASK.detect:
            self.yolo_predict.new_model_name = "./models/detect/%s" % self.select_model
        elif self.task == TASK.classify:
            self.yolo_predict.new_model_name = "./models/classify/%s" % self.select_model
        elif self.task == TASK.segment:
            self.yolo_predict.new_model_name = "./models/segment/%s" % self.select_model
        elif self.task == TASK.track:
            self.yolo_predict.new_model_name = "./models/track/%s" % self.select_model
        elif self.task == TASK.pose:
            self.yolo_predict.new_model_name = "./models/pose/%s" % self.select_model
        # 显示消息，提示模型已更改
        self.show_status('Change Model：%s' % self.select_model)

        # 在界面上显示新的模型名称
        # self.detectInterface.model_label.setText(f"模型：{self.select_model}")

    def change_val(self, x, flag):
        if flag == 'iou_spinbox':
            # 如果是 iou_spinbox 的值发生变化，则改变 iou_slider 的值
            self.detectInterface.iou_slider.setValue(int(x * 100))

        elif flag == 'iou_slider':
            # 如果是 iou_slider 的值发生变化，则改变 iou_spinbox 的值
            self.detectInterface.iou_spinbox.setValue(x / 100)
            # 显示消息，提示 IOU 阈值变化
            self.show_status('IOU Threshold: %s' % str(x / 100))
            # 设置 YOLO 实例的 IOU 阈值
            self.yolo_predict.iou_thres = x / 100

        elif flag == 'conf_spinbox':
            # 如果是 conf_spinbox 的值发生变化，则改变 conf_slider 的值
            self.detectInterface.conf_slider.setValue(int(x * 100))

        elif flag == 'conf_slider':
            # 如果是 conf_slider 的值发生变化，则改变 conf_spinbox 的值
            self.detectInterface.conf_spinbox.setValue(x / 100)
            # 显示消息，提示 Confidence 阈值变化
            self.show_status('Conf Threshold: %s' % str(x / 100))
            # 设置 YOLO 实例的 Confidence 阈值
            self.yolo_predict.conf_thres = x / 100

        elif flag == 'speed_spinbox':
            # 如果是 speed_spinbox 的值发生变化，则改变 speed_slider 的值
            self.detectInterface.speed_slider.setValue(x)

        elif flag == 'speed_slider':
            # 如果是 speed_slider 的值发生变化，则改变 speed_spinbox 的值
            self.detectInterface.speed_spinbox.setValue(x)
            # 显示消息，提示延迟时间变化
            self.show_status('Delay: %s ms' % str(x))
            # 设置 YOLO 实例的延迟时间阈值
            self.yolo_predict.speed_thres = x  # 毫秒

    def detect_page(self, task):
        self.task = task
        self.stackedWidget.setCurrentWidget(self.detectInterface)
        self.navigationInterface.setCurrentItem(self.detectInterface.objectName())
        self.detectInterface.TitleLabel.setText(str(task))

        self.yolo_predict.task = self.task
        self.yolo_predict.new_model_name = f"./models/{self.task.folder}/%s" % self.select_model

        self.pt_list = os.listdir(f'./models/{self.task.folder}/')
        self.pt_list = [file for file in self.pt_list if file.endswith(('.pt', 'onnx', 'engine'))]
        self.pt_list.sort(key=lambda x: os.path.getsize(f'./models/{self.task.folder}/' + x))  # 按文件大小排序
        self.detectInterface.model_box.clear()
        self.detectInterface.model_box.addItems(self.pt_list)

        self.show_status(f'当前检测模式：{self.task.title}')

    def ModelBoxRefre(self):
        # 获取模型文件夹下的所有模型文件
        for task in TASK:
            if self.task == task:
                pt_list = os.listdir(f'./models/{task.folder}')
                pt_list = [file for file in pt_list if file.endswith(('.pt', 'onnx', 'engine'))]
                pt_list.sort(key=lambda x: os.path.getsize(f'./models/{task.folder}/' + x))
                # 如果模型文件列表发生变化，则更新模型下拉框的内容
                if pt_list != self.pt_list:
                    self.pt_list = pt_list
                    self.detectInterface.model_box.clear()
                    self.detectInterface.model_box.addItems(self.pt_list)
                return

    def get_image(self):
        name, _ = QFileDialog.getOpenFileName(self, '图片', cfg.get(cfg.open_fold), "Picture File(*.jpg *.png)")
        if name:
            cfg.set(cfg.open_fold, os.path.dirname(name))
            self.input_source = INPUT_SOURCE.IMG
            # 将所选档案的路径设置为 yolo_predict 的 source
            self.yolo_predict.source = name

            # 显示档案载入状态
            self.show_status('载入图片：{}'.format(os.path.basename(name)))

            self.clear_canvas()

            # 停止检测
            self.stop()

            self.stackedWidget.setCurrentWidget(self.detectInterface)

    def get_video(self):
        name, _ = QFileDialog.getOpenFileName(self, '视频', cfg.get(cfg.open_fold),
                                              "Video File(*.gif *.mp4 *.mkv *.avi *.flv)")
        if name:
            cfg.set(cfg.open_fold, os.path.dirname(name))
            self.input_source = INPUT_SOURCE.VIDEO
            # 将所选档案的路径设置为 yolo_predict 的 source
            self.yolo_predict.source = name

            self.show_status('载入视频：{}'.format(os.path.basename(name)))

            # 停止检测
            self.stop()

            self.stackedWidget.setCurrentWidget(self.detectInterface)

    def get_webcam(self):
        self.input_source = INPUT_SOURCE.WEBCAM
        # 将所选档案的路径设置为 yolo_predict 的 source
        self.yolo_predict.source = 0

        self.show_status('目前页面：Webcam检测页面')

        if self.yolo_thread.isRunning():
            self.yolo_thread.quit()  # 结束线程
            self.stop()

        self.stackedWidget.setCurrentWidget(self.detectInterface)

    def run_or_continue(self):
        # 有输入
        if self.input_source:
            # 检查 YOLO 预测的来源是否为空
            if self.yolo_predict.source == '':
                self.show_status('开始侦测前请选择图片或影片来源...')
                self.detectInterface.run_button.setChecked(False)
            else:
                # 设置 YOLO 预测的停止标志为 False
                self.yolo_predict.stop_dtc = False

                # 如果开始按钮被勾选
                if self.detectInterface.run_button.isChecked():
                    self.detectInterface.run_button.setChecked(True)  # 启动按钮
                    self.show_status('检测中...')
                    self.yolo_predict.continue_dtc = True  # 控制 YOLO 是否暂停

                    if self.input_source != INPUT_SOURCE.IMG:
                        self.detectInterface.save_button.setEnabled(False)

                    if not self.yolo_thread.isRunning():
                        self.yolo_thread.start()
                        self.main2yolo_begin_sgl.emit()
                # 如果开始按钮未被勾选，表示暂停检测
                else:
                    self.yolo_predict.continue_dtc = False
                    self.show_status("检测暂停...")
                    self.detectInterface.run_button.setChecked(False)  # 停止按钮
        else:
            self.show_status("请在左侧选择输入（图片、视频、摄像头和流媒体）")

    def clear_canvas(self):
        # 清空预测结果显示区域的影象
        self.detectInterface.pre_video.clear()

        # 清空检测结果显示区域的影象
        self.detectInterface.res_video.clear()

        # 将进度条的值设置为0
        self.detectInterface.progress_bar.setValue(0)

    def stop(self):
        # 如果 YOLO 线程正在运行，则终止线程
        if self.yolo_thread.isRunning():
            self.yolo_thread.quit()  # 结束线程

        # 设置 YOLO 实例的终止标志为 True
        self.yolo_predict.stop_dtc = True

        # 恢复开始按钮的状态
        self.detectInterface.run_button.setChecked(False)

        if self.input_source != INPUT_SOURCE.IMG:
            self.clear_canvas()
            self.detectInterface.save_button.setEnabled(True)


    @staticmethod
    def show_image(img_src, label, flag):
        try:
            if flag == "path":
                img_src = cv2.imdecode(np.fromfile(img_src, dtype=np.uint8), -1)

            ih, iw, _ = img_src.shape
            w = label.geometry().width()
            h = label.geometry().height()
            # 保持纵横比
            # 找出长边
            img_src_ = None
            if iw / ih > w / h:
                scal = w / iw
                nw = w
                nh = int(scal * ih)
                if nw != 0 and nh != 0:
                    img_src_ = cv2.resize(img_src, (nw, nh))

            else:
                scal = h / ih
                nw = int(scal * iw)
                nh = h
                if nw != 0 and nh != 0:
                    img_src_ = cv2.resize(img_src, (nw, nh))

            if nw != 0 and nh != 0:
                frame = cv2.cvtColor(img_src_, cv2.COLOR_BGR2RGB)
                img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                             QImage.Format.Format_RGB888)
                label.setPixmap(QPixmap.fromImage(img))

        except Exception as e:
            print(e)

    def open_save_folder(self):
        save_folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹", self.detectInterface.LineEdit.text())
        if save_folder_path:
            self.detectInterface.LineEdit.setText(save_folder_path)
            self.show_status(f"选择保存文件夹： ｛save_folder_path｝")

    def change_save_folder(self):
        self.yolo_predict.save_dir = Path(self.detectInterface.LineEdit.text())

    def is_save_results(self):
        if self.detectInterface.save_button.isChecked() == Qt.CheckState.Unchecked:
            # 显示消息，提示运行图片结果不会保存
            self.show_status('NOTE：运行图片结果不会保存')

            # 将 YOLO 实例的保存结果的标志设置为 False
            self.yolo_predict.save_res = False
        elif self.detectInterface.save_button.isChecked() == Qt.CheckState.Checked:
            # 显示消息，提示运行图片结果将会保存
            self.show_status('NOTE：运行图片结果将会保存')
            # 将 YOLO 实例的保存结果的标志设置为 True
            self.yolo_predict.save_res = True

    def show_status(self, msg):
        # 设置状态栏文字
        self.detectInterface.status_bar.setText(msg)

    def save_config(self):
        cfg.set(cfg.iou, self.detectInterface.iou_spinbox.value())
        cfg.set(cfg.conf, self.detectInterface.conf_spinbox.value())
        cfg.set(cfg.delay, self.detectInterface.speed_spinbox.value())
        cfg.set(cfg.is_save_results, self.detectInterface.save_button.isChecked())
        cfg.set(cfg.save_path, self.detectInterface.LineEdit.text())

    def save_result(self, result):
        datetime_now = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')
        result_info = result.get('检测结果', None)
        result_df = result.get('结果表格', None)

        # print(result_info)
        # items = result_info.replace(',', '').split()
        # result_dict = {items[i + 1]: int(items[i]) for i in range(0, len(items), 2)}
        # print(result_df.columns)
        # print(self.yolo_predict.source)
        # print(self.task)
        if not result_df.empty:
            if 'class' in result_df.columns:
                result_df = result_df.drop(columns=['class'])
            # 2. 在前面插入 '文件' 和 '检测类别' 列
            result_df.insert(0, '文件名称', self.yolo_predict.source)  # 在第一列插入 '文件' 列
            result_df.insert(1, '检测类型', self.task.title)  # 在第二列插入 '检测类别' 列
            if self.task == TASK.detect:
                result_df.columns = ['文件名称', '检测类型', '对象名称', '置信度', '边界框']
            elif self.task == TASK.classify:
                result_df.columns = ['文件名称', '检测类型', '对象名称', '置信度']
            elif self.task == TASK.segment:
                result_df.columns = ['文件名称', '检测类型', '对象名称', '置信度', '边界框', '分割结果']
            elif self.task == TASK.pose:
                result_df.columns = ['文件名称', '检测类型', '对象名称', '置信度', '边界框', '检测点坐标']
            elif self.task == TASK.track:
                result_df.columns = ['文件名称', '检测类型', '对象名称', '置信度', '边界框', 'ID']

            self.detectInterface.TableWidget.setRowCount(result_df.shape[0])
            self.detectInterface.TableWidget.setColumnCount(result_df.shape[1])
            self.detectInterface.TableWidget.setHorizontalHeaderLabels(result_df)
            for i in range(result_df.shape[0]):
                for j in range(result_df.shape[1]):
                    item = QTableWidgetItem(str(result_df.iat[i, j]))
                    self.detectInterface.TableWidget.setItem(i, j, item)

        if self.input_source == INPUT_SOURCE.IMG:
            query = QSqlQuery(self.tableInterface.db)
            query.prepare("INSERT INTO yolo_data (datetime, type, result) VALUES (?, ?, ?)")
            query.addBindValue(datetime_now)
            query.addBindValue(str(self.task))
            query.addBindValue(result_info)
            query.exec()
            self.tableInterface.refresh_data()

    def get_data4chart(self):
        start_date = self.chartInterface.start_date.getDate() # 起
        end_date = self.chartInterface.end_date.getDate() # 止
        task = self.chartInterface.ComboBox_2.text()
        datetimes, results = self.tableInterface.get_results_by_date_and_type(start_date, end_date, task)
        datas = self.process_detections(datetimes, results)
        return datas

    def process_detections(self,datetimes, results):
        """
        处理 detections 数据，返回日期列表、种类列表、每天每个种类的数目列表以及每个种类的总次数
        :param datetimes: 时间列表，格式为 'yyyy-MM-dd HH:mm:ss'
        :param results: 结果列表，包含检测到的种类和数量
        :return: 日期列表, 种类列表, 每天每个种类的数目列表, 每个种类的总次数列表
        input:
        datetimes = [
            '2025-03-07 03:12:29', '2025-03-09 00:40:04', '2025-03-09 00:46:03',
            '2025-03-09 00:53:26', '2025-03-09 01:55:26'
        ]
        results = [
            '5 persons, 1 giraffe', '3 persons', '3 persons',
            '3 persons', '(no detections)'
        ]

        output:
        Dates: ['2025-03-07', '2025-03-09']
        Categories: ['giraffe', 'persons']
        Counts by category: [
            [1, 0],  # giraffe 在 2025-03-07 有 1 个，在 2025-03-09 有 0 个
            [5, 9]   # persons 在 2025-03-07 有 5 个，在 2025-03-09 有 9 个
        ]
        Total counts by category: [1, 14]  # giraffe 总次数为 1，persons 总次数为 14

        """
        # 提取日期部分并去重
        dates = sorted(set(dt.split()[0] for dt in datetimes))  # 按日期排序

        # 提取所有种类（不包括 '(no detections)'）
        categories = set()
        for result in results:
            if not 'no detections' in result:
                for item in result.split(','):
                    if item.strip():  # 忽略空字符串
                        categories.add(item.strip().split()[1])  # 提取种类名称
        categories = sorted(categories)  # 按字母顺序排序

        # 初始化每天每个种类的数目字典
        daily_counts = {date: defaultdict(int) for date in dates}

        # 初始化每个种类的总次数字典
        total_counts = defaultdict(int)

        # 遍历 datetimes 和 results，统计每天每个种类的数目和总次数
        for dt, result in zip(datetimes, results):
            date = dt.split()[0]  # 提取日期部分
            if not 'no detections' in result:
                for item in result.split(','):
                    if item.strip():  # 忽略空字符串
                        count, category = item.strip().split()
                        count = int(count)
                        daily_counts[date][category] += count
                        total_counts[category] += count

        # 将 daily_counts 转换为二维列表，与种类列表一一对应
        counts_by_category = []
        for category in categories:
            category_counts = []
            for date in dates:
                category_counts.append(daily_counts[date][category])
            counts_by_category.append(category_counts)

        # 将 total_counts 转换为列表，与种类列表一一对应
        total_counts_list = [total_counts[category] for category in categories]

        return dates, categories, counts_by_category, total_counts_list



    def update_chart(self):
        dates, categories, counts_by_category, total_counts_list = self.get_data4chart()
        chart_type = self.chartInterface.ComboBox.text()
        current_text = self.chartInterface.ComboBox_3.currentText()
        if current_text == "按天":
            dates, counts_by_category = dates, counts_by_category
        elif current_text == "按周":
            dates, counts_by_category = self.chartInterface.aggregate_by_week(dates, counts_by_category)
        elif current_text == "按月":
            dates, counts_by_category = self.chartInterface.aggregate_by_month(dates, counts_by_category)
        else:
            raise ValueError("未知的聚合方式")
        if len(dates) != 0:
            if chart_type == '饼图':
                self.chartInterface.update_pie_chart(categories, total_counts_list)
            elif chart_type == '条形图':
                self.chartInterface.update_bar_chart(dates, categories, counts_by_category)
            elif chart_type == '折线图':
                self.chartInterface.update_line_chart(dates, categories, counts_by_category)
        else:
            InfoBar.info(
                title="",
                content="没有查询到数据",
                orient=Qt.Orientation.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM_RIGHT,
                parent=self
            )
    def resizeEvent(self, e):
        super().resizeEvent(e)
    def closeEvent(self, event):
        # 保存配置
        self.save_config()
        # 退出线程和应用程序
        self.stop()

        w = Dialog('退出', "正在关闭软件，请稍等片刻。", self)
        # w.resize(400, 192)
        w.setTitleBarVisible(False)
        w.yesButton.setEnabled(False)
        # w.setContentCopyable(True)

        self.close_timer = QTimer(self)
        self.close_timer.setSingleShot(True)
        self.close_timer.timeout.connect(w.accept)
        self.close_timer.start(2000)  # 2 秒后触发 accept() 方法

        if w.exec():
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
