# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, LineEdit, PasswordLineEdit, PrimaryPushButton,
    PushButton, TitleLabel)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(463, 522)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(60, -1, 60, 30)
        self.TitleLabel = TitleLabel(Dialog)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setMaximumSize(QSize(16777215, 100))
        self.TitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.TitleLabel)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(15)
        self.BodyLabel = BodyLabel(Dialog)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.BodyLabel)

        self.LineEdit = LineEdit(Dialog)
        self.LineEdit.setObjectName(u"LineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.LineEdit)

        self.BodyLabel_2 = BodyLabel(Dialog)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.BodyLabel_2)

        self.LineEdit_2 = LineEdit(Dialog)
        self.LineEdit_2.setObjectName(u"LineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.LineEdit_2)

        self.BodyLabel_3 = BodyLabel(Dialog)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.BodyLabel_3)

        self.PasswordLineEdit = PasswordLineEdit(Dialog)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.PasswordLineEdit)

        self.BodyLabel_4 = BodyLabel(Dialog)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.BodyLabel_4)

        self.PasswordLineEdit_2 = PasswordLineEdit(Dialog)
        self.PasswordLineEdit_2.setObjectName(u"PasswordLineEdit_2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.PasswordLineEdit_2)

        self.BodyLabel_5 = BodyLabel(Dialog)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.BodyLabel_5)

        self.BodyLabel_6 = BodyLabel(Dialog)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.BodyLabel_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LineEdit_3 = LineEdit(Dialog)
        self.LineEdit_3.setObjectName(u"LineEdit_3")

        self.horizontalLayout_2.addWidget(self.LineEdit_3)

        self.BodyLabel_7 = BodyLabel(Dialog)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")

        self.horizontalLayout_2.addWidget(self.BodyLabel_7)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.LineEdit_4 = LineEdit(Dialog)
        self.LineEdit_4.setObjectName(u"LineEdit_4")

        self.horizontalLayout_3.addWidget(self.LineEdit_4)

        self.BodyLabel_8 = BodyLabel(Dialog)
        self.BodyLabel_8.setObjectName(u"BodyLabel_8")

        self.horizontalLayout_3.addWidget(self.BodyLabel_8)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.PrimaryPushButton = PrimaryPushButton(Dialog)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")
        self.PrimaryPushButton.setMinimumSize(QSize(0, 60))

        self.horizontalLayout.addWidget(self.PrimaryPushButton)

        self.PushButton = PushButton(Dialog)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setMinimumSize(QSize(0, 60))

        self.horizontalLayout.addWidget(self.PushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.TitleLabel.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.BodyLabel.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Dialog", u"Mail", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Dialog", u"Confirm Password", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Dialog", u"Age", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Dialog", u"Weight", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Dialog", u" kg    ", None))
        self.BodyLabel_8.setText(QCoreApplication.translate("Dialog", u" years", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.PushButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

