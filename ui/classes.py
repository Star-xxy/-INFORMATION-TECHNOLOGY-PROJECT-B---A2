# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'classes.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (AvatarWidget, BodyLabel, ImageLabel, PrimaryPushButton,
    PushButton, TitleLabel)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1113, 750)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1099, 960))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 250))
        self.frame_4.setMaximumSize(QSize(16777215, 250))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(80)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(80, 20, -1, 20)
        self.AvatarWidget_2 = AvatarWidget(self.frame_4)
        self.AvatarWidget_2.setObjectName(u"AvatarWidget_2")

        self.horizontalLayout_2.addWidget(self.AvatarWidget_2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(20)
        self.formLayout_2.setVerticalSpacing(20)
        self.BodyLabel_7 = BodyLabel(self.frame_4)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.BodyLabel_7)

        self.BodyLabel_8 = BodyLabel(self.frame_4)
        self.BodyLabel_8.setObjectName(u"BodyLabel_8")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.BodyLabel_8)

        self.BodyLabel_9 = BodyLabel(self.frame_4)
        self.BodyLabel_9.setObjectName(u"BodyLabel_9")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.BodyLabel_9)

        self.BodyLabel_10 = BodyLabel(self.frame_4)
        self.BodyLabel_10.setObjectName(u"BodyLabel_10")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.BodyLabel_10)

        self.BodyLabel_11 = BodyLabel(self.frame_4)
        self.BodyLabel_11.setObjectName(u"BodyLabel_11")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.BodyLabel_11)

        self.BodyLabel_12 = BodyLabel(self.frame_4)
        self.BodyLabel_12.setObjectName(u"BodyLabel_12")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.BodyLabel_12)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)


        self.horizontalLayout_2.addLayout(self.formLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(218, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.PrimaryPushButton = PrimaryPushButton(self.frame_4)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")
        self.PrimaryPushButton.setMinimumSize(QSize(150, 40))

        self.horizontalLayout_3.addWidget(self.PrimaryPushButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TitleLabel = TitleLabel(self.frame_2)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.listWidget = QListWidget(self.frame_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 300))

        self.verticalLayout_2.addWidget(self.listWidget)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.TitleLabel_2 = TitleLabel(self.frame_3)
        self.TitleLabel_2.setObjectName(u"TitleLabel_2")

        self.verticalLayout_3.addWidget(self.TitleLabel_2)

        self.listWidget_2 = QListWidget(self.frame_3)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setMinimumSize(QSize(0, 300))

        self.verticalLayout_3.addWidget(self.listWidget_2)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Frame", u"Username", None))
        self.BodyLabel_8.setText(QCoreApplication.translate("Frame", u"123", None))
        self.BodyLabel_9.setText(QCoreApplication.translate("Frame", u"Member Points", None))
        self.BodyLabel_10.setText(QCoreApplication.translate("Frame", u"300", None))
        self.BodyLabel_11.setText(QCoreApplication.translate("Frame", u"Number of courses", None))
        self.BodyLabel_12.setText(QCoreApplication.translate("Frame", u"3", None))
        self.label.setText("")
        self.PrimaryPushButton.setText(QCoreApplication.translate("Frame", u"Recharge Points", None))
        self.TitleLabel.setText(QCoreApplication.translate("Frame", u"My Courses", None))
        self.TitleLabel_2.setText(QCoreApplication.translate("Frame", u"Buy Yoga Classes", None))
    # retranslateUi

