# dialog_modify.py
# coding:utf-8
import sys

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QUrl, QRectF, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon, QPainter, QBrush, QColor, QDesktopServices, QPixmap, QPainterPath, QLinearGradient
from PySide6.QtWidgets import QApplication, QStackedWidget, QHBoxLayout, QWidget, QFileDialog, QFrame, QDialog, QMessageBox

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox, isDarkTheme, setThemeColor)
from ui.modify import Ui_Dialog as UI_info
from utils.style_sheet import StyleSheet
from utils.database import Database  # 引入数据库操作


class WidgetInfoModify(QDialog, UI_info):
    def __init__(self, name: str, user_info: dict, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(name)
        self.user_info = user_info  # 保存传入的用户信息
        self.updated_info = {}  # 保存修改后的信息
        self.setupUi(self)
        self.db = Database()  # 初始化数据库
        self.init_ui()
        self.init_connections()

    def init_ui(self):
        # 初始化界面时，填充默认值
        self.LineEdit.setText(self.user_info.get('username', ''))
        self.LineEdit_4.setText(self.user_info.get('mail', ''))
        self.LineEdit_2.setText(str(self.user_info.get('age', 0)))
        self.LineEdit_3.setText(str(self.user_info.get('weight', 0)))

    def init_connections(self):
        # 绑定确认和取消按钮的点击事件
        self.PrimaryPushButton.clicked.connect(self.save_and_close)
        self.PushButton.clicked.connect(self.reject)

    def save_and_close(self):
        # 获取用户输入
        username = self.LineEdit.text()
        mail = self.LineEdit_4.text()
        age = self.LineEdit_2.text()
        weight = self.LineEdit_3.text()

        # 使用数据库的校验方法
        is_valid, message = self.db.validate_input(
            username=username,
            password=self.user_info.get('password', ''),  # 假设密码不修改
            mail=mail,
            age=age,
            weight=weight,
            confirm_password=self.user_info.get('password', '')
        )

        if not is_valid:
            QMessageBox.warning(self, "输入错误", message)
            return

        # 更新用户信息到数据库
        try:
            with self.db.lock:
                cursor = self.db.conn.cursor()
                cursor.execute('''
                    UPDATE users 
                    SET username = ?, mail = ?, age = ?, weight = ?
                    WHERE username = ?
                ''', (username, mail, int(age), float(weight), self.user_info.get('username')))
                self.db.conn.commit()
                cursor.close()

            # 更新本地存储的信息
            self.updated_info = {
                'username': username,
                'mail': mail,
                'age': int(age),
                'weight': float(weight),
                'training_days': self.user_info.get('training_days', 0),
                'training_time': self.user_info.get('training_time', 0)
            }
            self.accept()  # 关闭对话框并返回 Accepted
        except Exception as e:
            QMessageBox.critical(self, "保存失败", f"数据库操作失败：{str(e)}")
            self.reject()

    def get_updated_info(self):
        # 返回更新后的信息
        return self.updated_info

if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_info = {'username': 'test', 'mail': 'test@qq.com', 'age': 25, 'weight': 70.0}
    w = WidgetInfoModify('123', user_info)
    w.show()
    app.exec()