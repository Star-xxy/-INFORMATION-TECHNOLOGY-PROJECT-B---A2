# ui/widget_class.py
import sqlite3  # Not used, can be removed if psycopg2 is consistently used
import sys

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QUrl, QRectF, QPropertyAnimation, QEasingCurve, QTimer, QTime, Signal, QSize
from PySide6.QtGui import QIcon, QPainter, QBrush, QColor, QDesktopServices, QPixmap, QPainterPath, \
    QLinearGradient, QImage
from PySide6.QtWidgets import (QApplication, QStackedWidget, QHBoxLayout, QWidget, QFileDialog, QFrame,
                               QListWidgetItem, QDialog, QLabel, QVBoxLayout, QPushButton,
                               QSizePolicy, QListWidget)  # Added some imports

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox, InfoBar, InfoBarPosition,
                            isDarkTheme, setThemeColor, BodyLabel, ImageLabel, PushButton as FluentPushButton,
                            PrimaryPushButton)  # PushButton might conflict, renamed to FluentPushButton

# Assuming Ui_Form are correctly imported for course cards
from ui.classes import Ui_Frame  # Main UI for WidgetClass
from ui.charge import Ui_Dialog as Ui_RechargeDialog  # UI for recharge dialog
from ui.class_course_card import Ui_Form as Ui_ShopCourseCard  # UI for shop course card (Buy button)
from ui.course_card import Ui_Form as Ui_MyCourseCard  # UI for user's owned course card (Watch button)

from utils.database import Database, DB_HOST, DB_NAME, DB_USER, DB_PASSWORD  # Import database


