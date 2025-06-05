# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'charge.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QWidget)

from qfluentwidgets import (BodyLabel, CaptionLabel, PrimaryPushButton, PushButton)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(399, 340)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(30)
        self.verticalSpacer = QSpacerItem(20, 26, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.BodyLabel = BodyLabel(self.frame)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setProperty(u"pixelFontSize", 22)

        self.gridLayout_2.addWidget(self.BodyLabel, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(32, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 0, 2, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(32, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)

        self.CaptionLabel = CaptionLabel(self.frame)
        self.CaptionLabel.setObjectName(u"CaptionLabel")

        self.gridLayout_2.addWidget(self.CaptionLabel, 3, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.PrimaryPushButton = PrimaryPushButton(self.frame)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")
        self.PrimaryPushButton.setMinimumSize(QSize(80, 40))

        self.horizontalLayout.addWidget(self.PrimaryPushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.PushButton = PushButton(self.frame)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setMinimumSize(QSize(80, 40))

        self.horizontalLayout.addWidget(self.PushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 27, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 5, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.BodyLabel.setText(QCoreApplication.translate("Dialog", u"Enter the recharge amount", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"20", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"points", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Dialog", u"Note: Each RMB can be exchanged for 10 points", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Dialog", u"Charge", None))
        self.PushButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

