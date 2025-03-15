# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detect.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QTableWidgetItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, ComboBox, CompactDoubleSpinBox, CompactSpinBox,
    IconWidget, LineEdit, PrimaryPushButton, PushButton,
    Slider, SubtitleLabel, SwitchButton, TableWidget,
    TitleLabel)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1073, 840)
        self.gridLayout_2 = QGridLayout(Frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(21, 9, 9, 21)
        self.frame = QFrame(Frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.Panel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, 0)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.horizontalLayout_24 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.TitleLabel = TitleLabel(self.frame_7)
        self.TitleLabel.setObjectName(u"TitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy1)
        self.TitleLabel.setMaximumSize(QSize(16777215, 32))
        self.TitleLabel.setProperty(u"lightColor", QColor(0, 0, 0, 220))

        self.horizontalLayout_24.addWidget(self.TitleLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_5)

        self.param_button = QPushButton(self.frame_7)
        self.param_button.setObjectName(u"param_button")
        self.param_button.setMinimumSize(QSize(48, 48))
        self.param_button.setMaximumSize(QSize(48, 48))
        self.param_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.param_button.setStyleSheet(u"QPushButton{\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/qfluentwidgets/images/icons/Menu_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.param_button.setIcon(icon)
        self.param_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_24.addWidget(self.param_button)


        self.verticalLayout_7.addWidget(self.frame_7, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.splitter_2 = QSplitter(self.frame)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.frame_2 = QFrame(self.splitter_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(300, 500))
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.frame_2)
        self.splitter.setObjectName(u"splitter")
        sizePolicy2.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy2)
        self.splitter.setFrameShape(QFrame.Shape.StyledPanel)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(6)
        self.pre_video = QLabel(self.splitter)
        self.pre_video.setObjectName(u"pre_video")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pre_video.sizePolicy().hasHeightForWidth())
        self.pre_video.setSizePolicy(sizePolicy3)
        self.pre_video.setMinimumSize(QSize(50, 0))
        self.pre_video.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.pre_video)
        self.res_video = QLabel(self.splitter)
        self.res_video.setObjectName(u"res_video")
        sizePolicy3.setHeightForWidth(self.res_video.sizePolicy().hasHeightForWidth())
        self.res_video.setSizePolicy(sizePolicy3)
        self.res_video.setMinimumSize(QSize(50, 0))
        self.res_video.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.res_video)

        self.verticalLayout_6.addWidget(self.splitter)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.run_button = QPushButton(self.frame_4)
        self.run_button.setObjectName(u"run_button")
        sizePolicy.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy)
        self.run_button.setMinimumSize(QSize(32, 32))
        self.run_button.setMaximumSize(QSize(40, 40))
        self.run_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.run_button.setStyleSheet(u"QPushButton{\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"	border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/yolo/images/icons/circled-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/yolo/images/icons/pause-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.run_button.setIcon(icon1)
        self.run_button.setIconSize(QSize(32, 32))
        self.run_button.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.run_button)

        self.progress_bar = QProgressBar(self.frame_4)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMinimumSize(QSize(0, 20))
        self.progress_bar.setMaximumSize(QSize(16777215, 20))
        self.progress_bar.setStyleSheet(u"QProgressBar{ \n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(0, 159, 170); \n"
"text-align:center; \n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background: rgba(0, 159, 170, 150);\n"
"border-radius: 7px;\n"
"}")
        self.progress_bar.setMaximum(1000)
        self.progress_bar.setValue(600)

        self.horizontalLayout_12.addWidget(self.progress_bar)

        self.stop_button = QPushButton(self.frame_4)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(32, 32))
        self.stop_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stop_button.setStyleSheet(u"QPushButton{\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"	border: none;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/yolo/images/icons/stop-circled.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_button.setIcon(icon2)
        self.stop_button.setIconSize(QSize(32, 32))
        self.stop_button.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.stop_button)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.splitter_2.addWidget(self.frame_2)
        self.frame_6 = QFrame(self.splitter_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.TableWidget = TableWidget(self.frame_6)
        if (self.TableWidget.columnCount() < 5):
            self.TableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.TableWidget.setObjectName(u"TableWidget")
        self.TableWidget.setMinimumSize(QSize(0, 0))
        self.TableWidget.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_5.addWidget(self.TableWidget, 0, Qt.AlignmentFlag.AlignBottom)

        self.splitter_2.addWidget(self.frame_6)

        self.verticalLayout_8.addWidget(self.splitter_2)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.right_param_frame = QFrame(Frame)
        self.right_param_frame.setObjectName(u"right_param_frame")
        self.right_param_frame.setMinimumSize(QSize(320, 0))
        self.right_param_frame.setMaximumSize(QSize(0, 16777215))
        self.right_param_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.right_param_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right_param_frame)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 31, 12, 12)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, -1, -1, 6)
        self.SubtitleLabel_7 = SubtitleLabel(self.right_param_frame)
        self.SubtitleLabel_7.setObjectName(u"SubtitleLabel_7")
        self.SubtitleLabel_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.SubtitleLabel_7.setProperty(u"pixelFontSize", 20)

        self.horizontalLayout_10.addWidget(self.SubtitleLabel_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.CardWidget_5 = CardWidget(self.right_param_frame)
        self.CardWidget_5.setObjectName(u"CardWidget_5")
        self.CardWidget_5.setMinimumSize(QSize(0, 80))
        self.horizontalLayout_9 = QHBoxLayout(self.CardWidget_5)
        self.horizontalLayout_9.setSpacing(30)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(30, -1, -1, 9)
        self.IconWidget_6 = IconWidget(self.CardWidget_5)
        self.IconWidget_6.setObjectName(u"IconWidget_6")
        self.IconWidget_6.setMinimumSize(QSize(32, 32))
        self.IconWidget_6.setMaximumSize(QSize(32, 32))
        icon3 = QIcon()
        icon3.addFile(u":/yolo/images/icons/model.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.IconWidget_6.setProperty(u"icon", icon3)

        self.horizontalLayout_9.addWidget(self.IconWidget_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, -1, -1, -1)
        self.SubtitleLabel_6 = SubtitleLabel(self.CardWidget_5)
        self.SubtitleLabel_6.setObjectName(u"SubtitleLabel_6")
        self.SubtitleLabel_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.SubtitleLabel_6.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_7.addWidget(self.SubtitleLabel_6)

        self.model_box = ComboBox(self.CardWidget_5)
        self.model_box.setObjectName(u"model_box")
        self.model_box.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_7.addWidget(self.model_box)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)


        self.verticalLayout_4.addWidget(self.CardWidget_5)

        self.CardWidget = CardWidget(self.right_param_frame)
        self.CardWidget.setObjectName(u"CardWidget")
        self.CardWidget.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.CardWidget)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, 9, -1, 0)
        self.IconWidget = IconWidget(self.CardWidget)
        self.IconWidget.setObjectName(u"IconWidget")
        self.IconWidget.setMinimumSize(QSize(32, 32))
        self.IconWidget.setMaximumSize(QSize(32, 32))
        icon4 = QIcon()
        icon4.addFile(u":/yolo/images/icons/iou.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.IconWidget.setProperty(u"icon", icon4)

        self.horizontalLayout_2.addWidget(self.IconWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 15)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, -1, 5)
        self.SubtitleLabel = SubtitleLabel(self.CardWidget)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setMinimumSize(QSize(0, 22))
        self.SubtitleLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.SubtitleLabel.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout.addWidget(self.SubtitleLabel)

        self.iou_spinbox = CompactDoubleSpinBox(self.CardWidget)
        self.iou_spinbox.setObjectName(u"iou_spinbox")
        self.iou_spinbox.setMinimumSize(QSize(90, 33))
        self.iou_spinbox.setMaximum(1.000000000000000)
        self.iou_spinbox.setSingleStep(0.010000000000000)

        self.horizontalLayout.addWidget(self.iou_spinbox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.iou_slider = Slider(self.CardWidget)
        self.iou_slider.setObjectName(u"iou_slider")
        self.iou_slider.setMinimumSize(QSize(100, 22))
        self.iou_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.iou_slider)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(self.right_param_frame)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.CardWidget_2.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_3 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(30, -1, -1, 0)
        self.IconWidget_3 = IconWidget(self.CardWidget_2)
        self.IconWidget_3.setObjectName(u"IconWidget_3")
        self.IconWidget_3.setMinimumSize(QSize(32, 32))
        self.IconWidget_3.setMaximumSize(QSize(32, 32))
        icon5 = QIcon()
        icon5.addFile(u":/yolo/images/icons/conf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.IconWidget_3.setProperty(u"icon", icon5)

        self.horizontalLayout_3.addWidget(self.IconWidget_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 15)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, -1, 5)
        self.SubtitleLabel_3 = SubtitleLabel(self.CardWidget_2)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        self.SubtitleLabel_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.SubtitleLabel_3.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_4.addWidget(self.SubtitleLabel_3)

        self.conf_spinbox = CompactDoubleSpinBox(self.CardWidget_2)
        self.conf_spinbox.setObjectName(u"conf_spinbox")
        self.conf_spinbox.setMinimumSize(QSize(90, 33))
        self.conf_spinbox.setMaximum(1.000000000000000)
        self.conf_spinbox.setSingleStep(0.010000000000000)

        self.horizontalLayout_4.addWidget(self.conf_spinbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.conf_slider = Slider(self.CardWidget_2)
        self.conf_slider.setObjectName(u"conf_slider")
        self.conf_slider.setMinimumSize(QSize(100, 22))
        self.conf_slider.setMaximum(100)
        self.conf_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.conf_slider)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addWidget(self.CardWidget_2)

        self.CardWidget_3 = CardWidget(self.right_param_frame)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        self.CardWidget_3.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_5 = QHBoxLayout(self.CardWidget_3)
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(30, -1, -1, 0)
        self.IconWidget_4 = IconWidget(self.CardWidget_3)
        self.IconWidget_4.setObjectName(u"IconWidget_4")
        self.IconWidget_4.setMinimumSize(QSize(32, 32))
        self.IconWidget_4.setMaximumSize(QSize(32, 32))
        icon6 = QIcon()
        icon6.addFile(u":/yolo/images/icons/delay.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.IconWidget_4.setProperty(u"icon", icon6)

        self.horizontalLayout_5.addWidget(self.IconWidget_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 15)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, -1, 5)
        self.SubtitleLabel_4 = SubtitleLabel(self.CardWidget_3)
        self.SubtitleLabel_4.setObjectName(u"SubtitleLabel_4")
        self.SubtitleLabel_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.SubtitleLabel_4.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_6.addWidget(self.SubtitleLabel_4)

        self.speed_spinbox = CompactSpinBox(self.CardWidget_3)
        self.speed_spinbox.setObjectName(u"speed_spinbox")
        self.speed_spinbox.setMaximum(50)
        self.speed_spinbox.setDisplayIntegerBase(10)

        self.horizontalLayout_6.addWidget(self.speed_spinbox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.speed_slider = Slider(self.CardWidget_3)
        self.speed_slider.setObjectName(u"speed_slider")
        self.speed_slider.setMinimumSize(QSize(100, 22))
        self.speed_slider.setMaximum(50)
        self.speed_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.speed_slider)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.CardWidget_3)

        self.CardWidget_4 = CardWidget(self.right_param_frame)
        self.CardWidget_4.setObjectName(u"CardWidget_4")
        self.CardWidget_4.setMinimumSize(QSize(0, 150))
        self.horizontalLayout_11 = QHBoxLayout(self.CardWidget_4)
        self.horizontalLayout_11.setSpacing(30)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(30, 10, -1, 10)
        self.IconWidget_5 = IconWidget(self.CardWidget_4)
        self.IconWidget_5.setObjectName(u"IconWidget_5")
        self.IconWidget_5.setMinimumSize(QSize(32, 32))
        self.IconWidget_5.setMaximumSize(QSize(32, 32))
        icon7 = QIcon()
        icon7.addFile(u":/yolo/images/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.IconWidget_5.setProperty(u"icon", icon7)

        self.horizontalLayout_11.addWidget(self.IconWidget_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.choose_folder_button = PrimaryPushButton(self.CardWidget_4)
        self.choose_folder_button.setObjectName(u"choose_folder_button")
        self.choose_folder_button.setMinimumSize(QSize(100, 39))
        self.choose_folder_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.choose_folder_button, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.LineEdit = LineEdit(self.CardWidget_4)
        self.LineEdit.setObjectName(u"LineEdit")
        self.LineEdit.setMinimumSize(QSize(150, 33))

        self.gridLayout.addWidget(self.LineEdit, 1, 0, 1, 2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, -1, 5)
        self.SubtitleLabel_5 = SubtitleLabel(self.CardWidget_4)
        self.SubtitleLabel_5.setObjectName(u"SubtitleLabel_5")
        self.SubtitleLabel_5.setMinimumSize(QSize(80, 0))
        self.SubtitleLabel_5.setMaximumSize(QSize(80, 16777215))
        self.SubtitleLabel_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.SubtitleLabel_5.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_8.addWidget(self.SubtitleLabel_5)

        self.save_button = SwitchButton(self.CardWidget_4)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_8.addWidget(self.save_button)


        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 2)


        self.horizontalLayout_11.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.CardWidget_4)

        self.verticalSpacer = QSpacerItem(20, 136, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.right_param_frame, 0, 1, 2, 1)

        self.status_bar = QLabel(Frame)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setStyleSheet(u"QLabel{\n"
"	font: 700 11pt \"Segoe UI\";\n"
"	color: rgba(0, 0, 0, 140);\n"
"}")

        self.gridLayout_2.addWidget(self.status_bar, 1, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.TitleLabel.setText(QCoreApplication.translate("Frame", u"YOLO\u76ee\u6807\u68c0\u6d4b", None))
        self.param_button.setText("")
        self.pre_video.setText("")
        self.res_video.setText("")
        self.run_button.setText("")
        self.stop_button.setText("")
        ___qtablewidgetitem = self.TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Frame", u"\u6587\u4ef6\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Frame", u"\u68c0\u6d4b\u7c7b\u578b", None));
        ___qtablewidgetitem2 = self.TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Frame", u"\u5bf9\u8c61\u540d\u79f0", None));
        ___qtablewidgetitem3 = self.TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Frame", u"\u7f6e\u4fe1\u5ea6", None));
        ___qtablewidgetitem4 = self.TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Frame", u"\u8fb9\u754c\u6846", None));
        self.SubtitleLabel_7.setText(QCoreApplication.translate("Frame", u"\u8bbe\u7f6e", None))
        self.SubtitleLabel_6.setText(QCoreApplication.translate("Frame", u"\u6a21\u578b", None))
        self.model_box.setText(QCoreApplication.translate("Frame", u"yolov8n", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Frame", u"\u4ea4\u5e76\u6bd4", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Frame", u"\u7f6e\u4fe1\u5ea6", None))
        self.SubtitleLabel_4.setText(QCoreApplication.translate("Frame", u"\u65f6\u5ef6(ms)", None))
        self.choose_folder_button.setText(QCoreApplication.translate("Frame", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.SubtitleLabel_5.setText(QCoreApplication.translate("Frame", u"\u4fdd\u5b58", None))
        self.save_button.setProperty(u"text", QCoreApplication.translate("Frame", u"\u5173", None))
        self.save_button.setProperty(u"onText", QCoreApplication.translate("Frame", u"\u5f00", None))
        self.save_button.setProperty(u"offText", QCoreApplication.translate("Frame", u"\u5173", None))
        self.status_bar.setText(QCoreApplication.translate("Frame", u"Welcome!", None))
    # retranslateUi

