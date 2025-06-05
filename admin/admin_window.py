# admin/admin_window.py
from PySide6.QtWidgets import QMainWindow, QTabWidget, QApplication, QWidget
from PySide6.QtGui import QIcon
import sys

# Import tab widgets
from admin.admin_user_tab import AdminUserTab
from admin.admin_course_tab import AdminCourseTab
from admin.admin_post_tab import AdminPostTab
from admin.admin_user_course_tab import AdminUserCourseTab
from admin.admin_activity_tab import AdminActivityTab
from admin.admin_friend_tab import AdminFriendTab


class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Administrator Panel")
        # self.setWindowIcon(QIcon("path/to/your/admin_icon.png")) # Add an icon
        self.resize(1000, 700)

        self.tabWidget = QTabWidget(self)
        self.setCentralWidget(self.tabWidget)

        # Create and add tabs
        self.userTab = AdminUserTab(self)
        self.tabWidget.addTab(self.userTab, "User Management")

        self.courseTab = AdminCourseTab(self)
        self.tabWidget.addTab(self.courseTab, "Shop Courses")

        self.postTab = AdminPostTab(self)
        self.tabWidget.addTab(self.postTab, "Posts & Comments")

        self.userCourseTab = AdminUserCourseTab(self)
        self.tabWidget.addTab(self.userCourseTab, "User Purchased Courses")

        self.activityTab = AdminActivityTab(self)
        self.tabWidget.addTab(self.activityTab, "User Activities")

        self.friendTab = AdminFriendTab(self)
        self.tabWidget.addTab(self.friendTab, "Friendships")

        self.center_window()

    def center_window(self):
        screen = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(
            (screen.width() - self.width()) // 2,
            (screen.height() - self.height()) // 2,
            self.width(),
            self.height()
        )

    def closeEvent(self, event):
        # Ensure child tabs also close their DB connections if they manage them
        for i in range(self.tabWidget.count()):
            widget = self.tabWidget.widget(i)
            if hasattr(widget, 'closeEvent'):  # Call custom closeEvent if defined
                # This is tricky, as QWidget's closeEvent is for top-level windows.
                # Better to have an explicit db_close method on tabs.
                if hasattr(widget, 'db_close'):
                    widget.db_close()
                elif hasattr(widget, 'db') and widget.db is not None:  # Fallback
                    print(f"Closing DB for tab: {self.tabWidget.tabText(i)}")
                    widget.db.close()
        super().closeEvent(event)


if __name__ == '__main__':  # For testing AdminWindow directly
    # Ensure your resource_rc.py (if any for icons) is imported in the main execution flow
    # or here for direct testing if icons are used from resources.
    # from resource import resource_rc
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec())