# coding:utf-8
import sys
import os  # Add os import for path manipulation

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QUrl, QRectF, QPropertyAnimation, QEasingCurve, QTimer, QTime, QObject  # Added QObject
from PySide6.QtGui import QIcon, QPainter, QBrush, QColor, QDesktopServices, QPixmap, QPainterPath, \
    QLinearGradient
# Import necessary widgets for the dialog and main class
from PySide6.QtWidgets import (QApplication, QStackedWidget, QHBoxLayout, QWidget, QFileDialog, QFrame,
                               QDialog, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton, QSpacerItem,
                               QSizePolicy)

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox,
                            isDarkTheme, setThemeColor, InfoBar, InfoBarPosition)  # Added InfoBar, InfoBarPosition

from config.config import cfg
from ui.analyze import Ui_Frame as UI_detect
from utils.style_sheet import StyleSheet

# Make sure the Database class import is correct (adjust path if needed)
# Assuming it's in utils/database.py or similar
try:
    # If database_pg.py exists from previous steps
    from database_pg import Database
except ImportError:
    # Fallback to original name if needed
    from utils.database import Database


# --- PublishDialog Class Definition (Paste the class code from step 1 here) ---
class PublishDialog(QDialog):
    # ... (Paste the full PublishDialog class code here) ...
    def __init__(self, username, db, parent=None):
        super().__init__(parent)
        self.username = username
        self.db = db
        self.image_path = None
        self.video_path = None

        self.setWindowTitle("Publish Post")
        self.setMinimumWidth(450)  # Adjust as needed

        # --- Widgets ---
        self.instruction_label = QLabel("Share your training thoughts or achievements:")
        self.content_edit = QTextEdit()
        self.content_edit.setPlaceholderText("Enter your post content here...")
        self.content_edit.setMinimumHeight(100)

        # Use standard icons if theme icons aren't reliable
        # self.select_image_btn = QPushButton(QIcon.fromTheme("document-open", QIcon(":/qfluentwidgets/images/folder.png")), " Select Image (Optional)")
        # self.select_video_btn = QPushButton(QIcon.fromTheme("document-open", QIcon(":/qfluentwidgets/images/folder.png")), " Select Video (Optional)")
        self.select_image_btn = QPushButton(" Select Image (Optional)")  # Simpler button without icon issues
        self.image_path_label = QLabel("No image selected")
        self.image_path_label.setStyleSheet("color: gray;")

        self.select_video_btn = QPushButton(" Select Video (Optional)")  # Simpler button without icon issues
        self.video_path_label = QLabel("No video selected")
        self.video_path_label.setStyleSheet("color: gray;")

        self.publish_btn = QPushButton("Publish")
        self.cancel_btn = QPushButton("Cancel")

        # --- Layouts ---
        main_layout = QVBoxLayout(self)

        # Content Area
        main_layout.addWidget(self.instruction_label)
        main_layout.addWidget(self.content_edit)

        # Image Selection Area
        image_layout = QHBoxLayout()
        image_layout.addWidget(self.select_image_btn)
        image_layout.addWidget(self.image_path_label, 1)  # Label takes remaining space
        main_layout.addLayout(image_layout)

        # Video Selection Area
        video_layout = QHBoxLayout()
        video_layout.addWidget(self.select_video_btn)
        video_layout.addWidget(self.video_path_label, 1)  # Label takes remaining space
        main_layout.addLayout(video_layout)

        # Spacer
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Button Area
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)  # Push buttons to the right
        button_layout.addWidget(self.cancel_btn)
        button_layout.addWidget(self.publish_btn)
        main_layout.addLayout(button_layout)

        # --- Connections ---
        self.select_image_btn.clicked.connect(self.select_image_file)
        self.select_video_btn.clicked.connect(self.select_video_file)
        self.publish_btn.clicked.connect(self.accept)  # Built-in slot for Accepted result
        self.cancel_btn.clicked.connect(self.reject)  # Built-in slot for Rejected result

    def select_image_file(self):
        """Opens a dialog to select an image file."""
        # Use a default path if cfg is not available
        start_path = os.path.expanduser("~")
        if 'cfg' in globals() and hasattr(cfg, 'open_fold'):
            start_path = cfg.get(cfg.open_fold)

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            start_path,
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_path:
            self.image_path = file_path
            self.image_path_label.setText(f"Image: {os.path.basename(file_path)}")
            self.image_path_label.setStyleSheet("color: black;")
            if 'cfg' in globals() and hasattr(cfg, 'open_fold'):
                try:
                    cfg.set(cfg.open_fold, os.path.dirname(file_path))
                except Exception as e:
                    print(f"Warning: Could not save last folder path: {e}")

    def select_video_file(self):
        """Opens a dialog to select a video file."""
        start_path = os.path.expanduser("~")
        if 'cfg' in globals() and hasattr(cfg, 'open_fold'):
            start_path = cfg.get(cfg.open_fold)

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Video",
            start_path,
            "Video Files (*.mp4 *.avi *.mkv *.mov *.wmv)"
        )
        if file_path:
            self.video_path = file_path
            self.video_path_label.setText(f"Video: {os.path.basename(file_path)}")
            self.video_path_label.setStyleSheet("color: black;")
            if 'cfg' in globals() and hasattr(cfg, 'open_fold'):
                try:
                    cfg.set(cfg.open_fold, os.path.dirname(file_path))
                except Exception as e:
                    print(f"Warning: Could not save last folder path: {e}")

    def get_post_data(self):
        """Returns the data entered by the user."""
        return {
            "content": self.content_edit.toPlainText().strip(),
            "image_url": self.image_path,
            "video_url": self.video_path
        }


