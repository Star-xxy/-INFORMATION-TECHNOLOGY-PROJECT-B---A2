import time

from PySide6.QtCore import Signal, QThread


# 多线程
class Worker(QThread):
    # 登录成功
    login_success = Signal()
    # 登录失败
    login_failed = Signal(str)
    # 操作成功
    do_something_success = Signal(object)
    # 操作失败
    do_something_failed = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        # 需要执行的操作
        self.action = None
        # 操作的参数
        self.action_args = None

    # 设置操作和参数
    def set_action(self, action, action_args):
        self.action = action
        self.action_args = action_args

    def run(self):
        # 操作对应的字典函数
        action_dict = {
            'login': self.login,
            'do_something': self.do_something,
        }
        # 执行操作，如果操作不存在则抛出异常
        try:
            action_dict[self.action](self.action_args)
        except KeyError:
            raise Exception('不存在的操作')

    def login(self, args):
        try:
            # todo 登录代码
            print("登录参数：", args)
            time.sleep(1)
            self.login_success.emit()
        except Exception as e:
            self.login_failed.emit('登录失败，请检查用户信息！')

    def do_something(self, args):
        try:
            # todo 实际操作代码
            print("参数：", args)
            time.sleep(3)
            self.do_something_success.emit({'result': '操作成功'})
        except Exception as e:
            self.do_something_failed.emit('操作失败，请检查网络！')
