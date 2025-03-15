# coding:utf-8
import random
import sys
from datetime import datetime, timedelta

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QUrl, QRectF, QEvent, QObject, QDate
from PySide6.QtGui import QIcon, QPainter, QBrush, QColor, QDesktopServices, QPixmap, QPainterPath, \
    QLinearGradient
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QApplication, QStackedWidget, QHBoxLayout, QWidget, QFileDialog, \
    QGraphicsDropShadowEffect, QTableView, QMessageBox, QHeaderView, QFrame

from PySide6.QtGui import QIntValidator
from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox,
                            isDarkTheme, setThemeColor, InfoBar, InfoBarPosition)

from tasks import TASK
from ui.data_table import Ui_Frame as UI_home
from utils.style_sheet import StyleSheet


class WidgetTable(QFrame, UI_home):

    def __init__(self, name: str, db_path: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(name)
        self.setupUi(self)


        # 创建数据库连接
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(db_path)

        if not self.db.open():
            QMessageBox.critical(self, "无法打开数据库", "无法建立数据库连接。")
            sys.exit(1)

        # 检查并创建表
        self.create_table_if_not_exists()

        # 设置分页属性
        self.page_size = 100
        self.current_page = 1
        self.total_pages = 1
        self.order_by = "datetime"
        self.order_direction = "ASC"
        self.filter_str = ""  # Initialize filter_str here

        self.search_input.searchSignal.connect(lambda: self.search_entries(True))
        self.search_button.clicked.connect(lambda: self.search_entries(True))
        self.clear_button.clicked.connect(self.clear_search)

        self.start_date.dateChanged.connect(lambda: self.search_entries(True))
        self.end_date.dateChanged.connect(lambda: self.search_entries(True))
        self.ComboBox.currentTextChanged.connect(lambda: self.search_entries(True))

        self.prev_button.clicked.connect(self.prev_page)
        self.next_button.clicked.connect(self.next_page)
        self.goto_page_button.clicked.connect(self.goto_page)

        # 创建查询模型
        self.model = QSqlQueryModel(self)

        # 创建表视图并添加排序功能
        self.table_view.setModel(self.model)
        self.table_view.setSortingEnabled(True)
        self.table_view.setBorderVisible(True)
        self.table_view.setBorderRadius(8)
        self.table_view.verticalHeader().hide()
        # self.table_view.setWordWrap(False)
        self.table_view.resizeColumnsToContents()
        # self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        header = self.table_view.horizontalHeader()
        header.setStretchLastSection(True)  # 使最后一列填充剩余空间
        header.sortIndicatorChanged.connect(self.on_sort_indicator_changed)  # 连接排序指示器更改信号
        header.setStyleSheet("QHeaderView::section { font-weight: bold; }")

        # 限制输入int
        int_validator = QIntValidator()
        self.goto_page_input.setValidator(int_validator)

        # 初始化日期
        self.start_date.setDate(QDate(2024, 1, 1))
        self.end_date.setDate(QDate(2030, 1, 1))
        # self.generate_test_data()

        self.update_model()
        self.table_view.setColumnWidth(0, 200)  # 设置日期列宽度
        self.table_view.setColumnWidth(1, 200)  # 设置日期列宽度
        self.table_view.verticalHeader().hide()

        self.ComboBox.addItem('所有')
        for task in TASK:
            self.ComboBox.addItem(task.title)
        StyleSheet.WIDGET_TABLE.apply(self)
    def create_table_if_not_exists(self):
        query = QSqlQuery(self.db)
        query.exec(
            "CREATE TABLE IF NOT EXISTS yolo_data ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "datetime TEXT NOT NULL, "
            "type TEXT NOT NULL, "
            "result TEXT NOT NULL)"
        )

    def update_model(self):
        # 计算偏移量
        offset = (self.current_page - 1) * self.page_size

        # 构建查询语句
        query_str = f"SELECT datetime, type, result FROM yolo_data"
        if self.filter_str:
            query_str += f" WHERE {self.filter_str}"
        query_str += f" ORDER BY {self.order_by} {self.order_direction} LIMIT {self.page_size} OFFSET {offset}"

        # 更新模型查询
        self.model.setQuery(query_str, self.db)

        # 计算总页数
        total_query_str = f"SELECT COUNT(*) FROM yolo_data"
        if self.filter_str:
            total_query_str += f" WHERE {self.filter_str}"
        total_query = QSqlQuery(self.db)
        total_query.exec(total_query_str)
        total_query.next()
        total_count = total_query.value(0)
        if not total_count:
            total_count = 1
        self.total_pages = (total_count + self.page_size - 1) // self.page_size

        # 更新页码标签
        self.page_label.setText(f"{self.current_page}/{self.total_pages}")
        # 更新分页按钮状态
        self.prev_button.setEnabled(self.current_page > 1)
        self.next_button.setEnabled(self.current_page < self.total_pages)

    def on_sort_indicator_changed(self, index, order):
        # Adjust index to exclude the hidden ID column
        column = index
        headers = ["datetime", "type"]  # Column names list
        if column < 2:
            self.order_by = headers[column]
            self.order_direction = "ASC" if order == Qt.SortOrder.AscendingOrder else "DESC"
            self.update_model()

    def search_entries(self, use_date=True):
        search_text = self.search_input.text()
        start_date = self.start_date.getDate().toString('yyyy-MM-dd') + ' 00:00:00'
        end_date = self.end_date.getDate().toString('yyyy-MM-dd') + ' 23:59:59'

        filter_str = ""
        if search_text:
            filter_str += f"(result LIKE '%{search_text}%' OR type LIKE '%{search_text}%' OR datetime LIKE '%{search_text}%')"

        if use_date and start_date and end_date:
            if filter_str:
                filter_str += " AND "
            filter_str += f"datetime BETWEEN '{start_date}' AND '{end_date}'"

        # 添加 ComboBox 的逻辑
        selected_type = self.ComboBox.currentText()
        if selected_type != '所有':
            if filter_str:
                filter_str += " AND "
            filter_str += f"type = '{selected_type}'"

        self.filter_str = filter_str  # 保存过滤条件
        self.current_page = 1  # Reset to first page
        self.update_model()

    def clear_search(self):
        self.search_input.clear()
        self.start_date.setDate(QDate(2024, 1, 1))
        self.end_date.setDate(QDate(2030, 1, 1))
        self.ComboBox.setCurrentText('所有')
        self.filter_str = ""  # 清除过滤条件
        self.search_entries()

    def refresh_data(self):
        self.current_page = 1  # 重置页码为1
        self.update_model()

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_model()

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_model()

    def goto_page(self):
        try:
            page_number = int(self.goto_page_input.text())
        except ValueError:
            InfoBar.info(
                title="",
                content="请输入有效查询",
                orient=Qt.Orientation.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM_RIGHT,
                parent=self
            )
            return
        page_number = int(self.goto_page_input.text())
        if page_number < 1:
            self.current_page = 1
        elif page_number > self.total_pages:
            self.current_page = self.total_pages
        else:
            self.current_page = page_number
        self.update_model()

    def generate_test_data(self):
        query = QSqlQuery(self.db)
        classes = ['person', 'bicycle', 'car', 'motorcycle', 'airplane']
        # 生成 1000 条测试数据
        for _ in range(100):
            # 随机生成日期时间
            random_days = random.randint(0, 180)  # 在过去半年内随机选择日期
            random_datetime = datetime.now() - timedelta(days=random_days)
            formatted_datetime = random_datetime.strftime('%Y-%m-%d %H:%M:%S')  # 更正格式字符串

            # 随机生成类型和结果
            random_type = random.choice(list(i.title for i in TASK))
            random_result = ', '.join([f"{random.randint(1, 10)} {cls}" for cls in classes])

            # 执行插入语句
            query.prepare(
                "INSERT INTO yolo_data (datetime, type, result) VALUES (?, ?, ?)"
            )
            query.addBindValue(formatted_datetime)
            query.addBindValue(random_type)
            query.addBindValue(random_result)
            query.exec()

    def get_results_by_date_and_type(self, start_date: QDate, end_date: QDate, type: str):
        """
        根据起始日期、终止日期和类型获取所有结果
        :param start_date: 起始日期，QDate 对象
        :param end_date: 终止日期，QDate 对象
        :param type: 类型
        :return: 两个列表，分别存放 datetime 和 result
        """
        # 将 QDate 转换为字符串
        start_datetime = start_date.toString('yyyy-MM-dd') + ' 00:00:00'
        end_datetime = end_date.toString('yyyy-MM-dd') + ' 23:59:59'

        # 修改查询语句以获取 datetime, result
        query_str = f"SELECT datetime, result FROM yolo_data WHERE datetime BETWEEN '{start_datetime}' AND '{end_datetime}' AND type = '{type}'"
        query = QSqlQuery(self.db)
        query.exec(query_str)

        datetimes = []  # 存放 datetime 的列表
        results = []  # 存放 result 的列表

        while query.next():
            datetime = query.value(0)  # 获取 datetime
            result = query.value(1)  # 获取 result
            datetimes.append(datetime)  # 添加到 datetime 列表
            results.append(result)  # 添加到 result 列表

        return (datetimes, results)  # 返回两个列表

    def clear_all_data(self):
        reply = QMessageBox.question(self, "确认清空", "你确定要清空所有数据吗？此操作无法撤销。",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            query = QSqlQuery(self.db)
            query.exec("DELETE FROM yolo_data")
            self.refresh_data()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WidgetTable('123', '../database/database.db')
    w.show()
    app.exec()

