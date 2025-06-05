# user.py
# coding:utf-8
import sys
from collections import defaultdict
from datetime import datetime, timedelta

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QUrl, QRectF, QPropertyAnimation, QEasingCurve, QDate
from PySide6.QtGui import QIcon, QPainter, QBrush, QColor, QDesktopServices, QPixmap, QPainterPath, QLinearGradient
from PySide6.QtWidgets import QApplication, QStackedWidget, QHBoxLayout, QWidget, QFileDialog, QFrame, QMessageBox, \
    QDialog

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox, isDarkTheme, setThemeColor)
from ui.dialog_modify import WidgetInfoModify  # 引入修改界面
from utils.chart import BarChart, LineChart
from utils.database import *  # 引入数据库操作

from ui.user import Ui_Frame as UI_user
from utils.style_sheet import StyleSheet


class WidgetUser(QFrame, UI_user):
    def __init__(self, name: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(name)
        self.setupUi(self)
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)
        self.init_connections()
        self.user_info = None  # 保存用户信息

        self.start_date.setDate(QDate(2024, 1, 1))
        self.end_date.setDate(QDate(2030, 1, 1))

        self.ComboBox_5.addItem('Bar chart')
        self.ComboBox_5.addItem('Line chart')

        self.ComboBox_4.addItem('By day')
        self.ComboBox_4.addItem('By week')
        self.ComboBox_4.addItem('By month')

        self.PushButton.clicked.connect(self.report_week)
        self.PushButton_2.clicked.connect(self.report_month)


    def report_week(self):
        self.BodyLabel_13.setText('From April 7 to April 13, 2025, I completed four yoga sessions focused on flexibility, balance, and breathwork. Vinyasa and Hatha styles were practiced, with noticeable progress in hamstring flexibility and pose stability. A minor wrist strain occurred during one session, highlighting the need for careful alignment in weight-bearing poses. Next week, I plan to include a restorative session and work more on core strength.')


    def report_month(self):
        self.BodyLabel_13.setText('Between March 16 and April 15, 2025, I maintained a consistent yoga routine with 16 sessions in total, improving flexibility, core strength, and breathing control. Highlights include holding Crow Pose, improved focus in meditative breathing, and steady practice habits. Challenges involved wrist discomfort and backbend transitions. Next month, I aim to join a weekly group class and begin learning more advanced poses like Headstand.')

    def aggregate_by_week(self, dates, counts_by_category):
        """
        将按天的统计转换为按周的统计
        :param dates: 原始日期列表 ['2025-03-07', '2025-03-09', ...]
        :param counts_by_category: 原始按天统计的二维列表 [[1,0,...], [5,9,...], ...]
        :return: 周日期列表, 按周统计的counts_by_category
        """
        # 将字符串日期转换为datetime对象
        date_objs = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

        # 找到起始周和结束周（周一作为每周的开始）
        week_starts = []
        week_counts = defaultdict(lambda: defaultdict(int))

        # 对每个日期进行分组
        for i, date_obj in enumerate(date_objs):
            # 获取周一的日期作为本周的标识
            days_since_monday = date_obj.weekday()  # 0=周一, 6=周日
            week_start = date_obj - timedelta(days=days_since_monday)
            week_start_str = week_start.strftime('%Y-%m-%d')

            # 记录周开始日期
            if week_start_str not in week_starts:
                week_starts.append(week_start_str)

            # 累加该周的计数
            for cat_idx, daily_counts in enumerate(counts_by_category):
                week_counts[week_start_str][cat_idx] += daily_counts[i]

        # 按日期排序
        week_starts.sort()

        # 转换为输出格式
        new_counts_by_category = []
        for cat_idx in range(len(counts_by_category)):
            category_counts = [week_counts[week_start][cat_idx] for week_start in week_starts]
            new_counts_by_category.append(category_counts)

        return week_starts, new_counts_by_category

    def aggregate_by_month(self, dates, counts_by_category):
        """
        将按天的统计转换为按月的统计
        :param dates: 原始日期列表 ['2025-03-07', '2025-03-09', ...]
        :param counts_by_category: 原始按天统计的二维列表 [[1,0,...], [5,9,...], ...]
        :return: 月日期列表, 按月统计的counts_by_category
        """
        # 将字符串日期转换为datetime对象
        date_objs = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

        # 按月分组
        month_starts = []
        month_counts = defaultdict(lambda: defaultdict(int))

        # 对每个日期进行分组
        for i, date_obj in enumerate(date_objs):
            # 获取每月的第一天作为标识
            month_start = date_obj.replace(day=1)
            month_start_str = month_start.strftime('%Y-%m-%d')

            # 记录月开始日期
            if month_start_str not in month_starts:
                month_starts.append(month_start_str)

            # 累加该月的计数
            for cat_idx, daily_counts in enumerate(counts_by_category):
                month_counts[month_start_str][cat_idx] += daily_counts[i]

        # 按日期排序
        month_starts.sort()

        # 转换为输出格式
        new_counts_by_category = []
        for cat_idx in range(len(counts_by_category)):
            category_counts = [month_counts[month_start][cat_idx] for month_start in month_starts]
            new_counts_by_category.append(category_counts)

        return month_starts, new_counts_by_category


    def update_bar_chart(self, dates, categories, counts_by_category):
        bar_chart = BarChart(
            data=[(categories[i], counts_by_category[i]) for i in range(len(categories))],
            xaxis_labels=dates,
            chart_title=f"",
        )

        # 将图表渲染为HTML并加载到浏览器中
        self.webEngineView.setHtml(bar_chart.get_chart().render_embed())

    def update_line_chart(self, dates, categories, counts_by_category):
        line = LineChart(
            data=[(categories[i], counts_by_category[i]) for i in range(len(categories))],
            xaxis_labels=dates,
            chart_title=f"",
        )

        # 将图表渲染为HTML并加载到浏览器中
        self.webEngineView.setHtml(line.get_chart().render_embed())

    def init_connections(self):
        # 绑定 PrimaryPushButton 的点击事件
        self.PrimaryPushButton.clicked.connect(self.open_modify_dialog)

    def open_modify_dialog(self):
        # 创建修改窗口并传入当前用户信息
        modify_dialog = WidgetInfoModify("ModifyUserInfo", self.user_info, self)
        modify_dialog.exec()  # 显示对话框（模态）

        # 如果对话框确认保存（通过信号或直接返回值判断），更新界面显示
        if modify_dialog.result() == QDialog.DialogCode.Accepted:
            self.update_user_info(modify_dialog.get_updated_info())

    def update_user_info(self, info):
        # 更新界面显示
        self.BodyLabel_2.setText(str(info.get('username', '')))
        self.BodyLabel_4.setText(str(info.get('age', 0)))
        self.BodyLabel_6.setText(str(info.get('weight', 0)))
        self.BodyLabel_8.setText(str(info.get('training_days', 0)))
        self.BodyLabel_10.setText(str(info.get('training_time', 0)))
        self.user_info.update(info)  # 更新本地存储的用户信息

