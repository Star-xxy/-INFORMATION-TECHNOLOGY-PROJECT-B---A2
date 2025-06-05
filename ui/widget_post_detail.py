# coding:utf-8
import sys

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QUrl, QRectF, QPropertyAnimation, QEasingCurve, QTimer, QTime
from PySide6.QtGui import QIcon, QPainter, QBrush, QColor, QDesktopServices, QPixmap, QPainterPath, \
    QLinearGradient
from PySide6.QtWidgets import QApplication, QStackedWidget, QHBoxLayout, QWidget, QFileDialog, QFrame, QVBoxLayout, \
    QLabel, QScrollArea

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox,
                            isDarkTheme, setThemeColor)
from qfluentwidgets.multimedia import VideoWidget

from ui.post_detail import Ui_Frame
from utils.database import *


class CommentWidget(QWidget):
    def __init__(self, comment, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()

        comment_text = comment['content']
        commenter_username = comment['commenter_username']
        comment_time = comment['comment_time']

        self.comment_label = QLabel(f"{commenter_username} ({comment_time}):\n{comment_text}")
        self.comment_label.setWordWrap(True)
        self.comment_label.setStyleSheet("""
            QLabel {
                padding: 5px;
                color: #333333;
                border: 0px;
            }
        """)

        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setStyleSheet("""
            QFrame {
                border: 1px solid #e0e0e0;
                border-radius: 5px;
                background-color: #f9f9f9;
                margin: 2px;
            }
        """)
        self.frame.setLayout(QVBoxLayout())
        self.frame.layout().addWidget(self.comment_label)

        layout.addWidget(self.frame)
        self.setLayout(layout)


class WidgetPostDetail(QFrame, Ui_Frame):
    def __init__(self, user_name, db, card_id, text, video_path, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.user_name = user_name
        self.db = db
        self.card_id = card_id

        # 设置视频播放器
        layout = QVBoxLayout()
        self.video_widget = VideoWidget(self)
        video_url = QUrl.fromLocalFile(video_path) if video_path else QUrl()
        self.video_widget.setVideo(video_url)
        self.video_widget.setMinimumHeight(300)
        layout.addWidget(self.video_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        self.frame.setLayout(layout)

        self.BodyLabel.setText(text)
        self.BodyLabel.setWordWrap(True)
        self.BodyLabel.setAlignment(Qt.AlignTop)

        # 可滚动评论区域
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; }")

        self.comments_widget = QWidget()
        self.comment_list = QVBoxLayout()
        self.comment_list.setAlignment(Qt.AlignTop)
        self.comments_widget.setLayout(self.comment_list)

        self.scroll_area.setWidget(self.comments_widget)
        self.verticalLayout.replaceWidget(self.widget, self.scroll_area)
        self.widget.deleteLater()

        self.load_comments()

        self.PrimaryPushButton.clicked.connect(self.submit_comment)
        self.PushButton.clicked.connect(self.close)


    def load_comments(self):
        """加载评论到滚动区域"""
        # 安全地清除现有评论
        while self.comment_list.count():
            item = self.comment_list.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        comments = self.db.get_comments(self.card_id)
        for comment in comments:
            comment_widget = CommentWidget(comment)
            self.comment_list.addWidget(comment_widget)

        self.comment_list.addStretch()
        QTimer.singleShot(100, lambda: self.scroll_area.verticalScrollBar().setValue(0))

    def submit_comment(self):
        """提交新评论"""
        comment = self.TextEdit.toPlainText().strip()
        if comment:
            try:
                print(self.card_id, self.user_name, comment)
                self.db.add_comment(self.card_id, self.user_name, comment)
                self.TextEdit.clear()
                self.load_comments()
            except Exception as e:
                print(f"Error submitting comment: {e}")
                MessageBox("Error", "Failed to submit comment!", self).exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setThemeColor('#0078d4')

    db = Database()
    posts = db.get_posts()
    if posts:
        test_post = posts[0]
        w = WidgetPostDetail(
            user_name='test_user',
            db=db,
            card_id=test_post['id'],
            text=test_post['content'],
            video_path=test_post['video_url']
        )
        w.show()
        app.exec()
    else:
        print("No posts found in database!")