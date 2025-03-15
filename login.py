import sys

from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtWidgets import QApplication
from qfluentwidgets import setThemeColor, SplitTitleBar, isDarkTheme

from utils.threads import Worker
from login.login_utils import show_dialog, hide_loading, show_toast, show_loading
from login.ui.LoginWindow import Ui_Form
from main import MainWindow


def isWin11():
    return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000


if isWin11():
    from qframelesswindow import AcrylicWindow as Window
else:
    from qframelesswindow import FramelessWindow as Window


class LoginWindow(Window, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # setTheme(Theme.DARK)
        self.init_ui()
        self.init_worker()


    def init_ui(self):
        setThemeColor('#28afe9')

        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()

        self.label.setScaledContents(False)
        self.setWindowIcon(QIcon(":login/images/logo.png"))
        self.resize(1000, 650)

        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=isDarkTheme())
        if not isWin11():
            color = QColor(25, 33, 42) if isDarkTheme() else QColor(240, 244, 249)
            self.setStyleSheet(f"LoginWindow{{background: {color.name()}}}")

        if sys.platform == "darwin":
            self.setSystemTitleBarButtonVisible(True)
            self.titleBar.minBtn.hide()
            self.titleBar.maxBtn.hide()
            self.titleBar.closeBtn.hide()

        self.titleBar.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Segoe UI';
                padding: 0 4px;
                color: white
            }
        """)

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)


    def login(self):
        # 模拟登录成功
        username = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        if username == '' or password == '':
            show_dialog(self, '请填写完整的登录信息！')
            return
        show_loading(self, '正在登录...')
        self.worker.set_action('login', {'username': username, 'password': password})
        self.worker.start()


    def init_worker(self):
        self.worker = Worker()
        self.worker.login_success.connect(self.on_login_success)
        self.worker.login_failed.connect(self.on_login_failed)

        self.pushButton.clicked.connect(self.login)
    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap(":/login/images/background.jpg").scaled(
            self.label.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        self.label.setPixmap(pixmap)

    def systemTitleBarRect(self, size):
        """ Returns the system title bar rect, only works for macOS """
        return QRect(size.width() - 75, 0, 75, size.height())

    def on_login_success(self):
        hide_loading(self, '登录成功！')
        show_toast(self, '提示', '登录成功！')
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def on_login_failed(self):
        show_toast(self, '提示', '登录失败！')
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LoginWindow()
    w.show()
    app.exec()