import darkdetect
from PySide6.QtCore import QFile, Qt
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QGuiApplication
from qfluentwidgets import Theme, Dialog, InfoBarPosition, InfoBar, StateToolTip
import base64

from Crypto.Cipher import AES

def set_window_center(window):
    """ set window center """
    qr = window.frameGeometry()
    cp = window.screen().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


def show_dialog(parent, content, title='提示', callback=None):
    w = Dialog(title, content, parent)
    # 获取当前屏幕高度
    screen = QGuiApplication.primaryScreen().geometry()
    height = screen.height()
    if parent:
        height = parent.screen().availableGeometry().height()
    w.contentLabel.setMaximumHeight(height * 0.5)
    w.windowTitleLabel.hide()
    if not callback:
        w.yesButton.hide()
        w.cancelButton.setText('确定')
        w.buttonLayout.insertWidget(0, QLabel(''))
        w.buttonLayout.setStretch(0, 1)
        w.buttonLayout.setStretch(1, 1)
    if w.exec():
        if callback:
            callback()


def show_toast(parent, title, content, position=InfoBarPosition.TOP_RIGHT, duration=1500):
    InfoBar.info(
        title=title,
        content=content,
        orient=Qt.Orientation.Horizontal,
        isClosable=True,
        position=position,
        duration=duration,
        parent=parent
    )


# 显示加载中
def show_loading(parent, content='请稍后...', title='加载中'):
    parent.stateTooltip = StateToolTip(title, content, parent)
    parent.stateTooltip.setTitle(title)
    parent.stateTooltip.setContent(content)
    parent.stateTooltip.show()
    move_loading(parent)


# 隐藏加载中
def hide_loading(parent, content='请查看结果框', title='操作完成'):
    if parent.stateTooltip:
        parent.stateTooltip.setTitle(title)
        parent.stateTooltip.setContent(content)
        parent.stateTooltip.setState(True)
        parent.stateTooltip = None


# 把加载中的窗口移动到窗口右下角
def move_loading(parent):
    if parent.stateTooltip:
        tl_x, tl_y, width, height = parent.window().frameGeometry().getRect()
        width2 = parent.stateTooltip.width()
        height2 = parent.stateTooltip.height()
        parent.stateTooltip.move(width - width2 - 30, height - height2 - 30)



def pkcs7padding(plaintext, block_size=16):
    text_length = len(plaintext)
    bytes_length = len(plaintext.encode('utf-8'))
    len_plaintext = text_length if (bytes_length == text_length) else bytes_length
    return plaintext + chr(block_size - len_plaintext % block_size) * (block_size - len_plaintext % block_size)


def aes_encrypt(content, key='j2EmvU6yHw8LzKxN', iv='yA3tGqWbVr9nLcPz'):
    padded_data = pkcs7padding(content)
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
    encrypt_bytes = cipher.encrypt(padded_data.encode('utf-8'))  # 加密
    return str(base64.b64encode(encrypt_bytes), encoding='utf-8')  # 重新编码


def aes_decrypt(content, key='j2EmvU6yHw8LzKxN', iv='yA3tGqWbVr9nLcPz'):
    if content == '':
        return ''
    try:
        cipher = AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
        decrypt_bytes = base64.b64decode(content)
        msg = cipher.decrypt(decrypt_bytes)
        return msg[0:-ord(msg[-1:])].decode('utf-8')
    except Exception as e:
        print('aes解密失败 ' + str(e))
        return ''
