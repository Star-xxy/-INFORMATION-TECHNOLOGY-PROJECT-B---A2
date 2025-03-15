# import os
# import sys
# import time
#
# from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtWebEngineWidgets import QWebEngineView
# from PySide6.QtCore import QUrl
#
#
# from pyecharts.charts import Bar
# from pyecharts import options as opts
#
# # V1 版本开始支持链式调用
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
#     .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
#     .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# )
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QMainWindow()
#     window.setWindowTitle("Simple Web Test")
#     window.setGeometry(100, 100, 800, 600)
#     browser = QWebEngineView()
#     window.setCentralWidget(browser)
#     browser.setHtml(bar.render_embed())
#     window.show()
#     sys.exit(app.exec())


import os
import sys
import time
import random

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QTimer

from pyecharts.charts import Bar, Pie, Line
from pyecharts import options as opts
from pyecharts.faker import Faker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("实时数据刷新示例")
        self.setGeometry(100, 100, 800, 600)

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # 初始化数据
        self.categories = ["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]
        self.data_a = [114, 55, 27, 101, 125, 27, 105]
        self.data_b = [57, 134, 137, 129, 145, 60, 49]

        # 初始化图表
        self.update_chart()

        # 设置定时器，每隔1秒更新一次数据
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(5000)

    def update_data(self):
        # 随机更新数据
        self.data_a = [random.randint(50, 150) for _ in range(len(self.categories))]
        self.data_b = [random.randint(50, 150) for _ in range(len(self.categories))]

        # 更新图表
        self.update_chart()

    def update_chart(self):
        # 创建新的柱状图
        # bar = (
        #     Bar()
        #     .add_xaxis(self.categories)
        #     .add_yaxis("商家A", self.data_a)
        #     .add_yaxis("商家B", self.data_b)
        #     .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
        # )

        # pie = (Pie()
        #        .add('', [list(z) for z in zip(self.categories, self.data_a)],
        #             radius=["30%", "75%"],
        #             rosetype="radius"
        #             )
        #        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        #        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
        #        )

        line = (
            Line()
            .set_global_opts(
                tooltip_opts=opts.TooltipOpts(is_show=False),
                xaxis_opts=opts.AxisOpts(type_="category"),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
            )
            .add_xaxis(xaxis_data=self.categories)
            .add_yaxis(
                series_name="",
                y_axis=self.data_a,
                symbol="emptyCircle",
                is_symbol_show=True,
                label_opts=opts.LabelOpts(is_show=False),
            )
        )

        # 将图表渲染为HTML并加载到浏览器中
        self.browser.setHtml(line.render_embed())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())