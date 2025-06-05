# admin/dialogs.py
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QLineEdit,
                               QPushButton, QDialogButtonBox, QLabel, QMessageBox,
                               QSpinBox, QTextEdit, QDoubleSpinBox)
from PySide6.QtCore import Qt


class BaseEditDialog(QDialog):
    def __init__(self, title, fields_config, data=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(400)

        self.layout = QVBoxLayout(self)
        self.formLayout = QFormLayout()
        self.fields = {}

        for field_info in fields_config:
            label_text = field_info["label"]
            key = field_info["key"]
            field_type = field_info.get("type", "text")
            read_only = field_info.get("read_only", False)
            default_value = data.get(key, field_info.get("default", "")) if data else field_info.get("default", "")

            if field_type == "text":
                widget = QLineEdit(str(default_value))
            elif field_type == "textarea":
                widget = QTextEdit(str(default_value))
                widget.setMinimumHeight(80)
            elif field_type == "int":
                widget = QSpinBox()
                widget.setRange(field_info.get("min", -999999), field_info.get("max", 999999))
                widget.setValue(int(default_value) if str(default_value).isdigit() else 0)
            elif field_type == "float":
                widget = QDoubleSpinBox()
                widget.setRange(field_info.get("min", -999999.0), field_info.get("max", 999999.0))
                widget.setValue(float(default_value) if str(default_value).replace('.', '', 1).isdigit() else 0.0)
            else:  # Default to QLineEdit
                widget = QLineEdit(str(default_value))

            if read_only:
                widget.setReadOnly(True)

            self.fields[key] = widget
            self.formLayout.addRow(label_text, widget)

        self.layout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)

    def get_data(self):
        data = {}
        for key, widget in self.fields.items():
            if isinstance(widget, QLineEdit) or isinstance(widget, QTextEdit):
                data[key] = widget.text() if isinstance(widget, QLineEdit) else widget.toPlainText()
            elif isinstance(widget, QSpinBox) or isinstance(widget, QDoubleSpinBox):
                data[key] = widget.value()
        return data


# --- Specific Dialog Configurations ---

USER_FIELDS_CONFIG = [
    {"label": "ID:", "key": "id", "type": "int", "read_only": True, "default": 0},
    {"label": "Username:", "key": "username", "type": "text"},
    {"label": "Password:", "key": "password", "type": "text", "default": ""},  # Admin can set/reset
    {"label": "Email:", "key": "mail", "type": "text"},
    {"label": "Age:", "key": "age", "type": "int"},
    {"label": "Weight:", "key": "weight", "type": "float"},
    {"label": "Points:", "key": "points", "type": "int"},
    {"label": "Level:", "key": "level", "type": "int"},
    {"label": "Training Days:", "key": "training_days", "type": "int"},
    {"label": "Training Time:", "key": "training_time", "type": "int"},
]

COURSE_FIELDS_CONFIG = [
    {"label": "ID:", "key": "id", "type": "int", "read_only": True, "default": 0},
    {"label": "Course Name:", "key": "course_name", "type": "text"},
    {"label": "Description:", "key": "course_description", "type": "textarea"},
    {"label": "Points Required:", "key": "points_required", "type": "int"},
    {"label": "Image Path:", "key": "image_path", "type": "text"},
    {"label": "Video Path:", "key": "video_path", "type": "text"},
]

POST_FIELDS_CONFIG = [
    {"label": "ID:", "key": "id", "type": "int", "read_only": True, "default": 0},
    {"label": "Author Username:", "key": "author_username", "type": "text", "read_only": True},
    # Usually not editable by admin unless impersonating
    {"label": "Post Time:", "key": "post_time", "type": "text", "read_only": True},
    {"label": "Content:", "key": "content", "type": "textarea"},
    {"label": "Image URL:", "key": "image_url", "type": "text", "default": ""},
    {"label": "Video URL:", "key": "video_url", "type": "text", "default": ""},
    {"label": "Likes:", "key": "likes", "type": "int"},
    {"label": "Favorites:", "key": "favorites", "type": "int"},
]

COMMENT_FIELDS_CONFIG = [
    {"label": "ID:", "key": "id", "type": "int", "read_only": True, "default": 0},
    {"label": "Post ID:", "key": "post_id", "type": "int", "read_only": True},
    {"label": "Commenter:", "key": "commenter_username", "type": "text", "read_only": True},
    {"label": "Comment Time:", "key": "comment_time", "type": "text", "read_only": True},
    {"label": "Content:", "key": "content", "type": "textarea"},
]