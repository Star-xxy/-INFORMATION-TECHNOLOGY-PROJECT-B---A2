# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chart.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

from qfluentwidgets import (CalendarPicker, CaptionLabel, ComboBox, PrimaryPushButton,
    PushButton)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1035, 691)
        self.verticalLayout_3 = QVBoxLayout(Frame)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(21, -1, 21, 21)
        self.frame = QFrame(Frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.CaptionLabel_9 = CaptionLabel(self.frame)
        self.CaptionLabel_9.setObjectName(u"CaptionLabel_9")
        self.CaptionLabel_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CaptionLabel_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.CaptionLabel_9.setProperty(u"pixelFontSize", 14)

        self.horizontalLayout_3.addWidget(self.CaptionLabel_9)

        self.ComboBox = ComboBox(self.frame)
        self.ComboBox.setObjectName(u"ComboBox")

        self.horizontalLayout_3.addWidget(self.ComboBox)

        self.CaptionLabel_10 = CaptionLabel(self.frame)
        self.CaptionLabel_10.setObjectName(u"CaptionLabel_10")
        self.CaptionLabel_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CaptionLabel_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.CaptionLabel_10.setProperty(u"pixelFontSize", 14)

        self.horizontalLayout_3.addWidget(self.CaptionLabel_10)

        self.ComboBox_2 = ComboBox(self.frame)
        self.ComboBox_2.setObjectName(u"ComboBox_2")

        self.horizontalLayout_3.addWidget(self.ComboBox_2)

        self.CaptionLabel_11 = CaptionLabel(self.frame)
        self.CaptionLabel_11.setObjectName(u"CaptionLabel_11")
        self.CaptionLabel_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.CaptionLabel_11.setProperty(u"pixelFontSize", 14)

        self.horizontalLayout_3.addWidget(self.CaptionLabel_11)

        self.start_date = CalendarPicker(self.frame)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setMinimumSize(QSize(0, 0))
        self.start_date.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.start_date)

        self.CaptionLabel_12 = CaptionLabel(self.frame)
        self.CaptionLabel_12.setObjectName(u"CaptionLabel_12")
        self.CaptionLabel_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.CaptionLabel_12.setProperty(u"pixelFontSize", 14)

        self.horizontalLayout_3.addWidget(self.CaptionLabel_12)

        self.end_date = CalendarPicker(self.frame)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setMinimumSize(QSize(0, 0))
        self.end_date.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.end_date)

        self.ComboBox_3 = ComboBox(self.frame)
        self.ComboBox_3.setObjectName(u"ComboBox_3")

        self.horizontalLayout_3.addWidget(self.ComboBox_3)

        self.refresh_button = PrimaryPushButton(self.frame)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setMinimumSize(QSize(80, 33))
        self.refresh_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.refresh_button)


        self.verticalLayout_3.addWidget(self.frame)

        self.webEngineView = QWebEngineView(Frame)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_3.addWidget(self.webEngineView)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.CaptionLabel_9.setText(QCoreApplication.translate("Frame", u"\u56fe\u8868\u7c7b\u578b\uff1a", None))
        self.CaptionLabel_10.setText(QCoreApplication.translate("Frame", u"\u68c0\u6d4b\u7ed3\u679c\u7c7b\u578b\uff1a", None))
        self.CaptionLabel_11.setText(QCoreApplication.translate("Frame", u"\u5f00\u59cb\u65e5\u671f\uff1a", None))
        self.CaptionLabel_12.setText(QCoreApplication.translate("Frame", u"\u7ed3\u675f\u65e5\u671f\uff1a", None))
        self.refresh_button.setText(QCoreApplication.translate("Frame", u"\u5237\u65b0", None))
    # retranslateUi

