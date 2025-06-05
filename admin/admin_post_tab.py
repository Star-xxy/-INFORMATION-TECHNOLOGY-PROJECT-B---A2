# admin/admin_post_tab.py
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, QAbstractItemView,
                               QHeaderView, QPushButton, QHBoxLayout, QMessageBox,
                               QTableWidgetItem, QDialog, QLabel, QSplitter)
from PySide6.QtCore import Qt, Slot
from utils.database import Database
from admin.dialogs import BaseEditDialog, POST_FIELDS_CONFIG, COMMENT_FIELDS_CONFIG


class AdminPostTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = Database()
        self.current_selected_post_id = None

        self.layout = QVBoxLayout(self)

        # Splitter for Posts and Comments
        self.splitter = QSplitter(Qt.Orientation.Vertical)

        # --- Posts Section ---
        self.postsWidget = QWidget()
        self.postsLayout = QVBoxLayout(self.postsWidget)
        self.postsLayout.addWidget(QLabel("<h2>Posts</h2>"))

        self.postActionLayout = QHBoxLayout()
        self.refreshPostsButton = QPushButton("Refresh Posts")
        self.refreshPostsButton.clicked.connect(self.load_posts_data)
        # self.addPostButton = QPushButton("Add Post") # Admin adding posts needs author - for now, edit/delete
        # self.addPostButton.clicked.connect(self.add_post_item)
        self.editPostButton = QPushButton("Edit Post")
        self.editPostButton.clicked.connect(self.edit_post_item)
        self.deletePostButton = QPushButton("Delete Post")
        self.deletePostButton.clicked.connect(self.delete_post_item)

        self.postActionLayout.addWidget(self.refreshPostsButton)
        self.postActionLayout.addStretch()
        # self.postActionLayout.addWidget(self.addPostButton)
        self.postActionLayout.addWidget(self.editPostButton)
        self.postActionLayout.addWidget(self.deletePostButton)
        self.postsLayout.addLayout(self.postActionLayout)

        self.postsTableWidget = QTableWidget()
        self.postsTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.postsTableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.postsTableWidget.itemSelectionChanged.connect(self.on_post_selected)
        self.postsLayout.addWidget(self.postsTableWidget)
        self.splitter.addWidget(self.postsWidget)

        # --- Comments Section ---
        self.commentsWidget = QWidget()
        self.commentsLayout = QVBoxLayout(self.commentsWidget)
        self.commentsLayout.addWidget(QLabel("<h3>Comments for Selected Post</h3>"))

        self.commentActionLayout = QHBoxLayout()
        self.refreshCommentsButton = QPushButton("Refresh Comments")
        self.refreshCommentsButton.clicked.connect(self.load_comments_for_selected_post)
        # self.addCommentButton = QPushButton("Add Comment")
        # self.addCommentButton.clicked.connect(self.add_comment_item)
        self.editCommentButton = QPushButton("Edit Comment")
        self.editCommentButton.clicked.connect(self.edit_comment_item)
        self.deleteCommentButton = QPushButton("Delete Comment")
        self.deleteCommentButton.clicked.connect(self.delete_comment_item)

        self.commentActionLayout.addWidget(self.refreshCommentsButton)
        self.commentActionLayout.addStretch()
        # self.commentActionLayout.addWidget(self.addCommentButton)
        self.commentActionLayout.addWidget(self.editCommentButton)
        self.commentActionLayout.addWidget(self.deleteCommentButton)
        self.commentsLayout.addLayout(self.commentActionLayout)

        self.commentsTableWidget = QTableWidget()
        self.commentsTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.commentsTableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.commentsLayout.addWidget(self.commentsTableWidget)
        self.splitter.addWidget(self.commentsWidget)

        self.layout.addWidget(self.splitter)
        self.splitter.setSizes([300, 200])  # Initial sizes for post and comment sections

        self.load_posts_data()

    def load_table_data(self, table_widget, data, fields_config):
        table_widget.clearContents()
        table_widget.setRowCount(0)
        if data is None: return False  # Error already handled by caller
        if not data: return True  # No data is not an error here

        headers = [cfg["key"] for cfg in fields_config]
        header_labels = [cfg["label"] for cfg in fields_config]
        table_widget.setColumnCount(len(header_labels))
        table_widget.setHorizontalHeaderLabels(header_labels)

        for row_idx, record in enumerate(data):
            table_widget.insertRow(row_idx)
            for col_idx, key in enumerate(headers):
                item_value = str(record.get(key, ''))
                table_widget.setItem(row_idx, col_idx, QTableWidgetItem(item_value))
        table_widget.resizeColumnsToContents()
        return True

    def load_posts_data(self):
        posts_data = self.db.admin_get_all_posts()
        if posts_data is None:
            QMessageBox.critical(self, "Error", "Failed to load posts data.")
            return
        self.load_table_data(self.postsTableWidget, posts_data, POST_FIELDS_CONFIG)
        self.commentsTableWidget.clearContents()  # Clear comments when posts are reloaded
        self.commentsTableWidget.setRowCount(0)
        self.current_selected_post_id = None

    @Slot()
    def on_post_selected(self):
        selected_rows = self.postsTableWidget.selectionModel().selectedRows()
        if not selected_rows:
            self.current_selected_post_id = None
            self.commentsTableWidget.clearContents()
            self.commentsTableWidget.setRowCount(0)
            return

        row_idx = selected_rows[0].row()
        try:
            id_col_idx = [cfg["key"] for cfg in POST_FIELDS_CONFIG].index("id")
            post_id_item = self.postsTableWidget.item(row_idx, id_col_idx)
            self.current_selected_post_id = int(post_id_item.text()) if post_id_item else None
        except (ValueError, IndexError):
            self.current_selected_post_id = None

        self.load_comments_for_selected_post()

    def load_comments_for_selected_post(self):
        if self.current_selected_post_id is None:
            self.commentsTableWidget.clearContents()
            self.commentsTableWidget.setRowCount(0)
            return

        comments_data = self.db.admin_get_comments_for_post(self.current_selected_post_id)
        if comments_data is None:
            QMessageBox.warning(self, "Warning",
                                f"Failed to load comments for post ID {self.current_selected_post_id}.")
            return
        self.load_table_data(self.commentsTableWidget, comments_data, COMMENT_FIELDS_CONFIG)

    def get_selected_item_data(self, table_widget, fields_config):
        selected_rows = table_widget.selectionModel().selectedRows()
        if not selected_rows: return None, None

        row_idx = selected_rows[0].row()
        record_data = {}
        record_id = None
        id_key = fields_config[0]["key"]  # Assuming first field is always 'id'

        for col_idx, field_cfg in enumerate(fields_config):
            key = field_cfg["key"]
            item = table_widget.item(row_idx, col_idx)
            value_str = item.text() if item else ""

            if field_cfg.get("type") == "int":
                try:
                    value = int(value_str)
                except ValueError:
                    value = 0
            elif field_cfg.get("type") == "textarea":  # QTextEdit content
                value = value_str  # Already string from table
            else:  # text
                value = value_str

            record_data[key] = value
            if key == id_key:  # Typically "id"
                record_id = value
        return record_id, record_data

    # --- Post CRUD ---
    def edit_post_item(self):
        post_id, current_data = self.get_selected_item_data(self.postsTableWidget, POST_FIELDS_CONFIG)
        if post_id is None:
            QMessageBox.warning(self, "Selection Error", "Please select a post to edit.")
            return

        dialog = BaseEditDialog("Edit Post", POST_FIELDS_CONFIG, data=current_data, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            updated_data = dialog.get_data()
            data_for_update = {k: v for k, v in updated_data.items() if
                               k not in ["id", "author_username", "post_time"]}  # Non-editable fields

            if self.db.admin_update_post(post_id, data_for_update):
                QMessageBox.information(self, "Success", "Post updated successfully.")
                self.load_posts_data()  # Reload all posts
            else:
                QMessageBox.critical(self, "Database Error", "Failed to update post.")

    def delete_post_item(self):
        post_id, _ = self.get_selected_item_data(self.postsTableWidget, POST_FIELDS_CONFIG)
        if post_id is None:
            QMessageBox.warning(self, "Selection Error", "Please select a post to delete.")
            return

        reply = QMessageBox.question(self, "Confirm Delete",
                                     f"Are you sure you want to delete post ID {post_id} and all its comments?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            if self.db.admin_delete_post(post_id):
                QMessageBox.information(self, "Success", "Post deleted successfully.")
                self.load_posts_data()  # This will also clear comments for the deleted post
            else:
                QMessageBox.critical(self, "Database Error", "Failed to delete post.")

    # --- Comment CRUD ---
    def edit_comment_item(self):
        if self.current_selected_post_id is None:
            QMessageBox.warning(self, "Selection Error", "Please select a post first.")
            return
        comment_id, current_data = self.get_selected_item_data(self.commentsTableWidget, COMMENT_FIELDS_CONFIG)
        if comment_id is None:
            QMessageBox.warning(self, "Selection Error", "Please select a comment to edit.")
            return

        dialog = BaseEditDialog("Edit Comment", COMMENT_FIELDS_CONFIG, data=current_data, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            updated_data = dialog.get_data()
            # Only content is typically editable by admin for comments
            if 'content' in updated_data:
                if self.db.admin_update_comment(comment_id, updated_data['content']):
                    QMessageBox.information(self, "Success", "Comment updated successfully.")
                    self.load_comments_for_selected_post()
                else:
                    QMessageBox.critical(self, "Database Error", "Failed to update comment.")
            else:
                QMessageBox.warning(self, "Input Error", "No content to update.")

    def delete_comment_item(self):
        if self.current_selected_post_id is None:
            QMessageBox.warning(self, "Selection Error", "Please select a post first.")
            return
        comment_id, _ = self.get_selected_item_data(self.commentsTableWidget, COMMENT_FIELDS_CONFIG)
        if comment_id is None:
            QMessageBox.warning(self, "Selection Error", "Please select a comment to delete.")
            return

        reply = QMessageBox.question(self, "Confirm Delete",
                                     f"Are you sure you want to delete comment ID {comment_id}?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            if self.db.admin_delete_comment(comment_id):
                QMessageBox.information(self, "Success", "Comment deleted successfully.")
                self.load_comments_for_selected_post()
            else:
                QMessageBox.critical(self, "Database Error", "Failed to delete comment.")

    def closeEvent(self, event):
        if self.db: self.db.close()
        super().closeEvent(event)