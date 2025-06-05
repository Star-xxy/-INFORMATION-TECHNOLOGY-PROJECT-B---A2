# utils/threads.py
import time
from PySide6.QtCore import Signal, QThread
from utils.database import * # Assuming Database, DB_HOST etc. are here or imported


class Worker(QThread):
    login_success = Signal(dict)
    login_failed = Signal(str)
    admin_login_success = Signal(str) # New signal for admin login
    do_something_success = Signal(object)
    do_something_failed = Signal(str)

    _db = None
    _db_ref_count = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.action = None
        self.action_args = None

        if Worker._db is None:
            Worker._db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)
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
            if self.action in action_dict:
                action_dict[self.action](self.action_args)
            else:
                self.do_something_failed.emit(f'Unknown action: {self.action}')
        except Exception as e:
            self.do_something_failed.emit(f'Error in worker thread for action {self.action}: {str(e)}')


    def login(self, args):
        try:
            username = args['username'].strip()
            password = args['password'].strip()

            # Admin Check
            if username == 'admin' and password == '888888':
                time.sleep(0.5) # Simulate check
                self.admin_login_success.emit(username) # Emit admin success signal
                return # Stop further processing for admin login

            # Existing user login logic
            user_data = Worker._db.check_login(username, password)

            if user_data:
                user_info = {
                    'id': user_data[0],
                    'username': user_data[1],
                    'password': user_data[2],
                    'mail': user_data[3],
                    'age': user_data[4],
                    'weight': user_data[5],
                    'training_days': user_data[6],
                    'training_time': user_data[7],
                    'level': user_data[8],
                    'points': user_data[9],
                }
                time.sleep(1)
                self.login_success.emit(user_info)
            else:
                self.login_failed.emit('Wrong username or password!')

        except Exception as e:
            self.login_failed.emit(f'Login Failed: {str(e)}')

    def do_something(self, args):
        try:
            time.sleep(3)
            self.do_something_success.emit({'result': 'Generic operation successful'})
        except Exception as e:
            self.do_something_failed.emit(f'Operation failed: {str(e)}')

    def __del__(self):
        Worker._db_ref_count -= 1
        if Worker._db_ref_count == 0 and Worker._db is not None:
            Worker._db.close()
            Worker._db = None