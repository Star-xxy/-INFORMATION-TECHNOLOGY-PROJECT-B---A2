# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'post_detail.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, PrimaryPushButton, PushButton, TextEdit)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(930, 808)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Frame)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(400, 300))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.BodyLabel = BodyLabel(Frame)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.BodyLabel, 0, Qt.AlignmentFlag.AlignBottom)

        self.widget = QWidget(Frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 20))
        self.widget.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.widget)

        self.TextEdit = TextEdit(Frame)
        self.TextEdit.setObjectName(u"TextEdit")
        self.TextEdit.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.TextEdit, 0, Qt.AlignmentFlag.AlignBottom)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.PrimaryPushButton = PrimaryPushButton(Frame)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")
        self.PrimaryPushButton.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.PrimaryPushButton)

        self.PushButton = PushButton(Frame)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.PushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.BodyLabel.setText(QCoreApplication.translate("Frame", u"content", None))
        self.TextEdit.setHtml(QCoreApplication.translate("Frame", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI','Microsoft YaHei','PingFang SC'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Post a comment...</p></body></html>", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Frame", u"Submit a comment", None))
        self.PushButton.setText(QCoreApplication.translate("Frame", u"Return", None))
    # retranslateUi

