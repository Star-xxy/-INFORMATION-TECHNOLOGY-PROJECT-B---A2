# coding:utf-8
import sys

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QUrl, QRectF, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon, QPainter, QBrush, QColor, QDesktopServices, QPixmap, QPainterPath, \
    QLinearGradient
from PySide6.QtWidgets import QApplication, QStackedWidget, QHBoxLayout, QWidget, QFileDialog, QFrame

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox,
                            isDarkTheme, setThemeColor)

from ui.detect import Ui_Frame as UI_detect
from utils.style_sheet import StyleSheet


class WidgetDetect(QFrame, UI_detect):

    def __init__(self, name: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(name)
        self.setupUi(self)

        self.param_button.clicked.connect(lambda: self.slideRightMenu())

        StyleSheet.WIDGET_DETECT.apply(self)

    def slideRightMenu(self):
        # Get current left menu width
        width = self.right_param_frame.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 320
        # If maximized
        else:
            # Restore menu
            newWidth = 0

        # Animate the transition
        self.animation = QPropertyAnimation(self.right_param_frame, b"maximumWidth")  # Animate minimumWidht
        self.animation.setDuration(300)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animation.start()

        self.setAutoFillBackground(False)  # 禁用自动填充背景


    # def paintEvent(self, e):
    #     painter = QPainter(self)
    #     painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
    #
    #     # 设置背景颜色为半透明
    #     color = QColor(255, 255, 255, 50)  # 半透明白色
    #     painter.fillRect(self.rect(), color)
    #
    #     # 调用父类的 paintEvent 以确保其他绘制操作被执行
    #     super().paintEvent(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WidgetDetect('123')
    w.show()
    app.exec()
