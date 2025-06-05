# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'course_card.ui'
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

from qfluentwidgets import (BodyLabel, CardWidget, ImageLabel, PushButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 198)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ImageLabel = ImageLabel(Form)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setMinimumSize(QSize(180, 180))
        self.ImageLabel.setMaximumSize(QSize(180, 180))

        self.horizontalLayout_3.addWidget(self.ImageLabel)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BodyLabel = BodyLabel(self.frame)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setProperty(u"pixelFontSize", 18)

        self.horizontalLayout_2.addWidget(self.BodyLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.BodyLabel_2 = BodyLabel(self.frame)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.verticalLayout.addWidget(self.BodyLabel_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.PushButton_2 = PushButton(self.frame)
        self.PushButton_2.setObjectName(u"PushButton_2")

        self.horizontalLayout.addWidget(self.PushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"Course1", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"Yoga Class 1", None))
        self.PushButton_2.setText(QCoreApplication.translate("Form", u"Watch", None))
    # retranslateUi

