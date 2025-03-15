# coding:utf-8
import os
import sys
import time

from PySide6.QtCore import Qt, QUrl, QObject, QEvent, QSize
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QApplication, QStackedWidget, QHBoxLayout, QFileDialog

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox,
                            isDarkTheme, setThemeColor, SplashScreen, setTheme, Theme, FluentWindow, FluentStyleSheet,
                            NavigationAvatarWidget)
from qframelesswindow import FramelessWindow, StandardTitleBar

from config.config import AUTHOR, FEEDBACK_URL, VERSION
from ui.widget_home import WidgetHome
# from ui.home_widget import WidgetHome
from ui.widget_detect import WidgetDetect
from ui.widget_data_table import WidgetTable
from ui.widget_chart import WidgetChart
from resource import resource_rc

# def isWin11():
#     return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000

# if isWin11():
#     from qframelesswindow import AcrylicWindow as FramelessWindow
# else:
#     from qframelesswindow import FramelessWindow


class Window(FluentWindow):
    source = '0'

    def __init__(self):
        super().__init__()
        # self.setTitleBar(StandardTitleBar(self))
        # if isWin11():
        #     self.windowEffect.setMicaEffect(self.winId(), isDarkTheme())
        self.setMicaEffectEnabled(False)
        # # use dark theme mode
        # setTheme(Theme.DARK)
        #
        # # change the theme color
        # setThemeColor('#0078d4')

        # self.hBoxLayout = QHBoxLayout(self)
        # self.navigationInterface = NavigationInterface(self, showMenuButton=True)
        # self.stackWidget = QStackedWidget(self)

        # create sub interface
        self.homeInterface = WidgetHome('home', self)
        self.detectInterface = WidgetDetect('detect', self)
        self.tableInterface = WidgetTable('table', 'database/database.db', self)
        self.chartInterface = WidgetChart('chart', self)
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
        self.navigationInterface.setAcrylicEnabled(True)

        self.addSubInterface(self.homeInterface, QIcon(':/yolo/images/icons/home.png'), '主页',
                             NavigationItemPosition.SCROLL)
        self.addSubInterface(self.detectInterface, QIcon(':/yolo/images/icons/vision.png'), '检测',
                             NavigationItemPosition.SCROLL)
        self.addSubInterface(self.tableInterface, QIcon(':/yolo/images/icons/table.png'), '数据显示',
                             NavigationItemPosition.SCROLL)
        self.addSubInterface(self.chartInterface, QIcon(':/yolo/images/icons/chart.png'), '图表',
                             NavigationItemPosition.SCROLL)

        self.navigationInterface.addSeparator(NavigationItemPosition.SCROLL)

        # self.navigationInterface.addItem(
        #     routeKey='folder',
        #     icon=QIcon(':/yolo/images/icons/folder.png'),
        #     text='批量图片（选择文件夹）',
        #     onClick=self.get_folder,
        #     selectable=False,
        #     position=NavigationItemPosition.SCROLL
        # )

        self.navigationInterface.addItem(
            routeKey='image',
            icon=QIcon(':/yolo/images/icons/image.png'),
            text='选择单张图片',
            onClick=self.get_image,
            selectable=False,
            position=NavigationItemPosition.SCROLL
        )

        self.navigationInterface.addItem(
            routeKey='video',
            icon=QIcon(':/yolo/images/icons/video.png'),
            text='选择视频',
            onClick=self.get_video,
            selectable=False,
            position=NavigationItemPosition.SCROLL
        )

        self.navigationInterface.addItem(
            routeKey='camera',
            icon=QIcon(':/yolo/images/icons/camera.png'),
            text='选择摄像头',
            onClick=self.get_webcam,
            selectable=False,
            position=NavigationItemPosition.SCROLL
        )

        # self.navigationInterface.addItem(
        #     routeKey='rtsp',
        #     icon=QIcon(':/yolo/images/icons/private-wall-mount-camera.png'),
        #     text='流媒体服务器',
        #     onClick=self.get_rtsp,
        #     selectable=False,
        #     position=NavigationItemPosition.SCROLL
        # )

        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('Zhongmning', 'resource/images/icons/logo.png'),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )

        # self.navigationInterface.addSeparator(NavigationItemPosition.SCROLL)
        # self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        # self.navigationInterface.setCurrentItem('home')

    def __init__window(self):

        self.resize(1200, 800)
        self.setWindowIcon(QIcon(':/yolo/images/icons/yolo.png'))
        self.setWindowTitle('YOLO')
        self.titleBar.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        # self.setQss()


    # def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP, parent=None):
    #     """ add sub interface """
    #     self.stackWidget.addWidget(interface)
    #     self.navigationInterface.addItem(
    #         routeKey=interface.objectName(),
    #         icon=icon,
    #         text=text,
    #         onClick=lambda: self.switchTo(interface),
    #         position=position,
    #         tooltip=text,
    #         parentRouteKey=parent.objectName() if parent else None
    #     )

    # def setQss(self):
    #     color = 'dark' if isDarkTheme() else 'light'
    #     with open(f'resource/qss/{color}/windows.qss', encoding='utf-8') as f:
    #         print(f.read())
    #         self.setStyleSheet(f.read())

    # def switchTo(self, widget):
    #     self.stackWidget.setCurrentWidget(widget)

    # def onCurrentInterfaceChanged(self, index):
    #     widget = self.stackWidget.widget(index)
    #     self.navigationInterface.setCurrentItem(widget.objectName())

    # def get_folder(self):
    #     folder_path = QFileDialog.getExistingDirectory(self, '选择资料夹', os.getcwd())
    #     print(folder_path)

    def get_image(self):
        ...

    def get_video(self):
        ...

    def get_webcam(self):
        ...

    def get_rtsp(self):
        ...

    def showMessageBox(self):
        w = MessageBox(
            '支持作者🥰',
            f'项目版本 {VERSION}，本项目开发作者 {AUTHOR}，需要更多自定义项目开发，毕业设计，请加微信 zzm17864296700',
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
