# admin/admin_user_course_tab.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QAbstractItemView, QHeaderView, QPushButton, \
    QTableWidgetItem, QMessageBox
from utils.database import Database


class AdminUserCourseTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = Database()
        self.layout = QVBoxLayout(self)

        self.refreshButton = QPushButton("Refresh Data")
        self.refreshButton.clicked.connect(self.load_data)
        self.layout.addWidget(self.refreshButton)

        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        # ... other table settings ...
        self.layout.addWidget(self.tableWidget)
        self.load_data()

    def load_data(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        data = self.db.admin_get_all_user_courses()
        if data is None: QMessageBox.critical(self, "Error", "Failed to load user course data."); return
        if not data: return

        headers = ["Purchase ID", "User ID", "Username", "Course Name", "Course Description", "Purchase Date"]
        # Match these to keys from db.admin_get_all_user_courses()
        db_keys = ["id", "user_id", "user_username", "course_name", "course_description", "purchase_date"]

        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row_idx, record in enumerate(data):
            self.tableWidget.insertRow(row_idx)
            for col_idx, key in enumerate(db_keys):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(record.get(key, ''))))
        self.tableWidget.resizeColumnsToContents()

    def closeEvent(self, event):
        if self.db: self.db.close()
        super().closeEvent(event)

