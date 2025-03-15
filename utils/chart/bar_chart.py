import random
from datetime import date, timedelta
from typing import List, Tuple, Optional, Sequence, Union
from collections import defaultdict

from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QComboBox
from PySide6.QtWebEngineWidgets import QWebEngineView

from pyecharts.charts import Bar
from pyecharts.charts.chart import Chart
from pyecharts.options import (
    AxisOpts,
    DataZoomOpts,
    InitOpts,
    LabelOpts,
    MarkPointItem,
    MarkPointOpts,
    TitleOpts,
    ToolBoxFeatureDataViewOpts,
    ToolBoxFeatureMagicTypeOpts,
    ToolBoxFeatureOpts,
    ToolboxOpts,
    TooltipOpts,
)

from utils.chart.chart_base import PyEChartsBase


class BarChart(PyEChartsBase):
    def __init__(
        self,
        data: List[Tuple[str, Sequence]],
        xaxis_labels: Optional[List[Union[date, str]]] = None,
        chart_title: Optional[str] = None,
        chart_subtitle: Optional[str] = None,
    ):
        super().__init__()
        self.chart = Bar(
            init_opts=InitOpts(
                theme=self.echarts_theme,
                width="100%",
                height="650px",
                is_fill_bg_color=True,
            )
        )

        tool_box_feature_magic_type_opts = ToolBoxFeatureMagicTypeOpts(
            type_=["stack", "tiled"],
        )
        tool_box_feature_opts = ToolBoxFeatureOpts(
            magic_type=tool_box_feature_magic_type_opts,
            data_view=ToolBoxFeatureDataViewOpts(is_show=False),
        )

        # 设置 x 轴标签(默认是时间)
        if xaxis_labels:
            self.chart.add_xaxis(xaxis_labels)
        else:
            # 如果没有设置x轴标签,则自动生成日期标签
            max_length = max(len(d[1]) for d in data)
            x_data = [
                date.today() - timedelta(days=max_length - i) for i in range(max_length)
            ]
            self.chart.add_xaxis(x_data)

        for name, values in data:
            self.chart.add_yaxis(
                series_name=name,
                y_axis=values,
                markpoint_opts=MarkPointOpts(
                    data=[
                        MarkPointItem(type_="max", name="最大值"),
                        MarkPointItem(type_="min", name="最小值"),
                    ]
                ),
            )

        self.chart.set_global_opts(
            title_opts=TitleOpts(title=chart_title, subtitle=chart_subtitle),
            xaxis_opts=AxisOpts(axislabel_opts=LabelOpts(rotate=-15), name="日期"),
            datazoom_opts=[
                DataZoomOpts(range_start=0, range_end=100),
                DataZoomOpts(type_="inside"),
            ],
            yaxis_opts=AxisOpts(
                axislabel_opts=LabelOpts(formatter="{value} 次"), name="数量"
            ),
            toolbox_opts=ToolboxOpts(feature=tool_box_feature_opts),
            tooltip_opts=TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )

        self.chart.set_series_opts(
            label_opts=LabelOpts(is_show=True),
        )

    def get_chart(self) -> Chart:
        return self.chart


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


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("动态柱状图 - 多类数据")
        self.resize(800, 600)

        len_data = 50
        # 生成随机数据
        self.start_date = date.today() - timedelta(days=len_data-1)
        self.dates = [self.start_date + timedelta(days=i) for i in range(len_data)]

        # 生成多类数据（A、B、C、D、E）
        self.data_A = list(zip(self.dates, [random.randint(0, 100) for _ in range(len_data)]))
        self.data_B = list(zip(self.dates, [random.randint(0, 100) for _ in range(len_data)]))
        self.data_C = list(zip(self.dates, [random.randint(0, 100) for _ in range(len_data)]))
        self.data_D = list(zip(self.dates, [random.randint(0, 100) for _ in range(len_data)]))
        self.data_E = list(zip(self.dates, [random.randint(0, 100) for _ in range(len_data)]))

        # 布局
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 添加 QComboBox
        self.combo_box = QComboBox()
        self.combo_box.addItems(["按天", "按周", "按月"])
        self.combo_box.currentTextChanged.connect(self.update_chart)
        layout.addWidget(self.combo_box)

        # 添加 QWebEngineView
        self.web = QWebEngineView()
        layout.addWidget(self.web)

        # 初始化图表
        self.update_chart()

    def update_chart(self):
        """根据 QComboBox 的选择更新图表"""
        current_text = self.combo_box.currentText()

        # 根据选择的时间粒度聚合数据
        if current_text == "按天":
            aggregated_data_A = aggregate_by_day(self.data_A)
            aggregated_data_B = aggregate_by_day(self.data_B)
            aggregated_data_C = aggregate_by_day(self.data_C)
            aggregated_data_D = aggregate_by_day(self.data_D)
            aggregated_data_E = aggregate_by_day(self.data_E)
        elif current_text == "按周":
            aggregated_data_A = aggregate_by_week(self.data_A)
            aggregated_data_B = aggregate_by_week(self.data_B)
            aggregated_data_C = aggregate_by_week(self.data_C)
            aggregated_data_D = aggregate_by_week(self.data_D)
            aggregated_data_E = aggregate_by_week(self.data_E)
        elif current_text == "按月":
            aggregated_data_A = aggregate_by_month(self.data_A)
            aggregated_data_B = aggregate_by_month(self.data_B)
            aggregated_data_C = aggregate_by_month(self.data_C)
            aggregated_data_D = aggregate_by_month(self.data_D)
            aggregated_data_E = aggregate_by_month(self.data_E)
        else:
            raise ValueError("未知的聚合方式")

        # 提取日期和值
        dates_A, values_A = zip(*aggregated_data_A)
        dates_B, values_B = zip(*aggregated_data_B)
        dates_C, values_C = zip(*aggregated_data_C)
        dates_D, values_D = zip(*aggregated_data_D)
        dates_E, values_E = zip(*aggregated_data_E)

        # 确保日期一致（按周或按月聚合后，各类数据的日期可能不完全一致）
        dates = sorted(set(dates_A).union(set(dates_B)).union(set(dates_C)).union(set(dates_D)).union(set(dates_E)))
        values_A_aligned = [values_A[dates_A.index(d)] if d in dates_A else 0 for d in dates]
        values_B_aligned = [values_B[dates_B.index(d)] if d in dates_B else 0 for d in dates]
        values_C_aligned = [values_C[dates_C.index(d)] if d in dates_C else 0 for d in dates]
        values_D_aligned = [values_D[dates_D.index(d)] if d in dates_D else 0 for d in dates]
        values_E_aligned = [values_E[dates_E.index(d)] if d in dates_E else 0 for d in dates]

        # 生成图表
        bar_chart = BarChart(
            [
                ("A", values_A_aligned),
                ("B", values_B_aligned),
                ("C", values_C_aligned),
                ("D", values_D_aligned),
                ("E", values_E_aligned),
            ],
            xaxis_labels=dates,
            chart_title=f"{current_text}聚合数据 - 多类数据",
        )
        self.web.setHtml(bar_chart.get_chart().render_embed())


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()