
# admin/admin_friend_tab.py (Similar structure)
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QAbstractItemView, QHeaderView, QPushButton, \
    QTableWidgetItem, QMessageBox
from utils.database import Database


class AdminFriendTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = Database()
        self.layout = QVBoxLayout(self)
        self.refreshButton = QPushButton("Refresh Data")
        self.refreshButton.clicked.connect(self.load_data)
        self.layout.addWidget(self.refreshButton)
        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.layout.addWidget(self.tableWidget)
        self.load_data()

    def load_data(self):
        self.tableWidget.clearContents();
        self.tableWidget.setRowCount(0)
        data = self.db.admin_get_all_friends()
        if data is None: QMessageBox.critical(self, "Error", "Failed to load friend data."); return
        if not data: return
        headers = ["ID", "User ID", "Username", "Friend Username"]
        db_keys = ["id", "user_id", "user_username", "friend_username"]
        self.tableWidget.setColumnCount(len(headers));
        self.tableWidget.setHorizontalHeaderLabels(headers)
        for r, rec in enumerate(data):
            self.tableWidget.insertRow(r)
            for c, k in enumerate(db_keys): self.tableWidget.setItem(r, c, QTableWidgetItem(str(rec.get(k, ''))))
        self.tableWidget.resizeColumnsToContents()

    def closeEvent(self, event):
        if self.db: self.db.close()
        super().closeEvent(event)