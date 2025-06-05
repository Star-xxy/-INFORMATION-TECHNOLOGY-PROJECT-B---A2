# widget_post_all.py

import sqlite3  # This import is not actively used by PostgreSQL logic, can be removed if not needed elsewhere
import sys

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QUrl  # Removed unused QRectF, QPropertyAnimation, QEasingCurve, QTimer, QTime
from PySide6.QtGui import QIcon, QImage, \
    QPixmap  # Removed unused QPainter, QBrush, QColor, QDesktopServices, QPainterPath, QLinearGradient
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QListWidgetItem,
                               QMessageBox)  # Removed unused QStackedWidget, QHBoxLayout, QFileDialog

# qfluentwidgets components are used in blog_card.py, so keep if Form uses them.
# from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox as FluentMessageBox,
# isDarkTheme, setThemeColor)

from ui.post_all import Ui_Frame
from ui.blog_card import Ui_Form  # This UI class is used by WidgetCard
from ui.widget_post_detail import WidgetPostDetail

from utils.database import Database, DB_HOST, DB_NAME, DB_USER, DB_PASSWORD  # Ensure correct import


class WidgetCard(QWidget, Ui_Form):  # Ui_Form is from ui.blog_card
    def __init__(self, card_id, author_username, image_path, text, likes, favorites, date,
                 db_instance: Database, current_user_id: int, current_username: str,
                 parent=None):  # Added db_instance and current_user_id
        super().__init__(parent)
        self.setupUi(self)  # Sets up UI from blog_card.py

        self.card_id = card_id
        self.author_username = author_username  # Store author of the post
        self.likes = likes
        self.favorites = favorites
        self.db = db_instance  # Use passed DB instance
        self.current_user_id = current_user_id
        self.current_username = current_username

        # Set image
        effective_image_path = image_path if image_path and image_path.strip() else 'resource/images/default_image.png'  # Ensure your default image exists
        image = QImage(effective_image_path)
        if image.isNull():  # Fallback if image loading fails
            image = QImage('resource/images/default_image.png')

        # Calculate target size for ImageLabel if available, otherwise default
        target_size = self.ImageLabel.size() if not self.ImageLabel.size().isEmpty() else QSize(180, 180)
        resized_image = image.scaled(target_size, Qt.AspectRatioMode.KeepAspectRatio,
                                     Qt.TransformationMode.SmoothTransformation)
        self.ImageLabel.setImage(resized_image)

        # Set text content
        self.BodyLabel.setText(self.author_username)  # Author of the post
        self.BodyLabel_2.setText(text)  # Post content
        self.PushButton.setText(f'Like ({likes})')
        self.PushButton_2.setText(f'Favorite ({favorites})')

        if date:
            self.CaptionLabel.setText(date)

        # Connect buttons
        self.PushButton.clicked.connect(self.like_card)  # Like button
        self.PushButton_2.clicked.connect(self.favorite_card)  # Favorite button
        self.PushButton_3.clicked.connect(self.handle_add_friend_action)  # Add Friend button

        self.update_add_friend_button_state()

        # widget_post_all.py (inside WidgetCard.update_add_friend_button_state)

    def update_add_friend_button_state(self):
        if not self.current_user_id or not self.author_username:
            self.PushButton_3.setVisible(False)
            return

        if self.author_username == self.current_username:
            self.PushButton_3.setText("It's you!")
            self.PushButton_3.setEnabled(False)
            self.PushButton_3.setVisible(True)
        else:
            # Use the new are_friends method
            if self.db.are_friends(self.current_user_id, self.author_username):
                self.PushButton_3.setText("Friends")
                self.PushButton_3.setEnabled(False)
            else:
                self.PushButton_3.setText("Add Friend")
                self.PushButton_3.setEnabled(True)
            self.PushButton_3.setVisible(True)
    def handle_add_friend_action(self):
        if not self.current_user_id:
            QMessageBox.warning(self, "Login Required", "You need to be logged in to add friends.")
            return
        if not self.author_username or self.author_username == self.current_username:
            return  # Should be handled by button state, but as a safeguard

        success, message = self.db.add_friend(self.current_user_id, self.author_username)

        if success:
            QMessageBox.information(self, "Friend Added", message)
            self.PushButton_3.setText("Friends")  # Or a more dynamic update from DB
            self.PushButton_3.setEnabled(False)
        else:
            QMessageBox.warning(self, "Add Friend Failed", message)
            # If message indicates "already friends", update button too
            if "already exists" in message or "already friends" in message:  # Adapt based on actual message
                self.PushButton_3.setText("Friends")
                self.PushButton_3.setEnabled(False)

    def like_card(self):
        self.likes += 1
        self.PushButton.setText(f"Like ({self.likes})")
        self.update_interaction_in_db()

    def favorite_card(self):
        self.favorites += 1
        self.PushButton_2.setText(f"Favorite ({self.favorites})")
        self.update_interaction_in_db()

    def update_interaction_in_db(self):
        """Updates likes and favorites in the database using PostgreSQL."""
        query = "UPDATE posts SET likes = %s, favorites = %s WHERE id = %s"
        params = (self.likes, self.favorites, self.card_id)

        # self.db._execute_query handles commit and errors internally based on its design
        # It returns None on successful commit without fetch, or query result, or None on error.
        # We might need a clearer success/failure indicator from _execute_query for non-fetch commits.
        # For now, we assume it works if no major error is logged by _execute_query.
        result = self.db._execute_query(query, params, commit=True)

        # A more robust check would be based on what _execute_query returns for successful DML
        # if result is None and an error was printed by _execute_query, it failed.
        # If the Database class's _execute_query returns, say, True on successful commit:
        # if not result:
        #     print(f"Failed to update likes/favorites for post ID {self.card_id}")
        # else:
        #     print(f"Updated likes/favorites for post ID {self.card_id}")
        # For now, let's assume the operation is attempted.


