# coding:utf-8
import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget

from qfluentwidgets import Dialog, setTheme, Theme, PrimaryPushButton, MessageBox


class CloseDialog(MessageBox):

    def __init__(self, title: str, content: str, parent, time=10000, auto=True, **kwargs):
        super().__init__(title, content, parent=parent)

        QTimer.singleShot(2000, self.close)
        # QTimer.singleShot(time, self.doCountDown)

class Demo(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(950, 500)
        self.btn = PrimaryPushButton('Click Me', parent=self)
        self.btn.move(425, 225)
        self.btn.clicked.connect(self.showDialog)
        self.setStyleSheet('Demo{background:white}')

    def showDialog(self):
        title = 'Are you sure you want to delete the folder?'
        content = """If you delete the "Music" folder from the list, the folder will no longer appear in the list, but will not be deleted."""
        w = CloseDialog(title, content, self)
        if w.exec():
            print('Yes button is pressed')
        else:
            print('Cancel button is pressed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()
