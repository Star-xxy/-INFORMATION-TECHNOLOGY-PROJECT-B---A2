# coding:utf-8
import random
import sys
from collections import defaultdict
from datetime import datetime, timedelta, date
from typing import List, Tuple

from tasks import TASK

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QUrl, QRectF, QEvent, QObject, QDate
from PySide6.QtGui import QIcon, QPainter, QBrush, QColor, QDesktopServices, QPixmap, QPainterPath, \
    QLinearGradient
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QApplication, QStackedWidget, QHBoxLayout, QWidget, QFileDialog, \
    QGraphicsDropShadowEffect, QTableView, QMessageBox, QHeaderView, QFrame

from PySide6.QtGui import QIntValidator
from pyecharts import options as opts
from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox,
                            isDarkTheme, setThemeColor, InfoBar, InfoBarPosition)

from ui.chart import Ui_Frame as UI_home
from utils.chart import PieChart, BarChart, LineChart
from utils.style_sheet import StyleSheet


def aggregate_by_day(data: List[Tuple[date, int]]) -> List[Tuple[date, int]]:
    """按天聚合（原始数据）"""
    return data


def aggregate_by_week(data: List[Tuple[date, int]]) -> List[Tuple[date, int]]:
    """按周聚合"""
    aggregated_data = defaultdict(int)
    for day, value in data:
        start_of_week = day - timedelta(days=day.weekday())
        aggregated_data[start_of_week] += value
    return sorted(aggregated_data.items())


def aggregate_by_month(data: List[Tuple[date, int]]) -> List[Tuple[date, int]]:
    """按月聚合"""
    aggregated_data = defaultdict(int)
    for day, value in data:
        start_of_month = date(day.year, day.month, 1)
        aggregated_data[start_of_month] += value
    return sorted(aggregated_data.items())


class WidgetChart(QFrame, UI_home):

    def __init__(self, name: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(name)
        self.setupUi(self)

        StyleSheet.WIDGET_CHART.apply(self)
        for task in TASK:
            if task != TASK.classify:
                self.ComboBox_2.addItem(task.title)
        self.ComboBox.addItem('饼图')
        self.ComboBox.addItem('条形图')
        self.ComboBox.addItem('折线图')

        self.start_date.setDate(QDate(2024, 1, 1))
        self.end_date.setDate(QDate(2030, 1, 1))

        self.ComboBox_3.addItem('按天')
        self.ComboBox_3.addItem('按周')
        self.ComboBox_3.addItem('按月')


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

    def update_pie_chart(self, categories, counts):
        data = list(zip(categories, counts))
        pie = PieChart(
            data=data,
            chart_title="饼图",
            chart_subtitle="",
        )
        # 将图表渲染为HTML并加载到浏览器中
        self.webEngineView.setHtml(pie.get_chart().render_embed())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WidgetChart('chart')
    w.show()
    app.exec()
