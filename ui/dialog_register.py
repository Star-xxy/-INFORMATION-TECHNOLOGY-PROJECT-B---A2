# register.py
import sys
from PySide6.QtCore import Signal  # 添加 Signal 支持
from PySide6.QtWidgets import QApplication, QDialog
from qfluentwidgets import MessageBox
from ui.register import Ui_Dialog as UI_info
from utils.database import Database


class WidgetRegister(QDialog, UI_info):
    # 定义一个信号，表示注册成功
    register_success = Signal()

    def __init__(self, name: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(name)
        self.setupUi(self)
        self.db = Database()

        # Connect buttons
        self.PrimaryPushButton.clicked.connect(self.register)
        self.PushButton.clicked.connect(self.close)

    def show_dialog(self, message):
        w = MessageBox(
            title="提示",
            content=message,
            parent=self
        )
        w.exec()

    def register(self):
        username = self.LineEdit.text()
        mail = self.LineEdit_2.text()
        password = self.PasswordLineEdit.text()
        confirm_password = self.PasswordLineEdit_2.text()
        age = self.LineEdit_4.text()
        weight = self.LineEdit_3.text()

        # Validate input
        is_valid, message = self.db.validate_input(
            username, password, mail, age, weight, confirm_password
        )

        if not is_valid:
            self.show_dialog(message)
            return

        # Try to register user
        if self.db.register_user(username, password, mail, age, weight):
            self.show_dialog("注册成功！")
            self.register_success.emit()  # 发出注册成功的信号
            self.accept()  # 关闭对话框并返回成功状态
        else:
            self.show_dialog("注册失败！用户名或邮箱已被使用！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WidgetRegister('register')
    w.show()
    app.exec()