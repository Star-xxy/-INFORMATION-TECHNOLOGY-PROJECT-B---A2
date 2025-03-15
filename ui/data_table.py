# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_table.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLayout, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (CalendarPicker, CaptionLabel, ComboBox, LineEdit,
    PrimaryPushButton, PushButton, SearchLineEdit, TableView)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1032, 800)
        self.verticalLayout_2 = QVBoxLayout(Frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(21, 9, 21, 21)
        self.frame = QFrame(Frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(13)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.search_input = SearchLineEdit(self.frame)
        self.search_input.setObjectName(u"search_input")

        self.horizontalLayout.addWidget(self.search_input)

        self.ComboBox = ComboBox(self.frame)
        self.ComboBox.setObjectName(u"ComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComboBox.sizePolicy().hasHeightForWidth())
        self.ComboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.ComboBox)

        self.CaptionLabel = CaptionLabel(self.frame)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setProperty(u"pixelFontSize", 14)

        self.horizontalLayout.addWidget(self.CaptionLabel)

        self.start_date = CalendarPicker(self.frame)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setMinimumSize(QSize(0, 0))
        self.start_date.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.start_date)

        self.CaptionLabel_2 = CaptionLabel(self.frame)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")
        self.CaptionLabel_2.setProperty(u"pixelFontSize", 14)

        self.horizontalLayout.addWidget(self.CaptionLabel_2)

        self.end_date = CalendarPicker(self.frame)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setMinimumSize(QSize(0, 0))
        self.end_date.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.end_date)

        self.search_button = PrimaryPushButton(self.frame)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(80, 33))
        self.search_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.search_button)

        self.clear_button = PushButton(self.frame)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setMinimumSize(QSize(80, 33))
        self.clear_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.clear_button)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(Frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.table_view = TableView(self.frame_2)
        self.table_view.setObjectName(u"table_view")

        self.verticalLayout.addWidget(self.table_view)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(Frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(189, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer = QSpacerItem(109, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.prev_button = PushButton(self.frame_3)
        self.prev_button.setObjectName(u"prev_button")
        self.prev_button.setMinimumSize(QSize(0, 40))
        self.prev_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.prev_button)

        self.page_label = CaptionLabel(self.frame_3)
        self.page_label.setObjectName(u"page_label")
        self.page_label.setMinimumSize(QSize(60, 0))
        self.page_label.setMaximumSize(QSize(60, 16777215))
        self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_label.setProperty(u"pixelFontSize", 16)

        self.horizontalLayout_3.addWidget(self.page_label)

        self.next_button = PushButton(self.frame_3)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setMinimumSize(QSize(0, 40))
        self.next_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.next_button)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 6)
        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.goto_page_input = LineEdit(self.frame_3)
        self.goto_page_input.setObjectName(u"goto_page_input")
        self.goto_page_input.setMinimumSize(QSize(50, 40))
        self.goto_page_input.setMaximumSize(QSize(50, 33))

        self.horizontalLayout_2.addWidget(self.goto_page_input)

        self.goto_page_button = PushButton(self.frame_3)
        self.goto_page_button.setObjectName(u"goto_page_button")
        self.goto_page_button.setMinimumSize(QSize(60, 40))
        self.goto_page_button.setMaximumSize(QSize(60, 33))
        self.goto_page_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.goto_page_button)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(189, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.ComboBox.setText("")
        self.CaptionLabel.setText(QCoreApplication.translate("Frame", u"\u5f00\u59cb\u65e5\u671f", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Frame", u"\u7ed3\u675f\u65e5\u671f", None))
        self.search_button.setText(QCoreApplication.translate("Frame", u"\u641c\u7d22", None))
        self.clear_button.setText(QCoreApplication.translate("Frame", u"\u8fd8\u539f", None))
        self.prev_button.setText(QCoreApplication.translate("Frame", u"\u4e0a\u4e00\u9875", None))
        self.page_label.setText(QCoreApplication.translate("Frame", u"1/20", None))
        self.next_button.setText(QCoreApplication.translate("Frame", u"\u4e0b\u4e00\u9875", None))
        self.goto_page_button.setText(QCoreApplication.translate("Frame", u"\u8df3\u8f6c", None))
    # retranslateUi