# --- End of PublishDialog ---


class WidgetAnalyze(QFrame, UI_detect):
    user_name = "None"
    refresh_cards = False

    # Modify __init__ to accept username and db
    def __init__(self, name: str, parent=None):
        super().__init__(parent=parent)
        # Use username for object name or keep separate 'name'? Let's use username.
        self.setObjectName(name)
        self.setupUi(self)
        self.PrimaryToolButton.setText('Detect')

        # Store username and db instance
        self.db = Database()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.elapsed_time = QTime(0, 0, 0)

        # Connect buttons if they exist in your UI file (Ui_Frame)
        # Ensure the names 'start_training_btn' and 'end_training_btn' match your .ui file
        if hasattr(self, 'start_training_btn'):
            self.start_training_btn.clicked.connect(self.start_training)
        else:
            print("Warning: start_training_btn not found in UI_detect")

        if hasattr(self, 'end_training_btn'):
            self.end_training_btn.clicked.connect(self.end_training)
        else:
            print("Warning: end_training_btn not found in UI_detect")

        # Initialize time display
        self.update_time_display(self.elapsed_time)

    def start_training(self):
        print("Training started.")
        self.elapsed_time.setHMS(0, 0, 0)  # Reset time
        self.update_time_display(self.elapsed_time)  # Update display immediately
        self.timer.start(1000)  # Start timer, update every second
        if hasattr(self, 'start_training_btn'):
            self.start_training_btn.setEnabled(False)
        if hasattr(self, 'end_training_btn'):
            self.end_training_btn.setEnabled(True)  # Enable end button

    def update_time(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        self.update_time_display(self.elapsed_time)

    def update_time_display(self, time_obj):
        """Helper method to update the time label"""
        hours = f"{time_obj.hour():02}"
        minutes = f"{time_obj.minute():02}"
        seconds = f"{time_obj.second():02}"

        text = (f"Exercise time: <span style='color:red; font-size:20px; font-weight:bold;'>{hours}</span>h "
                f"<span style='color:red; font-size:20px; font-weight:bold;'>{minutes}</span>m "
                f"<span style='color:red; font-size:20px; font-weight:bold;'>{seconds}</span>s")
        if hasattr(self, 'BodyLabel_2'):
            self.BodyLabel_2.setText(text)
        else:
            print("Warning: BodyLabel_2 not found in UI_detect")

    def end_training(self):
        print("End training clicked.")
        training_duration_seconds = 0
        if self.timer.isActive():
            self.timer.stop()
            # Calculate total seconds if needed later
            training_duration_seconds = QTime(0, 0, 0).secsTo(self.elapsed_time)
            print(f"Training stopped. Duration: {self.elapsed_time.toString('hh:mm:ss')}")
            # Update final time display
            self.update_time_display(self.elapsed_time)

        # Reset button states
        if hasattr(self, 'start_training_btn'):
            self.start_training_btn.setEnabled(True)
        if hasattr(self, 'end_training_btn'):
            self.end_training_btn.setEnabled(False)  # Disable end button after stopping

        # --- Show Publish Dialog ---
        dialog = PublishDialog(username=self.user_name, db=self.db, parent=self)
        result = dialog.exec()  # Show the dialog modally

        if result == QDialog.Accepted:
            post_data = dialog.get_post_data()
            content = post_data["content"]
            image_url = post_data["image_url"]  # Will be None if not selected
            video_url = post_data["video_url"]  # Will be None if not selected

            # Basic validation: require some content to publish
            if not content:
                InfoBar.warning(
                    title="Cannot Publish",
                    content="Post content cannot be empty.",
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT,  # Position relative to parent (WidgetAnalyze)
                    duration=3000,
                    parent=self
                )
                print("Publish canceled: Content was empty.")
                return  # Don't proceed if content is empty

            print(
                f"Attempting to publish post for {self.user_name}: Content='{content[:20]}...', Image='{image_url}', Video='{video_url}'")
            try:
                # Call the database function to create the post
                success = self.db.create_post(
                    author_username=self.user_name,
                    content=content,
                    image_url=image_url,
                    video_url=video_url
                )
                if success:
                    print("Post published successfully.")
                    InfoBar.success(
                        title="Success",
                        content="Your post has been published successfully!",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.TOP_RIGHT,
                        duration=3000,
                        parent=self
                    )
                else:
                    # Handle case where create_post returns False (e.g., DB error handled internally)
                    print("Failed to publish post (db.create_post returned False).")
                    InfoBar.error(
                        title="Error",
                        content="Failed to publish post due to a database issue.",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.TOP_RIGHT,
                        duration=4000,
                        parent=self
                    )

            except Exception as e:
                print(f"Error publishing post: {e}")
                import traceback
                traceback.print_exc()
                InfoBar.error(
                    title="Error",
                    content=f"An unexpected error occurred while publishing: {e}",
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT,
                    duration=5000,  # Show error longer
                    parent=self
                )

        else:
            # User clicked Cancel or closed the dialog
            print("Publish dialog canceled by user.")
            InfoBar.info(
                title="Canceled",
                content="Post discarded.",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        self.refresh_cards = True
        # --- End of Publish Dialog Handling ---


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # --- Database Setup for Testing ---
    # Make sure database connection details are correct in Database class or here
    try:
        db_instance = Database()  # Uses connection details defined in the class
        if not db_instance.conn:
            print("FATAL: Could not connect to the database for testing. Exiting.")
            sys.exit(1)
        print("Database connected for testing.")
        # You might want to ensure a test user exists
        test_user = "testuser_pg1"  # Use a user known to be in the DB
        # Optionally check if user exists
        # if not db_instance.check_login(test_user, "some_password"): # Check if user exists (might need password logic)
        #    print(f"Warning: Test user '{test_user}' might not exist in the database.")

    except Exception as e:
        print(f"FATAL: Error initializing database for testing: {e}")
        sys.exit(1)
    # --- End Database Setup ---

    # Instantiate WidgetAnalyze with username and db instance
    # Use a known username from your database for testing 'create_post'
    window = WidgetAnalyze(username=test_user, db=db_instance)
    window.show()

    exit_code = app.exec()

    # --- Cleanup ---
    if db_instance and db_instance.conn:
        db_instance.close()
        print("Database connection closed.")
    sys.exit(exit_code)