class WidgetPostAll(QFrame, Ui_Frame):  # Ui_Frame is from ui.post_all
    def __init__(self, name: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(name)
        self.setupUi(self)  # Sets up UI from post_all.py
        self.db = Database(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)  # Central DB instance for this widget

        self.current_user_id = None  # Store ID of the logged-in user
        self.current_username = None  # Store username of the logged-in user

        self.listWidget.itemClicked.connect(self.show_details)
        self.init_ui_placeholders()  # Renamed for clarity
        self.load_cards()

    def set_user_context(self, user_info: dict):
        """Receives user information from MainWindow."""
        if user_info:
            self.current_user_id = user_info.get('id')
            self.current_username = user_info.get('username')
            # self.user_name is used by WidgetPostDetail, ensure it's set
            self.user_name = self.current_username  # Keep self.user_name if WidgetPostDetail depends on it
            # print(f"WidgetPostAll context set: User ID {self.current_user_id}, Username {self.current_username}")
        else:
            self.current_user_id = None
            self.current_username = None
            self.user_name = None

        # Reload cards if user context changes, as "Add Friend" button state might depend on it
        self.load_cards()

    def init_ui_placeholders(self):
        """Initializes top user info placeholders. This should ideally be dynamic or removed if not used."""
        # This method fetches generic users. If it's for actual friend suggestions or activity,
        # it needs to be more context-aware or use the current logged-in user's data.
        # For now, keeping its original logic as a placeholder.
        users_to_display = []
        try:
            # Using _execute_query which handles the PostgreSQL connection
            users_to_display = self.db._execute_query(
                "SELECT username, training_time FROM users LIMIT 3",
                fetch='all'
            )
            if users_to_display is None: users_to_display = []  # Handle query error

        except Exception as e:  # Catch any exception during DB access
            print(f"Database error in init_ui_placeholders: {e}")
            users_to_display = []  # Ensure it's an empty list on error

        # Update UI (ensure these labels exist in ui.post_all.Ui_Frame)
        labels_map = [
            (self.StrongBodyLabel_4, self.BodyLabel),
            (self.StrongBodyLabel_5, self.BodyLabel_3),
            (self.StrongBodyLabel_6, self.BodyLabel_2)
        ]
        image_labels = [self.ImageLabel, self.ImageLabel_2, self.ImageLabel_3]

        for i in range(3):
            if i < len(users_to_display) and users_to_display[i]:
                username, training_time = users_to_display[i]
                if labels_map[i][0]: labels_map[i][0].setText(username or "User")
                if labels_map[i][1]: labels_map[i][1].setText(f'Training duration: {training_time or 0} minutes')
            else:  # Clear if not enough users
                if labels_map[i][0]: labels_map[i][0].setText("User")
                if labels_map[i][1]: labels_map[i][1].setText("Training duration: N/A")

        # Set default avatars
        default_avatar_path = 'resource/images/icons/office-man.png'
        image = QImage(default_avatar_path)
        if not image.isNull():
            resized_image = image.scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio,
                                         Qt.TransformationMode.SmoothTransformation)
            for img_label in image_labels:
                if img_label: img_label.setImage(resized_image)

    def load_cards(self):
        """Loads all blog cards."""
        self.listWidget.clear()  # Clear existing items before loading new ones
        cards_data = self.get_cards_data_from_db()  # Renamed for clarity

        if not cards_data:
            # print("No blog posts found or error fetching posts.")
            # Optionally display a message in the UI if no posts are available
            return

        for card_data in cards_data:
            card = WidgetCard(
                card_id=card_data["id"],
                author_username=card_data["author_username"],  # Pass author's username
                image_path=card_data["image_url"],
                text=card_data["content"],
                likes=card_data["likes"],
                favorites=card_data["favorites"],
                date=card_data["post_time"],
                db_instance=self.db,  # Pass the DB instance
                current_user_id=self.current_user_id,  # Pass current user ID
                current_username=self.current_username,  # Pass current username
                parent=self  # Optional: for styling or context
            )
            item = QListWidgetItem()
            item.setSizeHint(card.sizeHint())  # Crucial for proper layout of custom widgets
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, card)

            # Store data for detail view if needed, though detail view now takes card_id
            item.setData(Qt.ItemDataRole.UserRole + 1, card_data["id"])  # Store post ID

    def get_cards_data_from_db(self):
        """Fetches all blog post data from the database."""
        try:
            # get_posts() returns a list of dictionaries or []
            return self.db.get_posts()
        except Exception as e:  # Catch any exception
            print(f"Database error in get_cards_data_from_db: {e}")
            return []

    def show_details(self, item: QListWidgetItem):
        # Retrieve the post ID stored in the item
        post_id = item.data(Qt.ItemDataRole.UserRole + 1)
        if post_id is None:
            print("Error: Could not retrieve post_id for detail view.")
            return

        # Fetch full post data again for the detail view to ensure it's up-to-date
        # Or pass all necessary initial data if preferred.
        # For now, WidgetPostDetail takes card_id, text, video_path.
        # We need to fetch this info or ensure it's available.

        # Simplification: Assuming WidgetPostDetail can fetch its own details if given card_id and db.
        # The original item.data(1) stored a tuple: (card_id, image_path, text, video_path)
        # Let's find the original post data for this card_id to pass to WidgetPostDetail
        original_post_data = None
        all_posts = self.db.get_posts()  # This could be cached if performance is an issue
        if all_posts:
            for post in all_posts:
                if post['id'] == post_id:
                    original_post_data = post
                    break

        if original_post_data:
            self.detail_window = WidgetPostDetail(
                current_username=self.current_username,  # Pass current logged-in username
                db_instance=self.db,
                card_id=original_post_data["id"],
                initial_content=original_post_data["content"],
                video_url=original_post_data["video_url"],
                image_url=original_post_data["image_url"],  # Pass image_url
                author_username=original_post_data["author_username"],  # Pass author
                post_time=original_post_data["post_time"]  # Pass post time
            )
            self.detail_window.show()
        else:
            QMessageBox.warning(self, "Error", f"Could not load details for post ID {post_id}.")

    def closeEvent(self, event):
        if self.db:
            self.db.close()  # Close DB connection when widget is closed
            print("WidgetPostAll: Database connection closed.")
        super().closeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)


    # from qfluentwidgets import setThemeColor, Theme, setTheme
    # setThemeColor('#0078d4')
    # setTheme(Theme.LIGHT) # Or Theme.DARK

    # --- For testing WidgetPostAll directly ---
    # Create a dummy MainWindow or pass dummy user_info
    class DummyMainWindow:
        def __init__(self):
            self.user_info = {'id': 1, 'username': 'test_user'}  # Example user


    # dummy_main_window = DummyMainWindow() # If needed for context

    w = WidgetPostAll('Blog Posts')
    # Simulate setting user context if running standalone
    # This would normally be done by the actual MainWindow after login
    test_user_info = {'id': 1, 'username': 'test_user_logged_in', 'points': 100}  # Example, ensure 'id' exists
    w.set_user_context(test_user_info)

    w.show()
    app.exec()