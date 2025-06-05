# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'post_all.ui'
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
    QListWidget, QListWidgetItem, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, ImageLabel, StrongBodyLabel, TitleLabel)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(993, 645)
        self.verticalLayout_3 = QVBoxLayout(Frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(Frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, -1, 30)
        self.TitleLabel = TitleLabel(self.frame_2)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(60, 40, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.StrongBodyLabel_3 = StrongBodyLabel(self.frame_2)
        self.StrongBodyLabel_3.setObjectName(u"StrongBodyLabel_3")
        self.StrongBodyLabel_3.setProperty(u"pixelFontSize", 20)

        self.gridLayout.addWidget(self.StrongBodyLabel_3, 2, 0, 1, 1)

        self.StrongBodyLabel_6 = StrongBodyLabel(self.frame_2)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")
        self.StrongBodyLabel_6.setProperty(u"pixelFontSize", 20)

        self.gridLayout.addWidget(self.StrongBodyLabel_6, 2, 2, 1, 1)

        self.BodyLabel = BodyLabel(self.frame_2)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.BodyLabel, 0, 3, 1, 1)

        self.StrongBodyLabel_5 = StrongBodyLabel(self.frame_2)
        self.StrongBodyLabel_5.setObjectName(u"StrongBodyLabel_5")
        self.StrongBodyLabel_5.setProperty(u"pixelFontSize", 20)

        self.gridLayout.addWidget(self.StrongBodyLabel_5, 1, 2, 1, 1)

        self.StrongBodyLabel_2 = StrongBodyLabel(self.frame_2)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")
        self.StrongBodyLabel_2.setProperty(u"pixelFontSize", 20)

        self.gridLayout.addWidget(self.StrongBodyLabel_2, 1, 0, 1, 1)

        self.StrongBodyLabel = StrongBodyLabel(self.frame_2)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setMinimumSize(QSize(80, 0))
        self.StrongBodyLabel.setProperty(u"pixelFontSize", 20)

        self.gridLayout.addWidget(self.StrongBodyLabel, 0, 0, 1, 1)

        self.BodyLabel_2 = BodyLabel(self.frame_2)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.gridLayout.addWidget(self.BodyLabel_2, 2, 3, 1, 1)

        self.BodyLabel_3 = BodyLabel(self.frame_2)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.gridLayout.addWidget(self.BodyLabel_3, 1, 3, 1, 1)

        self.StrongBodyLabel_4 = StrongBodyLabel(self.frame_2)
        self.StrongBodyLabel_4.setObjectName(u"StrongBodyLabel_4")
        self.StrongBodyLabel_4.setMinimumSize(QSize(100, 0))
        self.StrongBodyLabel_4.setProperty(u"pixelFontSize", 20)

        self.gridLayout.addWidget(self.StrongBodyLabel_4, 0, 2, 1, 1)

        self.ImageLabel = ImageLabel(self.frame_2)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setMinimumSize(QSize(32, 32))
        self.ImageLabel.setMaximumSize(QSize(32, 32))
        self.ImageLabel.setScaledContents(True)

        self.gridLayout.addWidget(self.ImageLabel, 0, 1, 1, 1)

        self.ImageLabel_2 = ImageLabel(self.frame_2)
        self.ImageLabel_2.setObjectName(u"ImageLabel_2")
        self.ImageLabel_2.setMinimumSize(QSize(32, 32))
        self.ImageLabel_2.setMaximumSize(QSize(32, 32))

        self.gridLayout.addWidget(self.ImageLabel_2, 1, 1, 1, 1)

        self.ImageLabel_3 = ImageLabel(self.frame_2)
        self.ImageLabel_3.setObjectName(u"ImageLabel_3")
        self.ImageLabel_3.setMinimumSize(QSize(32, 32))
        self.ImageLabel_3.setMaximumSize(QSize(32, 32))

        self.gridLayout.addWidget(self.ImageLabel_3, 2, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame = QFrame(Frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.TitleLabel.setText(QCoreApplication.translate("Frame", u"Top three training hours this week:", None))
        self.StrongBodyLabel_3.setText(QCoreApplication.translate("Frame", u"NO.3", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Frame", u"Name", None))
        self.BodyLabel.setText(QCoreApplication.translate("Frame", u"Training duration", None))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("Frame", u"Name", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Frame", u"NO.2 ", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Frame", u"NO.1 ", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Frame", u"Training duration", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Frame", u"Training duration", None))
        self.StrongBodyLabel_4.setText(QCoreApplication.translate("Frame", u"Name", None))
    # retranslateUi

