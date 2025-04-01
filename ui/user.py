# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (AvatarWidget, BodyLabel, CalendarPicker, CaptionLabel,
    ComboBox, ImageLabel, PrimaryPushButton, PushButton,
    ScrollArea)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1145, 1275)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea = ScrollArea(Frame)
        self.ScrollArea.setObjectName(u"ScrollArea")
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1143, 1273))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 250))
        self.frame.setMaximumSize(QSize(16777215, 250))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(80)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(80, 20, -1, 20)
        self.AvatarWidget = AvatarWidget(self.frame)
        self.AvatarWidget.setObjectName(u"AvatarWidget")

        self.horizontalLayout.addWidget(self.AvatarWidget)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(20)
        self.BodyLabel = BodyLabel(self.frame)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.BodyLabel)

        self.BodyLabel_2 = BodyLabel(self.frame)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.BodyLabel_2)

        self.BodyLabel_5 = BodyLabel(self.frame)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.BodyLabel_5)

        self.BodyLabel_6 = BodyLabel(self.frame)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.BodyLabel_6)

        self.BodyLabel_9 = BodyLabel(self.frame)
        self.BodyLabel_9.setObjectName(u"BodyLabel_9")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.BodyLabel_9)

        self.BodyLabel_10 = BodyLabel(self.frame)
        self.BodyLabel_10.setObjectName(u"BodyLabel_10")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.BodyLabel_10)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)


        self.horizontalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(20)
        self.formLayout_2.setVerticalSpacing(20)
        self.BodyLabel_3 = BodyLabel(self.frame)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.BodyLabel_3)

        self.BodyLabel_4 = BodyLabel(self.frame)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.BodyLabel_4)

        self.BodyLabel_7 = BodyLabel(self.frame)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.BodyLabel_7)

        self.BodyLabel_8 = BodyLabel(self.frame)
        self.BodyLabel_8.setObjectName(u"BodyLabel_8")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.BodyLabel_8)

        self.BodyLabel_11 = BodyLabel(self.frame)
        self.BodyLabel_11.setObjectName(u"BodyLabel_11")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.BodyLabel_11)

        self.BodyLabel_12 = BodyLabel(self.frame)
        self.BodyLabel_12.setObjectName(u"BodyLabel_12")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.BodyLabel_12)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)


        self.horizontalLayout.addLayout(self.formLayout_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(218, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.PrimaryPushButton = PrimaryPushButton(self.frame)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")
        self.PrimaryPushButton.setMinimumSize(QSize(150, 40))

        self.horizontalLayout_3.addWidget(self.PrimaryPushButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.CaptionLabel_12 = CaptionLabel(self.frame_2)
        self.CaptionLabel_12.setObjectName(u"CaptionLabel_12")
        self.CaptionLabel_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CaptionLabel_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.CaptionLabel_12.setProperty(u"pixelFontSize", 14)

        self.horizontalLayout_4.addWidget(self.CaptionLabel_12)

        self.ComboBox_5 = ComboBox(self.frame_2)
        self.ComboBox_5.setObjectName(u"ComboBox_5")

        self.horizontalLayout_4.addWidget(self.ComboBox_5)

        self.CaptionLabel_11 = CaptionLabel(self.frame_2)
        self.CaptionLabel_11.setObjectName(u"CaptionLabel_11")
        self.CaptionLabel_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.CaptionLabel_11.setProperty(u"pixelFontSize", 14)

        self.horizontalLayout_4.addWidget(self.CaptionLabel_11)

        self.start_date = CalendarPicker(self.frame_2)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setMinimumSize(QSize(0, 0))
        self.start_date.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.start_date)

        self.CaptionLabel_13 = CaptionLabel(self.frame_2)
        self.CaptionLabel_13.setObjectName(u"CaptionLabel_13")
        self.CaptionLabel_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.CaptionLabel_13.setProperty(u"pixelFontSize", 14)

        self.horizontalLayout_4.addWidget(self.CaptionLabel_13)

        self.end_date = CalendarPicker(self.frame_2)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setMinimumSize(QSize(0, 0))
        self.end_date.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.end_date)

        self.ComboBox_4 = ComboBox(self.frame_2)
        self.ComboBox_4.setObjectName(u"ComboBox_4")

        self.horizontalLayout_4.addWidget(self.ComboBox_4)

        self.refresh_button_2 = PrimaryPushButton(self.frame_2)
        self.refresh_button_2.setObjectName(u"refresh_button_2")
        self.refresh_button_2.setMinimumSize(QSize(80, 33))
        self.refresh_button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.refresh_button_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.webEngineView = QWebEngineView(self.frame_2)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setMinimumSize(QSize(0, 720))
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_3.addWidget(self.webEngineView)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(40, -1, 40, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.PushButton = PushButton(self.frame_4)
        self.PushButton.setObjectName(u"PushButton")

        self.horizontalLayout_5.addWidget(self.PushButton)

        self.PushButton_2 = PushButton(self.frame_4)
        self.PushButton_2.setObjectName(u"PushButton_2")

        self.horizontalLayout_5.addWidget(self.PushButton_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.BodyLabel_13 = BodyLabel(self.frame_4)
        self.BodyLabel_13.setObjectName(u"BodyLabel_13")
        self.BodyLabel_13.setMinimumSize(QSize(0, 100))
        self.BodyLabel_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.BodyLabel_13.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.BodyLabel_13)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.ScrollArea)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.BodyLabel.setText(QCoreApplication.translate("Frame", u"Username", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Frame", u"11111", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Frame", u"Weight", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Frame", u"11111", None))
        self.BodyLabel_9.setText(QCoreApplication.translate("Frame", u"Training time", None))
        self.BodyLabel_10.setText(QCoreApplication.translate("Frame", u"11111", None))
        self.label.setText("")
        self.BodyLabel_3.setText(QCoreApplication.translate("Frame", u"Age", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Frame", u"11111", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Frame", u"Training days", None))
        self.BodyLabel_8.setText(QCoreApplication.translate("Frame", u"11111", None))
        self.BodyLabel_11.setText(QCoreApplication.translate("Frame", u"Exercise preference", None))
        self.BodyLabel_12.setText(QCoreApplication.translate("Frame", u"111111", None))
        self.label_2.setText("")
        self.PrimaryPushButton.setText(QCoreApplication.translate("Frame", u"Edit profile", None))
        self.CaptionLabel_12.setText(QCoreApplication.translate("Frame", u"Chart type:", None))
        self.CaptionLabel_11.setText(QCoreApplication.translate("Frame", u"Start date:", None))
        self.CaptionLabel_13.setText(QCoreApplication.translate("Frame", u"End date:", None))
        self.refresh_button_2.setText(QCoreApplication.translate("Frame", u"Refresh", None))
        self.PushButton.setText(QCoreApplication.translate("Frame", u"Weekly report", None))
        self.PushButton_2.setText(QCoreApplication.translate("Frame", u"Monthly report", None))
        self.BodyLabel_13.setText("")
    # retranslateUi

