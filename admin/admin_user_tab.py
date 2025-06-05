# admin/admin_user_tab.py
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, QAbstractItemView,
                               QHeaderView, QPushButton, QHBoxLayout, QMessageBox,
                               QTableWidgetItem, QDialog)
from PySide6.QtCore import Qt
from utils.database import Database  # Assuming same DB connection params for now
from admin.dialogs import BaseEditDialog, USER_FIELDS_CONFIG


class AdminUserTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = Database()  # Each tab manages its own DB connection for simplicity here

        self.layout = QVBoxLayout(self)

        # Action buttons
        self.actionLayout = QHBoxLayout()
        self.refreshButton = QPushButton("Refresh")
        self.refreshButton.clicked.connect(self.load_data)
        self.addButton = QPushButton("Add User")
        self.addButton.clicked.connect(self.add_item)
        self.editButton = QPushButton("Edit User")
        self.editButton.clicked.connect(self.edit_item)
        self.deleteButton = QPushButton("Delete User")
        self.deleteButton.clicked.connect(self.delete_item)

        self.actionLayout.addWidget(self.refreshButton)
        self.actionLayout.addStretch()
        self.actionLayout.addWidget(self.addButton)
        self.actionLayout.addWidget(self.editButton)
        self.actionLayout.addWidget(self.deleteButton)
        self.layout.addLayout(self.actionLayout)

        # Table
        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.layout.addWidget(self.tableWidget)

        self.load_data()

    def load_data(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        data = self.db.admin_get_all_user_details()
        if data is None:
            QMessageBox.critical(self, "Error", "Failed to load user data from database.")
            return
        if not data: return

        headers = list(USER_FIELDS_CONFIG[i]["key"] for i in range(len(USER_FIELDS_CONFIG)))  # Use defined order
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels([cfg["label"] for cfg in USER_FIELDS_CONFIG])

        for row_idx, record in enumerate(data):
            self.tableWidget.insertRow(row_idx)
            for col_idx, header_key in enumerate(headers):
                item_value = str(record.get(header_key, ''))
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(item_value))
        self.tableWidget.resizeColumnsToContents()

    def get_selected_record_id(self, id_column_name="id"):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Selection Error", "Please select a user first.")
            return None

        header_labels = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
        try:
            # Find the column index for the ID using the display label from USER_FIELDS_CONFIG
            id_display_label = next(cfg["label"] for cfg in USER_FIELDS_CONFIG if cfg["key"] == id_column_name)
            id_col_idx = header_labels.index(id_display_label)
        except (StopIteration, ValueError):
            QMessageBox.critical(self, "Error", f"Configuration error: Cannot find column for '{id_column_name}'.")
            return None

        selected_row_index = selected_rows[0].row()
        id_item = self.tableWidget.item(selected_row_index, id_col_idx)
        return int(id_item.text()) if id_item else None

    def get_record_data_from_selected_row(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows: return None

        row_idx = selected_rows[0].row()
        record_data = {}
        # Use USER_FIELDS_CONFIG to map column to key and get data
        for col_idx, field_cfg in enumerate(USER_FIELDS_CONFIG):
            key = field_cfg["key"]
            item = self.tableWidget.item(row_idx, col_idx)
            if item:
                # Attempt to convert to original type for dialog if necessary, dialog handles defaults
                raw_value = item.text()
                if field_cfg.get("type") == "int":
                    try:
                        record_data[key] = int(raw_value)
                    except ValueError:
                        record_data[key] = 0
                elif field_cfg.get("type") == "float":
                    try:
                        record_data[key] = float(raw_value)
                    except ValueError:
                        record_data[key] = 0.0
                else:
                    record_data[key] = raw_value
            else:
                record_data[key] = field_cfg.get("default", "")  # Default if cell is empty for some reason
        return record_data

    def add_item(self):
        # Create a fields config for adding, 'id' is not needed for input
        add_config = [cfg for cfg in USER_FIELDS_CONFIG if cfg["key"] != "id"]
        dialog = BaseEditDialog("Add New User", add_config, data=None, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            new_data = dialog.get_data()
            # Validate required fields, e.g., username, password, mail
            if not all(new_data.get(key) for key in ["username", "password", "mail"]):
                QMessageBox.warning(self, "Input Error", "Username, Password, and Email are required.")
                return

            if self.db.admin_add_user(
                    username=new_data["username"], password=new_data["password"], mail=new_data["mail"],
                    age=new_data.get("age", 0), weight=new_data.get("weight", 0.0),
                    points=new_data.get("points", 0), level=new_data.get("level", 0),
                    training_days=new_data.get("training_days", 0), training_time=new_data.get("training_time", 0)
            ):
                QMessageBox.information(self, "Success", "User added successfully.")
                self.load_data()
            else:
                QMessageBox.critical(self, "Database Error", "Failed to add user.")

    def edit_item(self):
        record_id = self.get_selected_record_id()
        if record_id is None: return

        current_data = self.get_record_data_from_selected_row()
        if current_data is None: return

        dialog = BaseEditDialog("Edit User", USER_FIELDS_CONFIG, data=current_data, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            updated_data = dialog.get_data()
            # Remove ID from data to be updated, as it's used in WHERE clause
            data_for_update = {k: v for k, v in updated_data.items() if k != "id"}

            if self.db.admin_update_user(record_id, data_for_update):
                QMessageBox.information(self, "Success", "User updated successfully.")
                self.load_data()
            else:
                QMessageBox.critical(self, "Database Error", "Failed to update user.")

    def delete_item(self):
        record_id = self.get_selected_record_id()
        if record_id is None: return

        reply = QMessageBox.question(self, "Confirm Delete",
                                     f"Are you sure you want to delete user ID {record_id}?\nThis may also delete their posts, comments, and other related data.",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            if self.db.admin_delete_user(record_id):
                QMessageBox.information(self, "Success", "User deleted successfully.")
                self.load_data()
            else:
                QMessageBox.critical(self, "Database Error", "Failed to delete user.")

    def closeEvent(self, event):  # For completeness if tab has specific close needs
        if self.db: self.db.close()
        super().closeEvent(event)