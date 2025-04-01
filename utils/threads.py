# threads.py
import time
from PySide6.QtCore import Signal, QThread
from utils.database import Database


class Worker(QThread):
    login_success = Signal(dict)
    login_failed = Signal(str)
    do_something_success = Signal(object)
    do_something_failed = Signal(str)

    # 使用类变量共享单一数据库实例
    _db = None
    _db_ref_count = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.action = None
        self.action_args = None

        # 初始化共享数据库实例
        if Worker._db is None:
            Worker._db = Database()
        Worker._db_ref_count += 1

    def set_action(self, action, action_args):
        self.action = action
        self.action_args = action_args

    def run(self):
        action_dict = {
            'login': self.login,
            'do_something': self.do_something,
        }
        try:
            action_dict[self.action](self.action_args)
        except KeyError:
            raise Exception('不存在的操作')

    def login(self, args):
        try:
            username = args['username'].strip()
            password = args['password'].strip()

            user_data = Worker._db.check_login(username, password)

            if user_data:
                user_info = {
                    'username': user_data[0],
                    'password': user_data[1],
                    'mail': user_data[2],
                    'age': user_data[3],
                    'weight': user_data[4],
                    'training_days': user_data[5],
                    'training_time': user_data[6],
                    'level': user_data[7],
                    'points': user_data[8],
                }
                time.sleep(1)  # 模拟网络延迟
                self.login_success.emit(user_info)
            else:
                self.login_failed.emit('用户名或密码错误！')

        except Exception as e:
            self.login_failed.emit(f'登录失败：{str(e)}')

    def do_something(self, args):
        try:
            time.sleep(3)
            self.do_something_success.emit({'result': '操作成功'})
        except Exception as e:
            self.do_something_failed.emit('操作失败，请检查网络！')

    def __del__(self):
        Worker._db_ref_count -= 1
        if Worker._db_ref_count == 0 and Worker._db is not None:
            Worker._db.close()
            Worker._db = None