# --- Custom Card Widgets ---
class MyCourseCardWidget(QWidget, Ui_MyCourseCard):
    """ Card for displaying a user's purchased course. """

    def __init__(self, course_data, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.course_data = course_data

        self.BodyLabel.setText(course_data.get("name", "Course Name"))
        self.BodyLabel_2.setText(course_data.get("description", "Course Description"))

        image_path = course_data.get("image_path", "")
        if image_path:
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                self.ImageLabel.setImage(pixmap.scaled(self.ImageLabel.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                                       Qt.TransformationMode.SmoothTransformation))
            else:
                self.ImageLabel.setImage(QPixmap(":/yolo/images/icons/default_course.png"))  # Placeholder
        else:
            self.ImageLabel.setImage(QPixmap(":/yolo/images/icons/default_course.png"))  # Placeholder

        self.PushButton_2.setText("Watch Video")  # From course_card.ui
        # The click connection will be handled in WidgetClass


class ShopCourseCardWidget(QWidget, Ui_ShopCourseCard):
    """ Card for displaying a course available in the shop. """

    def __init__(self, course_data, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.course_data = course_data

        self.BodyLabel.setText(course_data.get("name", "Course Name"))
        description = course_data.get("description", "Course Description")
        points = course_data.get("points_required", 0)
        self.BodyLabel_2.setText(f"{description}\nPrice: {points} points")

        image_path = course_data.get("image_path", "")
        if image_path:
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                self.ImageLabel.setImage(pixmap.scaled(self.ImageLabel.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                                       Qt.TransformationMode.SmoothTransformation))
            else:
                self.ImageLabel.setImage(QPixmap(":/yolo/images/icons/default_course.png"))  # Placeholder
        else:
            self.ImageLabel.setImage(QPixmap(":/yolo/images/icons/default_course.png"))  # Placeholder

        self.PushButton_2.setText(f"Buy ({points} pts)")  # From class_course_card.ui
        # The click connection will be handled in WidgetClass


class WidgetRecharge(QDialog, Ui_RechargeDialog):
    recharge_successful_signal = Signal(int)  # Emits new total points

    def __init__(self, db_conn, user_id, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.db = db_conn
        self.user_id = user_id
        self.setWindowTitle("Recharge Points")

        self.PrimaryPushButton.setText("Confirm Recharge")
        self.PrimaryPushButton.clicked.connect(self.process_recharge)
        self.PushButton.setText("Cancel")
        self.PushButton.clicked.connect(self.reject)

        # Set a default or minimum recharge amount if desired
        self.lineEdit.setText("10")  # Default 10 RMB, for 100 points
        self.lineEdit.setPlaceholderText("Enter amount in RMB")

    def process_recharge(self):
        if not self.user_id:
            InfoBar.error("Error", "User not identified.", parent=self, duration=3000, position=InfoBarPosition.TOP)
            return

        try:
            amount_rmb = int(self.lineEdit.text())
            if amount_rmb <= 0:
                InfoBar.warning("Invalid Amount", "Recharge amount must be positive.", parent=self, duration=3000,
                                position=InfoBarPosition.TOP)
                return
        except ValueError:
            InfoBar.warning("Invalid Input", "Please enter a valid number for the amount.", parent=self, duration=3000,
                            position=InfoBarPosition.TOP)
            return

        points_to_add = amount_rmb * 10  # 1 RMB = 10 points

        success, new_total_points_or_error = self.db.add_user_points(self.user_id, points_to_add)

        if success:
            InfoBar.success("Success", f"{points_to_add} points added successfully!", parent=self, duration=3000,
                            position=InfoBarPosition.TOP)
            self.recharge_successful_signal.emit(
                new_total_points_or_error)  # new_total_points_or_error is new_total_points here
            self.accept()
        else:
            InfoBar.error("Recharge Failed", f"Could not add points: {new_total_points_or_error}", parent=self,
                          duration=3000, position=InfoBarPosition.TOP)


class WidgetClass(QFrame, Ui_Frame):
    def __init__(self, name: str, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setObjectName(name)
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)  # Each widget gets its own DB for now

        self.user_id = None
        self.current_username = "Guest"
        self.current_points = 0
        self.num_owned_courses = 0

        # Set a default avatar or load one
        default_avatar = QPixmap(":/yolo/images/icons/default_user.png")  # Add a default user icon to resources
        if not default_avatar.isNull():
            self.AvatarWidget_2.setImage(
                default_avatar.scaled(self.AvatarWidget_2.width(), self.AvatarWidget_2.height(),
                                      Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

        self.PrimaryPushButton.clicked.connect(self.show_recharge_dialog)

        # Adjust listWidget properties for better card display if needed
        self.listWidget.setSpacing(10)
        self.listWidget_2.setSpacing(10)
        self.listWidget.setViewMode(QListWidget.ViewMode.ListMode)  # Ensure it's list mode
        self.listWidget.setResizeMode(QListWidget.ResizeMode.Adjust)

    def set_user_context(self, user_info: dict):
        """Receives user information and updates the context for this widget."""
        self.user_id = user_info.get('id')
        self.current_username = user_info.get('username', 'Guest')
        self.current_points = user_info.get('points', 0)

        if self.user_id:
            self.num_owned_courses = self.db.count_user_courses(self.user_id)
            self.load_my_courses()
            self.load_shop_courses()  # Shop courses are general, but reload can help reflect owned status if implemented
        else:
            self.listWidget.clear()
            self.listWidget_2.clear()  # Or show a "Please log in" message
            self.num_owned_courses = 0

        self.update_header_display()

    def update_header_display(self):
        """Updates the user information display in the header."""
        self.BodyLabel_8.setText(str(self.current_username))  # Username value
        self.BodyLabel_10.setText(str(self.current_points))  # Points value
        self.BodyLabel_12.setText(str(self.num_owned_courses))  # Number of courses value

        # You might want to update the avatar based on user_info if available
        # self.AvatarWidget_2.setImage(...)

    def load_my_courses(self):
        self.listWidget.clear()
        if not self.user_id:
            return

        my_courses_data = self.db.get_user_purchased_courses(self.user_id)
        self.num_owned_courses = len(my_courses_data)  # Update count

        for course_data in my_courses_data:
            card_widget = MyCourseCardWidget(course_data)
            card_widget.PushButton_2.clicked.connect(
                lambda checked=False, c_data=course_data: self.play_video_for_course(c_data))

            list_item = QListWidgetItem(self.listWidget)
            list_item.setSizeHint(card_widget.sizeHint())  # Important for layout
            self.listWidget.addItem(list_item)
            self.listWidget.setItemWidget(list_item, card_widget)
        self.update_header_display()

    def load_shop_courses(self):
        self.listWidget_2.clear()
        shop_courses_data = self.db.get_shop_courses()

        for course_data in shop_courses_data:
            card_widget = ShopCourseCardWidget(course_data)
            # Pass the card widget itself or its data to the purchase handler
            card_widget.PushButton_2.clicked.connect(
                lambda checked=False, c_data=course_data: self.confirm_purchase_course(c_data))

            list_item = QListWidgetItem(self.listWidget_2)
            list_item.setSizeHint(card_widget.sizeHint())  # Important for layout
            self.listWidget_2.addItem(list_item)
            self.listWidget_2.setItemWidget(list_item, card_widget)

    def play_video_for_course(self, course_data):
        video_path = course_data.get("video_path")
        if video_path:
            print(f"Attempting to play video: {video_path}")
            # Check if file exists, though QDesktopServices might handle it
            if not QDesktopServices.openUrl(QUrl.fromLocalFile(video_path)):
                InfoBar.error("Playback Error", f"Could not open video file: {video_path}", parent=self, duration=3000,
                              position=InfoBarPosition.TOP_RIGHT)
        else:
            InfoBar.warning("No Video", "No video path associated with this course.", parent=self, duration=3000,
                            position=InfoBarPosition.TOP_RIGHT)

    def show_recharge_dialog(self):
        if not self.user_id:
            InfoBar.warning("Login Required", "Please log in to recharge points.", parent=self, duration=3000,
                            position=InfoBarPosition.TOP)
            return

        dialog = WidgetRecharge(self.db, self.user_id, self)
        dialog.recharge_successful_signal.connect(self.handle_recharge_success)
        dialog.exec()

    def handle_recharge_success(self, new_total_points):
        self.current_points = new_total_points
        self.update_header_display()
        # Optionally, refresh main window's point display if it's separate
        if self.parent() and hasattr(self.parent(), 'user_info'):
            self.parent().user_info['points'] = new_total_points
            if hasattr(self.parent(), 'update_user_info_displays'):  # A hypothetical method in MainWindow
                self.parent().update_user_info_displays()

    def confirm_purchase_course(self, course_data):
        if not self.user_id:
            InfoBar.warning("Login Required", "Please log in to purchase courses.", parent=self, duration=3000,
                            position=InfoBarPosition.TOP)
            return

        course_name = course_data.get("name")
        points_required = course_data.get("points_required")

        # Check if already owned (client-side quick check, DB check is authoritative)
        owned_courses = self.db.get_user_purchased_courses(self.user_id)
        if any(c['name'] == course_name for c in owned_courses):
            InfoBar.info("Already Owned", f"You already own the course: {course_name}", parent=self, duration=3000,
                         position=InfoBarPosition.TOP_RIGHT)
            return

        msg_box = MessageBox(
            "Confirm Purchase",
            f"Do you want to buy '{course_name}' for {points_required} points?\nYour current points: {self.current_points}",
            self
        )
        msg_box.yesButton.setText("Confirm")
        msg_box.cancelButton.setText("Cancel")

        if msg_box.exec():
            self.execute_purchase(course_data)

    def execute_purchase(self, course_data):
        course_name = course_data.get("name")
        points_required = course_data.get("points_required")

        if self.current_points < points_required:
            InfoBar.error("Purchase Failed", "Not enough points.", parent=self, duration=3000,
                          position=InfoBarPosition.TOP_RIGHT)
            return

        success, message = self.db.purchase_course(self.user_id, self.current_username, course_name, points_required)

        if success:
            InfoBar.success("Purchase Successful!", f"You have purchased '{course_name}'.", parent=self, duration=3000,
                            position=InfoBarPosition.TOP_RIGHT)
            # Update user's points
            self.current_points -= points_required  # Or fetch fresh from DB
            # user_info_fresh = self.db.get_user_info(self.user_id) # More robust
            # if user_info_fresh: self.current_points = user_info_fresh['points']

            self.load_my_courses()  # Refresh list of owned courses
            # self.load_shop_courses() # Refresh shop (e.g., to disable "Buy" if now owned)
            self.update_header_display()

            # Propagate points update to MainWindow if necessary
            if self.parent() and hasattr(self.parent(), 'user_info'):
                self.parent().user_info['points'] = self.current_points
                if hasattr(self.parent(), 'update_user_info_displays'):
                    self.parent().update_user_info_displays()
        else:
            InfoBar.error("Purchase Failed", message, parent=self, duration=3000, position=InfoBarPosition.TOP_RIGHT)

    def closeEvent(self, event):
        if self.db:
            self.db.close()
        super().closeEvent(event)