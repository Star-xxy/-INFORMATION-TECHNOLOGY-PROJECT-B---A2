# coding:utf-8
import sys
from pathlib import Path

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QUrl, QRectF, QEvent, QObject, QSize, QRect, QEasingCurve
from PySide6.QtGui import QIcon, QPainter, QBrush, QColor, QDesktopServices, QPixmap, QPainterPath, \
    QLinearGradient, QCursor
from PySide6.QtWidgets import QApplication, QStackedWidget, QHBoxLayout, QWidget, QFileDialog, \
    QGraphicsDropShadowEffect, QVBoxLayout, QSizePolicy, QGridLayout, QLabel

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox,
                            isDarkTheme, setThemeColor, ElevatedCardWidget, ImageLabel, CaptionLabel, FlowLayout,
                            IconWidget, TitleLabel, BodyLabel, SingleDirectionScrollArea, SmoothScrollArea, ScrollArea)
from resource import resource_rc
from tasks import TASK
from utils.signal_bus import signalBus
from utils.style_sheet import StyleSheet

class TypeCard(ElevatedCardWidget):
    """ Emoji card """

    def __init__(self, icon_path, title, text, task,  parent=None):
        super().__init__(parent)
        self.task = task
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setProperty("borderRadius", 10)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(24, 24, -1, 13)

        self.IconWidget = IconWidget(self)
        self.IconWidget.setObjectName(u"IconWidget")
        self.IconWidget.setMinimumSize(QSize(64, 64))
        self.IconWidget.setMaximumSize(QSize(64, 64))
        icon = QIcon()
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.IconWidget.setProperty("icon", icon)

        self.verticalLayout.addWidget(self.IconWidget)
        self.TitleLabel = TitleLabel(self)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setMaximumSize(QSize(16777215, 40))
        self.TitleLabel.setProperty("pixelFontSize", 20)
        self.TitleLabel.setText(title)

        self.verticalLayout.addWidget(self.TitleLabel)
        self.BodyLabel = BodyLabel(self)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setScaledContents(False)
        self.BodyLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.BodyLabel.setWordWrap(True)
        self.BodyLabel.setProperty("lightColor", QColor(93, 93, 93))
        self.BodyLabel.setProperty("pixelFontSize", 12)
        self.BodyLabel.setText(text)
        self.verticalLayout.addWidget(self.BodyLabel)
        self.setFixedSize(200, 240)


    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        signalBus.switchToSampleCard.emit(self.task)

class SampleCardView(QWidget):
    """ Sample card view """

    def __init__(self, title: str, parent=None):
        super().__init__(parent=parent)
        self.titleLabel = QLabel(title, self)
        self.vBoxLayout = QVBoxLayout(self)
        self.flowLayout = FlowLayout()

        self.vBoxLayout.setContentsMargins(100, 36, 36, 36)
        self.vBoxLayout.setSpacing(36)
        self.flowLayout.setContentsMargins(0, 0, 0, 0)
        self.flowLayout.setHorizontalSpacing(12)
        self.flowLayout.setVerticalSpacing(12)

        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addLayout(self.flowLayout, 1)

        self.titleLabel.setObjectName('viewTitleLabel')

        StyleSheet.TYPE_CARD.apply(self)


    def addSampleCard(self, icon, title, content, task):
        """ add sample card """
        card = TypeCard(icon, title, content, task, self)
        self.flowLayout.addWidget(card)


class WidgetHome(ScrollArea):

    def __init__(self, name: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(name)
        self.cards = ['det_card', 'cls_card', 'track_card', 'seg_card', 'pose_card']
        self.view = QWidget(self)
        self.view.setObjectName("scrollViewContent")
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)
        StyleSheet.WIDGET_HOME.apply(self)

        self.resize(1000, 680)
        self.vBoxLayout = QVBoxLayout(self.view)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        basicInputView = SampleCardView(
            self.tr(""), self.view)
        basicInputView.addSampleCard(
            ':/yolo/images/icons/detection-2.png',
            '目标检测',
            '通过单个前向传播快速识别和定位图像中的多个目标物体，并输出它们的类别和边界框，适用于实时和高效的目标检测应用',
             TASK.detect,
        )
        basicInputView.addSampleCard(
            ':/yolo/images/icons/classify-2.png',
            '图像分类',
            '对输入图像进行分类任务，能够将图像分配到预定义的类别中',
             TASK.classify,
        )
        basicInputView.addSampleCard(
            ':/yolo/images/icons/track.png',
            '目标跟踪',
            '结合了目标检测和跟踪算法，通过连续帧中的目标识别与位置预测，实现对多个目标物体的实时跟踪',
             TASK.track,
        )
        basicInputView.addSampleCard(
            ':/yolo/images/icons/segment-2.png',
            '图像分割',
            '通过像素级分割掩码对图像中的目标物体进行精确分割，能够同时提供物体的边界框和详细的分割区域',
             TASK.segment,
        )
        basicInputView.addSampleCard(
            ':/yolo/images/icons/pose.png',
            '姿态检测',
            '识别和定位图像或视频中人的关键点，如头部、躯干、四肢等，进而推断人体的姿态和运动',
             TASK.pose,
        )

        self.vBoxLayout.addWidget(basicInputView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WidgetHome('123')
    w.show()
    app.exec()
