# coding:utf-8
import sys

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QUrl, QRectF, QPropertyAnimation, QEasingCurve, QTimer, QTime
from PySide6.QtGui import QIcon, QPainter, QBrush, QColor, QDesktopServices, QPixmap, QPainterPath, \
    QLinearGradient
from PySide6.QtWidgets import QApplication, QStackedWidget, QHBoxLayout, QWidget, QFileDialog, QFrame

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox,
                            isDarkTheme, setThemeColor)

from ui.analyze import Ui_Frame as UI_detect
from utils.style_sheet import StyleSheet


class WidgetAnalyze(QFrame, UI_detect):

    def __init__(self, name: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(name)
        self.setupUi(self)


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.elapsed_time = QTime(0, 0, 0)
        self.start_training_btn.clicked.connect(self.start_training)
        self.end_training_btn.clicked.connect(self.end_training)

    def start_training(self):
        self.timer.start(1000)  # 每秒更新
        self.start_training_btn.setEnabled(False)
        self.elapsed_time = QTime(0, 0, 0)
        self.update_time()

    def update_time(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        hours = f"{self.elapsed_time.hour():02}"
        minutes = f"{self.elapsed_time.minute():02}"
        seconds = f"{self.elapsed_time.second():02}"

        text = (f"Exercise time: <span style='color:red; font-size:20px; font-weight:bold;'> {hours} </span> hours "
                f"<span style='color:red; font-size:20px; font-weight:bold;'> {minutes} </span> minutes "
                f"<span style='color:red; font-size:20px; font-weight:bold;'> {seconds} </span> seconds")
        self.BodyLabel_2.setText(text)

    def end_training(self):
        if self.timer.isActive():
            self.timer.stop()
            text = (f"You have exercised for  <span style='color:red; font-size:20px; font-weight:bold;'> {self.elapsed_time.hour()} </span> hours "
                    f"<span style='color:red; font-size:20px; font-weight:bold;'> {self.elapsed_time.minute()} </span> minutes "
                    f"<span style='color:red; font-size:20px; font-weight:bold;'> {self.elapsed_time.second()} </span> seconds")

            self.BodyLabel_2.setText(text)
            self.start_training_btn.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WidgetAnalyze('123')
    w.show()
    app.exec()
