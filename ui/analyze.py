# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analyze.ui'
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
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QVBoxLayout, QWidget)

from qfluentwidgets import (AvatarWidget, BodyLabel, CaptionLabel, CardWidget,
    ElevatedCardWidget, ImageLabel, LargeTitleLabel, PrimaryPushButton,
    PrimaryToolButton, PushButton, ScrollArea, SimpleCardWidget,
    StrongBodyLabel, SubtitleLabel, ToolButton)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1169, 1412)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea = ScrollArea(Frame)
        self.ScrollArea.setObjectName(u"ScrollArea")
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1167, 1513))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(40, -1, -1, -1)
        self.LargeTitleLabel = LargeTitleLabel(self.frame)
        self.LargeTitleLabel.setObjectName(u"LargeTitleLabel")

        self.horizontalLayout_7.addWidget(self.LargeTitleLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(30)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(30, -1, -1, -1)
        self.start_training_btn = PrimaryPushButton(self.frame_6)
        self.start_training_btn.setObjectName(u"start_training_btn")
        self.start_training_btn.setMinimumSize(QSize(0, 64))

        self.horizontalLayout_8.addWidget(self.start_training_btn)

        self.end_training_btn = PushButton(self.frame_6)
        self.end_training_btn.setObjectName(u"end_training_btn")
        self.end_training_btn.setMinimumSize(QSize(0, 64))

        self.horizontalLayout_8.addWidget(self.end_training_btn)

        self.BodyLabel_2 = BodyLabel(self.frame_6)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        self.BodyLabel_2.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_8.addWidget(self.BodyLabel_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addWidget(self.frame_6)


        self.horizontalLayout_11.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_8 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.ElevatedCardWidget = ElevatedCardWidget(self.frame)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        self.ElevatedCardWidget.setMinimumSize(QSize(400, 220))
        self.ElevatedCardWidget.setMaximumSize(QSize(400, 220))
        self.verticalLayout_5 = QVBoxLayout(self.ElevatedCardWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.ElevatedCardWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(40, 20, 20, 9)
        self.AvatarWidget = AvatarWidget(self.frame_3)
        self.AvatarWidget.setObjectName(u"AvatarWidget")

        self.horizontalLayout_6.addWidget(self.AvatarWidget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(17, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.StrongBodyLabel = StrongBodyLabel(self.frame_3)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setProperty(u"pixelFontSize", 22)

        self.verticalLayout_3.addWidget(self.StrongBodyLabel)

        self.CaptionLabel = CaptionLabel(self.frame_3)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setProperty(u"pixelFontSize", 14)

        self.verticalLayout_3.addWidget(self.CaptionLabel)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(17, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.ElevatedCardWidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_5.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(40, 10, 60, 40)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BodyLabel_3 = BodyLabel(self.frame_5)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        self.BodyLabel_3.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_2.addWidget(self.BodyLabel_3)

        self.BodyLabel_7 = BodyLabel(self.frame_5)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")
        self.BodyLabel_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.BodyLabel_7.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_2.addWidget(self.BodyLabel_7)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BodyLabel_6 = BodyLabel(self.frame_5)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")
        self.BodyLabel_6.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_4.addWidget(self.BodyLabel_6)

        self.BodyLabel_10 = BodyLabel(self.frame_5)
        self.BodyLabel_10.setObjectName(u"BodyLabel_10")
        self.BodyLabel_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.BodyLabel_10.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_4.addWidget(self.BodyLabel_10)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BodyLabel_4 = BodyLabel(self.frame_5)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")
        self.BodyLabel_4.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_3.addWidget(self.BodyLabel_4)

        self.BodyLabel_8 = BodyLabel(self.frame_5)
        self.BodyLabel_8.setObjectName(u"BodyLabel_8")
        self.BodyLabel_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.BodyLabel_8.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_3.addWidget(self.BodyLabel_8)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.BodyLabel_5 = BodyLabel(self.frame_5)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")
        self.BodyLabel_5.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_5.addWidget(self.BodyLabel_5)

        self.BodyLabel_9 = BodyLabel(self.frame_5)
        self.BodyLabel_9.setObjectName(u"BodyLabel_9")
        self.BodyLabel_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.BodyLabel_9.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_5.addWidget(self.BodyLabel_9)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_5)


        self.horizontalLayout_11.addWidget(self.ElevatedCardWidget)

        self.horizontalSpacer_9 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)


        self.verticalLayout_12.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(40, -1, 40, -1)
        self.splitter = QSplitter(self.frame_2)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QFrame.Shape.StyledPanel)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(6)
        self.pre_video = QLabel(self.splitter)
        self.pre_video.setObjectName(u"pre_video")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pre_video.sizePolicy().hasHeightForWidth())
        self.pre_video.setSizePolicy(sizePolicy1)
        self.pre_video.setMinimumSize(QSize(50, 550))
        self.pre_video.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.pre_video)
        self.res_video = QLabel(self.splitter)
        self.res_video.setObjectName(u"res_video")
        sizePolicy1.setHeightForWidth(self.res_video.sizePolicy().hasHeightForWidth())
        self.res_video.setSizePolicy(sizePolicy1)
        self.res_video.setMinimumSize(QSize(50, 0))
        self.res_video.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.res_video)

        self.verticalLayout_2.addWidget(self.splitter)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy3)
        self.run_button.setMinimumSize(QSize(32, 32))
        self.run_button.setMaximumSize(QSize(40, 40))
        self.run_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.run_button.setStyleSheet(u"QPushButton{\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/yolo/images/icons/circled-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/yolo/images/icons/pause-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.run_button.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u":/yolo/images/icons/stop-circled.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_button.setIcon(icon1)
        self.stop_button.setIconSize(QSize(32, 32))
        self.stop_button.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.stop_button)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(208, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ToolButton = ToolButton(self.frame_2)
        self.ToolButton.setObjectName(u"ToolButton")
        self.ToolButton.setMinimumSize(QSize(64, 64))
        self.ToolButton.setMaximumSize(QSize(64, 64))
        self.ToolButton.setIconSize(QSize(24, 24))
        self.ToolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.ToolButton)

        self.ToolButton_2 = ToolButton(self.frame_2)
        self.ToolButton_2.setObjectName(u"ToolButton_2")
        self.ToolButton_2.setMinimumSize(QSize(64, 64))
        self.ToolButton_2.setMaximumSize(QSize(64, 64))
        self.ToolButton_2.setIconSize(QSize(24, 24))
        self.ToolButton_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.ToolButton_2)

        self.ToolButton_3 = ToolButton(self.frame_2)
        self.ToolButton_3.setObjectName(u"ToolButton_3")
        self.ToolButton_3.setMinimumSize(QSize(72, 64))
        self.ToolButton_3.setMaximumSize(QSize(72, 64))
        self.ToolButton_3.setIconSize(QSize(24, 24))
        self.ToolButton_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.ToolButton_3)

        self.PrimaryToolButton = PrimaryToolButton(self.frame_2)
        self.PrimaryToolButton.setObjectName(u"PrimaryToolButton")
        self.PrimaryToolButton.setMinimumSize(QSize(64, 64))
        self.PrimaryToolButton.setMaximumSize(QSize(64, 64))

        self.horizontalLayout.addWidget(self.PrimaryToolButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_12.addWidget(self.frame_2)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(40, 20, 40, 20)
        self.SubtitleLabel = SubtitleLabel(self.frame_8)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setAutoFillBackground(False)
        self.SubtitleLabel.setProperty(u"strikeOut", False)

        self.verticalLayout_10.addWidget(self.SubtitleLabel)

        self.BodyLabel_12 = BodyLabel(self.frame_8)
        self.BodyLabel_12.setObjectName(u"BodyLabel_12")
        self.BodyLabel_12.setMinimumSize(QSize(0, 50))
        self.BodyLabel_12.setAutoFillBackground(False)
        self.BodyLabel_12.setWordWrap(True)
        self.BodyLabel_12.setProperty(u"pixelFontSize", 16)

        self.verticalLayout_10.addWidget(self.BodyLabel_12)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(40, 20, 40, 20)
        self.SubtitleLabel_2 = SubtitleLabel(self.frame_9)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")

        self.verticalLayout_9.addWidget(self.SubtitleLabel_2)

        self.BodyLabel_13 = BodyLabel(self.frame_9)
        self.BodyLabel_13.setObjectName(u"BodyLabel_13")
        self.BodyLabel_13.setMinimumSize(QSize(0, 50))
        self.BodyLabel_13.setWordWrap(True)
        self.BodyLabel_13.setProperty(u"pixelFontSize", 16)

        self.verticalLayout_9.addWidget(self.BodyLabel_13)


        self.verticalLayout_11.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(40, 20, 40, 20)
        self.SubtitleLabel_3 = SubtitleLabel(self.frame_10)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")

        self.verticalLayout_7.addWidget(self.SubtitleLabel_3)

        self.BodyLabel_14 = BodyLabel(self.frame_10)
        self.BodyLabel_14.setObjectName(u"BodyLabel_14")
        self.BodyLabel_14.setMinimumSize(QSize(0, 50))
        self.BodyLabel_14.setWordWrap(True)
        self.BodyLabel_14.setProperty(u"pixelFontSize", 16)

        self.verticalLayout_7.addWidget(self.BodyLabel_14)


        self.verticalLayout_11.addWidget(self.frame_10)


        self.verticalLayout_12.addWidget(self.frame_7, 0, Qt.AlignmentFlag.AlignTop)

        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.ScrollArea)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Frame", u"Yoga training monitoring system", None))
        self.start_training_btn.setText(QCoreApplication.translate("Frame", u"Start training", None))
        self.end_training_btn.setText(QCoreApplication.translate("Frame", u"End training", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Frame", u"Exercise time: hours minutes seconds", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Frame", u"Username", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Frame", u"Persistence is victory", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Frame", u"Training days  ", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Frame", u"11111", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Frame", u"Training time  ", None))
        self.BodyLabel_10.setText(QCoreApplication.translate("Frame", u"11111", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Frame", u"Level  ", None))
        self.BodyLabel_8.setText(QCoreApplication.translate("Frame", u"11111", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Frame", u"Points  ", None))
        self.BodyLabel_9.setText(QCoreApplication.translate("Frame", u"11111", None))
        self.pre_video.setText("")
        self.res_video.setText("")
        self.run_button.setText("")
        self.stop_button.setText("")
        self.ToolButton.setText(QCoreApplication.translate("Frame", u"Image", None))
        self.ToolButton_2.setText(QCoreApplication.translate("Frame", u"Video", None))
        self.ToolButton_3.setText(QCoreApplication.translate("Frame", u"Camera", None))
        self.PrimaryToolButton.setText(QCoreApplication.translate("Frame", "Detect", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Frame", u"Correct posture", None))
        self.BodyLabel_12.setText(QCoreApplication.translate("Frame", u"The Anjaneyasana (Low Lunge Pose) requires the front leg to be bent with the knee above the ankle, the back leg to be extended straight with the back knee close to the ground, the hips facing forward, the spine in a neutral position, the hands can be placed on the ground or raised overhead, and the chest opened.", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Frame", u"User's posture", None))
        self.BodyLabel_13.setText(QCoreApplication.translate("Frame", u"The user is performing an advanced variation of Anjaneyasana with arms extended upwards. The front leg is bent at a good angle, with the knee roughly above the ankle, and the back leg is straight with the back knee close to the ground and the top of the foot flat, meeting the pose's requirements. The hips appear to be fairly aligned, and the body overall presents a smooth line, demonstrating good balance and strength. The back is slightly arched, and the chest is open, but there may be some overextension in the spine, and the shoulders seem slightly tense. The head is tilted upward, which could potentially cause discomfort in the neck.", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Frame", u"Adjustment suggestions", None))
        self.BodyLabel_14.setText(QCoreApplication.translate("Frame", u"Relax the shoulders, avoid shrugging, and allow the shoulder blades to naturally sink down.\n"
"Slightly adjust the back to maintain a neutral spine, avoiding excessive arching to protect the lower back.\n"
"Lower the head, gaze forward, and alleviate tension in the neck.\n"
"\n"
"", None))
    # retranslateUi

