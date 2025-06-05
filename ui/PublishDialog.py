# Add these imports to the top of your file
import os

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit,
                               QLineEdit, QPushButton, QSpacerItem, QSizePolicy, QFileDialog)
from PySide6.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarPosition # For feedback

from config.config import cfg


# --- New Publish Dialog Class ---
class PublishDialog(QDialog):
    def __init__(self, username, db, parent=None):
        super().__init__(parent)
        self.username = username
        self.db = db
        self.image_path = None
        self.video_path = None

        self.setWindowTitle("Publish Post")
        self.setMinimumWidth(450) # Adjust as needed

        # --- Widgets ---
        self.instruction_label = QLabel("Share your training thoughts or achievements:")
        self.content_edit = QTextEdit()
        self.content_edit.setPlaceholderText("Enter your post content here...")
        self.content_edit.setMinimumHeight(100)

        self.select_image_btn = QPushButton(QIcon.fromTheme("document-open"), " Select Image (Optional)") # Placeholder icon
        self.image_path_label = QLabel("No image selected")
        self.image_path_label.setStyleSheet("color: gray;")

        self.select_video_btn = QPushButton(QIcon.fromTheme("document-open"), " Select Video (Optional)") # Placeholder icon
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
        image_layout.addWidget(self.image_path_label, 1) # Label takes remaining space
        main_layout.addLayout(image_layout)

        # Video Selection Area
        video_layout = QHBoxLayout()
        video_layout.addWidget(self.select_video_btn)
        video_layout.addWidget(self.video_path_label, 1) # Label takes remaining space
        main_layout.addLayout(video_layout)

        # Spacer
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Button Area
        button_layout = QHBoxLayout()
        button_layout.addStretch(1) # Push buttons to the right
        button_layout.addWidget(self.cancel_btn)
        button_layout.addWidget(self.publish_btn)
        main_layout.addLayout(button_layout)

        # --- Connections ---
        self.select_image_btn.clicked.connect(self.select_image_file)
        self.select_video_btn.clicked.connect(self.select_video_file)
        self.publish_btn.clicked.connect(self.accept) # Built-in slot for Accepted result
        self.cancel_btn.clicked.connect(self.reject) # Built-in slot for Rejected result

    def select_image_file(self):
        """Opens a dialog to select an image file."""
        # Use cfg path if available, otherwise default to home
        start_path = cfg.get(cfg.open_fold) if 'cfg' in globals() else os.path.expanduser("~")
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            start_path,
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_path:
            self.image_path = file_path
            # Display only filename for brevity in UI
            self.image_path_label.setText(f"Image: {os.path.basename(file_path)}")
            self.image_path_label.setStyleSheet("color: black;") # Change color to indicate selection
            if 'cfg' in globals():
                cfg.set(cfg.open_fold, os.path.dirname(file_path)) # Update last opened folder

    def select_video_file(self):
        """Opens a dialog to select a video file."""
        start_path = cfg.get(cfg.open_fold) if 'cfg' in globals() else os.path.expanduser("~")
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
            if 'cfg' in globals():
                cfg.set(cfg.open_fold, os.path.dirname(file_path))

    def get_post_data(self):
        """Returns the data entered by the user."""
        return {
            "content": self.content_edit.toPlainText().strip(),
            "image_url": self.image_path,
            "video_url": self.video_path
        }

# --- End of Publish Dialog Class ---