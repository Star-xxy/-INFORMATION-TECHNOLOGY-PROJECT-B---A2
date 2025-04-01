import base64
import time
from pathlib import Path
from PySide6.QtCore import QMutex, QSemaphore, QEvent
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QApplication, QFileDialog, QTableWidgetItem, QHeaderView
from PySide6.QtGui import QImage, QPixmap, Qt, QIcon
from PySide6.QtCore import QTimer, QThread, Signal, QDateTime
from openai import OpenAI
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

class MainWindow(Window):
    main2yolo_begin_sgl = Signal()  # 主视窗向 YOLO 实例发送执行信号
    input_source = None  # img video webcam

    def __init__(self, user_info):
        super().__init__()
        self.user_info = user_info

        self.init_ui()
        self.init_yolo()
        self.init_signal()
        self.init_config()

        self.update_user_info(user_info)

        self.client = OpenAI(
            api_key="sk-627a7f6f36e84ae5a90e69c96c130af4",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )



    def init_config(self):
        self.change_model()
        self.yolo_predict.task = TASK.pose

    def init_ui(self):
        self.show()
        QApplication.processEvents()
        self.analyzeInterface.progress_bar.setValue(0)
        image = QImage('resource/images/icons/office-man.png')
        resized_image = image.scaled(96, 96)
        self.analyzeInterface.AvatarWidget.setImage(resized_image)
        self.userInterface.AvatarWidget.setImage(resized_image)

    def init_signal(self):
        self.analyzeInterface.run_button.clicked.connect(self.run_or_continue)  # 暂停/开始
        self.analyzeInterface.stop_button.clicked.connect(self.stop)  # 终止

        self.analyzeInterface.ToolButton.clicked.connect(self.get_image)
        self.analyzeInterface.ToolButton_2.clicked.connect(self.get_video)
        self.analyzeInterface.ToolButton_3.clicked.connect(self.get_webcam)
        self.analyzeInterface.PrimaryToolButton.clicked.connect(self.analyzeInterface.run_button.click)

        self.userInterface.refresh_button_2.clicked.connect(self.update_chart)
        self.userInterface.ComboBox_4.currentTextChanged.connect(self.update_chart)
        self.userInterface.ComboBox_5.currentTextChanged.connect(self.update_chart)
        self.userInterface.start_date.dateChanged.connect(self.update_chart)
        self.userInterface.end_date.dateChanged.connect(self.update_chart)
        self.update_chart()

        self.is_resizing = False

        self.analyzeInterface.res_video.installEventFilter(self)
        self.analyzeInterface.pre_video.installEventFilter(self)

        self.resizing_timer = QTimer(self)
        self.resizing_timer.setInterval(500)  # 设置定时器的间隔为500毫秒（即0.5秒）
        self.resizing_timer.timeout.connect(self.on_timer_timeout)
        self.resizing_timer.start()

    def on_timer_timeout(self):
        self.is_resizing = False

    def init_yolo(self):
        self.select_model = 'yolov8n-pose.pt'  # 默认模型
        self.task = TASK.pose
        # YOLO-v8 线程
        self.yolo_predict = YoloPredictor()  # 创建 YOLO 实例
        self.yolo_predict.save_res = cfg.get(cfg.is_save_results)
        self.yolo_predict.save_dir = Path(cfg.get(cfg.save_path))
        self.yolo_thread = QThread()  # 创建 YOLO 线程
        self.yolo_predict.yolo2main_pre_img.connect(
            lambda x: self.show_image(x, self.analyzeInterface.pre_video, 'origin'))
        self.yolo_predict.yolo2main_res_img.connect(
            lambda x: self.show_image(x, self.analyzeInterface.res_video, 'img'))

        self.yolo_predict.yolo2main_progress.connect(lambda x: self.analyzeInterface.progress_bar.setValue(x))
        self.yolo_predict.yolo2main_stop.connect(self.stop)
        self.main2yolo_begin_sgl.connect(self.yolo_predict.run)
        self.yolo_predict.moveToThread(self.yolo_thread)


    def update_user_info(self, info):

        username = info.get('username', '')
        mail = info.get('mail', '')
        age = info.get('age', 0)
        weight = info.get('weight', 0)
        training_days = info.get('training_days', 0)
        training_time = info.get('training_time', 0)
        level = info.get('level', 0)
        points = info.get('points', 0)

        self.analyzeInterface.StrongBodyLabel.setText(str(username))
        self.analyzeInterface.BodyLabel_7.setText(str(training_days))
        self.analyzeInterface.BodyLabel_10.setText(str(training_time))
        self.analyzeInterface.BodyLabel_8.setText(str(level))
        self.analyzeInterface.BodyLabel_9.setText(str(points))
        self.userInterface.user_info = info
        self.userInterface.update_user_info(info)  # 更新本地存储的用户信息

    def switchToSample(self, task):
        self.detect_page(task)

    def change_model(self):
        # 获取当前选择的模型名称
        self.yolo_predict.new_model_name = "./models/pose/%s" % self.select_model


    def detect_page(self, task):
        self.task = task
        self.yolo_predict.task = self.task
        self.yolo_predict.new_model_name = f"./models/{self.task.folder}/%s" % self.select_model


    def get_image(self):
        name, _ = QFileDialog.getOpenFileName(self, '图片', cfg.get(cfg.open_fold), "Picture File(*.jpg *.png *.jpeg)")
        if name:
            cfg.set(cfg.open_fold, os.path.dirname(name))
            self.input_source = INPUT_SOURCE.IMG
            # 将所选档案的路径设置为 yolo_predict 的 source
            self.yolo_predict.source = name
            self.clear_canvas()

            # 停止检测
            self.stop()

            self.stackedWidget.setCurrentWidget(self.analyzeInterface)

    def get_video(self):
        name, _ = QFileDialog.getOpenFileName(self, '视频', cfg.get(cfg.open_fold),
                                              "Video File(*.gif *.mp4 *.mkv *.avi *.flv)")
        if name:
            cfg.set(cfg.open_fold, os.path.dirname(name))
            self.input_source = INPUT_SOURCE.VIDEO
            # 将所选档案的路径设置为 yolo_predict 的 source
            self.yolo_predict.source = name


            # 停止检测
            self.stop()

            self.stackedWidget.setCurrentWidget(self.analyzeInterface)

    def get_webcam(self):
        self.input_source = INPUT_SOURCE.WEBCAM
        # 将所选档案的路径设置为 yolo_predict 的 source
        self.yolo_predict.source = 0

        if self.yolo_thread.isRunning():
            self.yolo_thread.quit()  # 结束线程
            self.stop()

        self.stackedWidget.setCurrentWidget(self.analyzeInterface)

    def run_or_continue(self):
        # 有输入
        if self.input_source:
            # 检查 YOLO 预测的来源是否为空
            if self.yolo_predict.source == '':
                self.analyzeInterface.run_button.setChecked(False)
            else:
                # 设置 YOLO 预测的停止标志为 False
                self.yolo_predict.stop_dtc = False

                # 如果开始按钮被勾选
                if self.analyzeInterface.run_button.isChecked():
                    self.analyzeInterface.run_button.setChecked(True)  # 启动按钮
                    self.yolo_predict.continue_dtc = True  # 控制 YOLO 是否暂停


                    if not self.yolo_thread.isRunning():
                        self.yolo_thread.start()
                        self.main2yolo_begin_sgl.emit()
                # 如果开始按钮未被勾选，表示暂停检测
                else:
                    self.yolo_predict.continue_dtc = False
                    self.analyzeInterface.run_button.setChecked(False)  # 停止按钮

    def clear_canvas(self):
        # 清空预测结果显示区域的影象
        self.analyzeInterface.pre_video.clear()

        # 清空检测结果显示区域的影象
        self.analyzeInterface.res_video.clear()

        # 将进度条的值设置为0
        self.analyzeInterface.progress_bar.setValue(0)

    def stop(self):
        # 如果 YOLO 线程正在运行，则终止线程
        if self.yolo_thread.isRunning():
            self.yolo_thread.quit()  # 结束线程

        # 设置 YOLO 实例的终止标志为 True
        self.yolo_predict.stop_dtc = True

        # 恢复开始按钮的状态
        self.analyzeInterface.run_button.setChecked(False)

        if self.input_source != INPUT_SOURCE.IMG:
            self.clear_canvas()

    def get_ai_responce(self, img_src):

        _, buffer = cv2.imencode('.jpg', img_src)
        image_base64 = base64.b64encode(buffer).decode('utf-8')
        image_to_base64 = f"data:image/jpeg;base64,{image_base64}"
        messages = [
            {
                "role": "system",
                "content": [{"type": "text", "text": "You are a yoga instructor assistant."}],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_to_base64
                        },
                    },
                    {
                        "type": "text",
                        "text": "Analyze the yoga pose in the image and provide feedback in three parts: "
                                "'Correct posture', 'User's posture', and 'Adjustment suggestions'. "
                                "Include the name of the yoga pose in the 'Correct posture' section, "
                                "formatted as 'known as [Sanskrit name]'. "
                                "Use English for the response and clearly label each section as '**Correct posture:** ', "
                                "'**User's posture:** ', and '**Adjustment suggestions:** ' followed by the description."
                    },
                ],
            },
        ]
        completion = self.client.chat.completions.create(
            model="qwen-omni-turbo",
            messages=messages,
            modalities=["text"],
            stream=True,
            stream_options={"include_usage": True}
        )

        full_response = ""
        for chunk in completion:
            if chunk.choices and chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
        return full_response

    def split_response(self, response):
        parts = response.split('\n\n')  # Split by double newlines
        if len(parts) >= 3:
            # Remove the bolded labels and extract pose name from "Correct posture"
            correct_posture = parts[0].replace("**Correct posture:** ", "")
            users_posture = parts[1].replace("**User's posture:** ", "")
            adjustment_suggestions = parts[2].replace("**Adjustment suggestions:** ", "")

            # Extract pose name (assuming it's mentioned in "Correct posture" like "Navasana (Boat Pose)")
            pose_name = "Unknown"
            if "known as" in correct_posture:
                start_idx = correct_posture.index("known as") + len("known as ")
                end_idx = correct_posture.index(")", start_idx) if ")" in correct_posture[start_idx:] else len(
                    correct_posture)
                pose_name = correct_posture[start_idx:end_idx + 1].strip()

            return {
                "Pose name": pose_name,
                "Correct posture": correct_posture,
                "User's posture": users_posture,
                "Adjustment suggestions": adjustment_suggestions
            }
        else:
            return {
                "Pose name": "N/A",
                "Correct posture": "N/A",
                "User's posture": "N/A",
                "Adjustment suggestions": "N/A"
            }

    def show_image(self, img_src, label, flag):
        if self.is_resizing:  # 如果正在调整大小，暂时不更新图像
            return

        try:
            if flag == "path":
                img_src = cv2.imdecode(np.fromfile(img_src, dtype=np.uint8), -1)
            if flag == "origin":
                if self.input_source == INPUT_SOURCE.IMG:
                    full_response = self.get_ai_responce(img_src)
                    response_parts = self.split_response(full_response)

                    self.analyzeInterface.BodyLabel_12.setText(response_parts["Correct posture"])
                    self.analyzeInterface.BodyLabel_13.setText(response_parts["User's posture"])
                    self.analyzeInterface.BodyLabel_14.setText(response_parts["Adjustment suggestions"])

            ih, iw, _ = img_src.shape
            w = label.geometry().width()
            h = label.geometry().height()

            # 保持纵横比
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
                frame = cv2.cvtColor(img_src_, cv2.COLOR_BGR2RGB).copy()
                img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                             QImage.Format.Format_RGB888)
                label.setPixmap(QPixmap.fromImage(img))
        except Exception as e:
            print(f"Error in show_image: {e}")


    def update_chart(self):
        start_date = self.userInterface.start_date.getDate() # 起
        end_date = self.userInterface.end_date.getDate() # 止
        dates, counts_by_category, yoga_poses = self.userInterface.db.query_activities_by_date_and_pose(start_date, end_date)

        chart_type = self.userInterface.ComboBox_5.text()
        current_text = self.userInterface.ComboBox_4.currentText()

        if current_text == "By day":
            dates, counts_by_category = dates, counts_by_category
        elif current_text == "By week":
            dates, counts_by_category = self.userInterface.aggregate_by_week(dates, counts_by_category)
        elif current_text == "By month":
            dates, counts_by_category = self.userInterface.aggregate_by_month(dates, counts_by_category)
        else:
            raise ValueError("unknow")
        if len(dates) != 0:
            if chart_type == 'Bar chart':
                self.userInterface.update_bar_chart(dates, yoga_poses, counts_by_category)
            elif chart_type == 'Line chart':
                self.userInterface.update_line_chart(dates, yoga_poses, counts_by_category)
        else:
            InfoBar.info(
                title="",
                content="没有查询到数据",
                orient=Qt.Orientation.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM_RIGHT,
                parent=self
            )

    def eventFilter(self, obj, event):
        # 监听 resizeEvent
        if event.type() == QEvent.Type.Resize:
            self.is_resizing = True  # 正在调整大小
        return super().eventFilter(obj, event)

    def closeEvent(self, event):
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
    user_info = {'age': 12, 'level': 0, 'mail': '123@qq.com', 'password': '111111', 'points': 0, 'training_days': 0, 'training_time': 0, 'username': '1234', 'weight': 12.0}
    app = QApplication(sys.argv)
    w = MainWindow(user_info=user_info)
    w.show()
    app.exec()
