# coding:utf-8
import os
import sys
import time

from PySide6.QtCore import Qt, QUrl, QObject, QEvent, QSize
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QApplication, QStackedWidget, QHBoxLayout, QFileDialog

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox,
                            isDarkTheme, setThemeColor, SplashScreen, setTheme, Theme, MSFluentWindow, FluentStyleSheet,
                            NavigationAvatarWidget)
from qframelesswindow import FramelessWindow, StandardTitleBar

from config.config import AUTHOR, FEEDBACK_URL, VERSION
from ui.widget_analyze import WidgetAnalyze
from ui.widget_user import WidgetUser
from ui.widget_post_all import WidgetPostAll
from ui.widget_class import WidgetClass

from resource import resource_rc

# def isWin11():
#     return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000

# if isWin11():
#     from qframelesswindow import AcrylicWindow as FramelessWindow
# else:
#     from qframelesswindow import FramelessWindow


class Window(MSFluentWindow):
    source = '0'

    def __init__(self):
        super().__init__()
        self.setMicaEffectEnabled(False)
        # create sub interface
        self.analyzeInterface = WidgetAnalyze('home', self)
        self.userInterface = WidgetUser('detect', self)
        self.postsInterface = WidgetPostAll('posts', self)
        self.classesInterface = WidgetClass('classes', self)
        # self.__init_layout()
        self.__init__navigation()
        self.__init__window()


    # def __init__layout(self):
    #     self.hBoxLayout.setSpacing(0)
    #     self.hBoxLayout.setContentsMargins(0, self.titleBar.height(), 0, 0)
    #     self.hBoxLayout.addWidget(self.navigationInterface)
    #     self.hBoxLayout.addWidget(self.stackWidget)
    #     self.hBoxLayout.setStretchFactor(self.stackWidget, 1)
    def __init__navigation(self):
        # enable acrylic effect

        self.addSubInterface(self.analyzeInterface, QIcon(':/yolo/images/icons/home.png'), 'Home',)
        self.addSubInterface(self.userInterface, QIcon(':/yolo/images/icons/vision.png'), 'User',)
        self.addSubInterface(self.postsInterface, QIcon(':/yolo/images/icons/model.png'), 'Social',)
        self.addSubInterface(self.classesInterface, QIcon(':/yolo/images/icons/classify.png'), 'Class',)

    def __init__window(self):

        self.resize(1400, 800)
        self.setWindowIcon(QIcon(':/yolo/images/icons/yolo.png'))
        self.setWindowTitle('YOLO')
        self.titleBar.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        # self.setQss()


    def get_image(self):
        ...

    def get_video(self):
        ...

    def get_webcam(self):
        ...

    def showMessageBox(self):
        w = MessageBox(
            '支持作者🥰',
            f'项目版本 {VERSION}，本项目开发作者 {AUTHOR}',
            self
        )
        w.yesButton.setText('打开主页')
        w.cancelButton.setText('下次一定')

        if w.exec():
            QDesktopServices.openUrl(QUrl(FEEDBACK_URL))
        # self.navigationInterface.panel.collapse()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
