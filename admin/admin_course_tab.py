# admin/admin_course_tab.py
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, QAbstractItemView,
                               QHeaderView, QPushButton, QHBoxLayout, QMessageBox,
                               QTableWidgetItem, QDialog)
from PySide6.QtCore import Qt
from utils.database import Database
from admin.dialogs import BaseEditDialog, COURSE_FIELDS_CONFIG


class AdminCourseTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = Database()

        self.layout = QVBoxLayout(self)

        self.actionLayout = QHBoxLayout()
        self.refreshButton = QPushButton("Refresh")
        self.refreshButton.clicked.connect(self.load_data)
        self.addButton = QPushButton("Add Course")
        self.addButton.clicked.connect(self.add_item)
        self.editButton = QPushButton("Edit Course")
        self.editButton.clicked.connect(self.edit_item)
        self.deleteButton = QPushButton("Delete Course")
        self.deleteButton.clicked.connect(self.delete_item)

        self.actionLayout.addWidget(self.refreshButton)
        self.actionLayout.addStretch()
        self.actionLayout.addWidget(self.addButton)
        self.actionLayout.addWidget(self.editButton)
        self.actionLayout.addWidget(self.deleteButton)
        self.layout.addLayout(self.actionLayout)

        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        # ... other table settings ...
        self.layout.addWidget(self.tableWidget)
        self.load_data()

    def load_data(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        data = self.db.admin_get_all_shop_courses()  # Uses existing get_shop_courses
        if data is None:
            QMessageBox.critical(self, "Error", "Failed to load course data.")
            return
        if not data: return

        # Map database keys to COURSE_FIELDS_CONFIG keys
        # DB returns: "id", "name", "description", "points_required", "image_path", "video_path"
        # Config uses: "id", "course_name", "course_description", etc.
        # We need a consistent set of headers for the table.
        headers_cfg = COURSE_FIELDS_CONFIG
        header_keys = [cfg["key"] for cfg in headers_cfg]
        header_labels = [cfg["label"] for cfg in headers_cfg]

        self.tableWidget.setColumnCount(len(header_labels))
        self.tableWidget.setHorizontalHeaderLabels(header_labels)

        for row_idx, db_record in enumerate(data):
            self.tableWidget.insertRow(row_idx)
            # Map db_record keys to config keys for consistent column order
            # Example: db_record might have "name", config expects "course_name" for the cell.
            # For simplicity, assuming db.get_shop_courses returns keys that match COURSE_FIELDS_CONFIG['key']
            # or we adapt the data before display.
            # Let's assume direct mapping for now, db.get_shop_courses returns dicts with keys:
            # id, name (map to course_name), description (map to course_description), points_required, image_path, video_path

            record_for_display = {
                "id": db_record.get("id"),
                "course_name": db_record.get("name"),  # Mapping
                "course_description": db_record.get("description"),  # Mapping
                "points_required": db_record.get("points_required"),
                "image_path": db_record.get("image_path"),
                "video_path": db_record.get("video_path")
            }

            for col_idx, key in enumerate(header_keys):
                item_value = str(record_for_display.get(key, ''))
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(item_value))
        self.tableWidget.resizeColumnsToContents()

    def get_selected_record_id_and_data(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Selection Error", "Please select a course.")
            return None, None

        row_idx = selected_rows[0].row()
        record_data = {}
        record_id = None

        for col_idx, field_cfg in enumerate(COURSE_FIELDS_CONFIG):
            key = field_cfg["key"]
            item = self.tableWidget.item(row_idx, col_idx)
            value_str = item.text() if item else ""

            if field_cfg.get("type") == "int":
                try:
                    value = int(value_str)
                except ValueError:
                    value = 0
            else:  # text, textarea
                value = value_str

            record_data[key] = value
            if key == "id":
                record_id = value
        return record_id, record_data

    def add_item(self):
        add_config = [cfg for cfg in COURSE_FIELDS_CONFIG if cfg["key"] != "id"]
        dialog = BaseEditDialog("Add New Course", add_config, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            new_data = dialog.get_data()
            if not new_data.get("course_name"):
                QMessageBox.warning(self, "Input Error", "Course Name is required.")
                return

            if self.db.admin_add_shop_course(
                    name=new_data["course_name"], description=new_data.get("course_description", ""),
                    points=new_data.get("points_required", 0),
                    image_path=new_data.get("image_path", ""), video_path=new_data.get("video_path", "")
            ):
                QMessageBox.information(self, "Success", "Course added successfully.")
                self.load_data()
            else:
                QMessageBox.critical(self, "Database Error", "Failed to add course.")

    def edit_item(self):
        record_id, current_data = self.get_selected_record_id_and_data()
        if record_id is None: return

        dialog = BaseEditDialog("Edit Course", COURSE_FIELDS_CONFIG, data=current_data, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            updated_data = dialog.get_data()
            data_for_update = {k: v for k, v in updated_data.items() if k != "id"}

            if self.db.admin_update_shop_course(record_id, data_for_update):
                QMessageBox.information(self, "Success", "Course updated successfully.")
                self.load_data()
            else:
                QMessageBox.critical(self, "Database Error", "Failed to update course.")

    def delete_item(self):
        record_id, _ = self.get_selected_record_id_and_data()
        if record_id is None: return

        reply = QMessageBox.question(self, "Confirm Delete",
                                     f"Are you sure you want to delete course ID {record_id}?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            if self.db.admin_delete_shop_course(record_id):
                QMessageBox.information(self, "Success", "Course deleted successfully.")
                self.load_data()
            else:
                QMessageBox.critical(self, "Database Error", "Failed to delete course.")

    def closeEvent(self, event):
        if self.db: self.db.close()
        super().closeEvent(event)