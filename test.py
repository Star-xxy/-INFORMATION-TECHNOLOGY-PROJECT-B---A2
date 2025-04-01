from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, \
    QFileDialog, QHBoxLayout, QTextEdit, QFrame, QLineEdit, QInputDialog
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QMediaPlayer

from qfluentwidgets.multimedia import VideoWidget
import sqlite3
import sys
import cv2  # OpenCV to capture the first frame of the video


class CardWidget(QWidget):
    def __init__(self, card_id, image_path, text, likes, favorites, parent=None):
        super().__init__(parent)
        self.card_id = card_id
        self.likes = likes
        self.favorites = favorites
        layout = QHBoxLayout()

        # 显示图片
        self.image_label = QLabel()
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(100, 100))

        # 显示文字
        self.text_label = QLabel(text)
        self.text_label.setWordWrap(True)

        # 显示点赞和收藏
        self.like_button = QPushButton(f"点赞 ({self.likes})")
        self.favorite_button = QPushButton(f"收藏 ({self.favorites})")
        self.like_button.clicked.connect(self.like_card)
        self.favorite_button.clicked.connect(self.favorite_card)

        layout.addWidget(self.image_label)
        layout.addWidget(self.text_label)
        layout.addWidget(self.like_button)
        layout.addWidget(self.favorite_button)
        self.setLayout(layout)

    def like_card(self):
        self.likes += 1
        self.like_button.setText(f"点赞 ({self.likes})")
        self.update_interaction_in_db()

    def favorite_card(self):
        self.favorites += 1
        self.favorite_button.setText(f"收藏 ({self.favorites})")
        self.update_interaction_in_db()

    def update_interaction_in_db(self):
        conn = sqlite3.connect('cards.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE cards SET likes = ?, favorites = ? WHERE id = ?',
                       (self.likes, self.favorites, self.card_id))
        conn.commit()
        conn.close()


# 数据库管理类
class DatabaseManager:
    def __init__(self, db_name="cards.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cards (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    image_path TEXT,
                                    text TEXT,
                                    video_path TEXT,
                                    likes INTEGER DEFAULT 0,
                                    favorites INTEGER DEFAULT 0)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS comments (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    card_id INTEGER,
                                    comment TEXT,
                                    FOREIGN KEY (card_id) REFERENCES cards(id) ON DELETE CASCADE)''')
        self.conn.commit()

    def add_card(self, image_path, text, video_path):
        self.cursor.execute("INSERT INTO cards (image_path, text, video_path) VALUES (?, ?, ?)",
                            (image_path, text, video_path))
        self.conn.commit()

    def get_cards(self):
        self.cursor.execute("SELECT id, image_path, text, video_path, likes, favorites FROM cards")
        return self.cursor.fetchall()

    def delete_card(self, card_id):
        self.cursor.execute("DELETE FROM cards WHERE id = ?", (card_id,))
        self.conn.commit()

    def add_comment(self, card_id, comment):
        self.cursor.execute("INSERT INTO comments (card_id, comment) VALUES (?, ?)", (card_id, comment))
        self.conn.commit()

    def get_comments(self, card_id):
        self.cursor.execute("SELECT comment FROM comments WHERE card_id = ?", (card_id,))
        return [row[0] for row in self.cursor.fetchall()]


class CommentWidget(QWidget):
    def __init__(self, comment_text, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()

        # 评论框
        self.comment_label = QLabel(comment_text)
        self.comment_label.setWordWrap(True)

        # 边框
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLayout(QVBoxLayout())
        self.frame.layout().addWidget(self.comment_label)

        layout.addWidget(self.frame)
        self.setLayout(layout)


class DetailWindow(QWidget):
    def __init__(self, db_manager, card_id, image_path, text, video_path, parent=None):
        super().__init__(parent)
        self.db_manager = db_manager
        self.card_id = card_id
        self.setWindowTitle("卡片详情")
        self.resize(500, 500)

        layout = QVBoxLayout()

        # 文字显示
        self.text_label = QLabel(text)
        self.text_label.setWordWrap(True)

        # 视频播放
        self.video_widget = VideoWidget(self)
        self.video_widget.setVideo(QUrl(video_path))

        # 评论区
        self.comment_box = QTextEdit()
        self.comment_box.setFixedHeight(100)
        self.comment_box.setPlaceholderText("发表评论...")

        # 发表按钮
        self.submit_button = QPushButton("提交评论")
        self.submit_button.clicked.connect(self.submit_comment)

        # 评论列表
        self.comment_list = QVBoxLayout()
        self.comment_container = QWidget()
        self.comment_container.setLayout(self.comment_list)
        self.load_comments()

        # 返回按钮
        self.back_button = QPushButton("返回")
        self.back_button.clicked.connect(self.close)

        layout.addWidget(self.video_widget)
        layout.addWidget(self.text_label)
        layout.addWidget(self.comment_container)
        layout.addWidget(self.comment_box)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.back_button)

        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def load_comments(self):
        for i in reversed(range(self.comment_list.count())):
            self.comment_list.itemAt(i).widget().deleteLater()

        comments = self.db_manager.get_comments(self.card_id)
        for comment in comments:
            self.comment_list.addWidget(CommentWidget(comment))

    def submit_comment(self):
        comment = self.comment_box.toPlainText()
        if comment:
            self.db_manager.add_comment(self.card_id, comment)
            self.comment_box.clear()
            self.load_comments()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("卡片管理界面")
        self.resize(400, 500)
        self.db_manager = DatabaseManager()

        # 主布局
        self.layout = QVBoxLayout()

        # 显示区域
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.show_details)
        self.layout.addWidget(self.list_widget)

        # 按钮区域
        self.add_button = QPushButton("添加卡片")
        self.remove_button = QPushButton("删除选中卡片")

        self.add_button.clicked.connect(self.add_card)
        self.remove_button.clicked.connect(self.remove_card)

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.remove_button)

        self.setLayout(self.layout)
        self.load_cards()

    def load_cards(self):
        self.list_widget.clear()
        for card_id, image_path, text, video_path, likes, favorites in self.db_manager.get_cards():
            card = CardWidget(card_id, image_path, text, likes, favorites)
            item = QListWidgetItem()
            item.setSizeHint(card.sizeHint())
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, card)
            item.setData(1, (card_id, image_path, text, video_path))

    def add_card(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "选择图片", "", "Images (*.png *.jpg *.jpeg)")
        video_path, _ = file_dialog.getOpenFileName(self, "选择视频", "", "Videos (*.mp4 *.avi *.mov)")

        if image_path and video_path:
            text, ok = QInputDialog.getText(self, "输入卡片文字", "请输入卡片的文字描述:")
            if ok and text:
                self.db_manager.add_card(image_path, text, video_path)
                self.load_cards()

    def remove_card(self):
        selected_items = self.list_widget.selectedItems()
        for item in selected_items:
            card_id = item.data(1)[0]
            self.db_manager.delete_card(card_id)
            self.load_cards()

    def show_details(self, item):
        card_id, image_path, text, video_path = item.data(1)
        self.detail_window = DetailWindow(self.db_manager, card_id, image_path, text, video_path)
        self.detail_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
