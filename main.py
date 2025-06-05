# main.py
import base64
import time
from pathlib import Path
from PySide6.QtCore import QMutex, QSemaphore, QEvent, QUrl  # Added QUrl for potential use in other parts if needed
from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtGui import QImage, QPixmap, Qt, QIcon
from PySide6.QtCore import QTimer, QThread, Signal, QDateTime
from openai import OpenAI  # Ensure OpenAI client is imported

from qfluentwidgets import Dialog, InfoBarPosition, InfoBar, setTheme, Theme

from core import YoloPredictor  # Assuming this is part of your project
import numpy as np
import traceback
import sys
import cv2
import os

from tasks import TASK, INPUT_SOURCE  # Assuming these are part of your project
from config.config import cfg
from main_window import Window  # Window is MSFluentWindow


class MainWindow(Window):
    main2yolo_begin_sgl = Signal()
    input_source = None

    def __init__(self, user_info):
        super().__init__()
        self.user_info = user_info

        # Initialize OpenAI client - THIS IS KEPT
        self.client = OpenAI(
            api_key="sk-627a7f6f36e84ae5a90e69c96c130af4",  # Replace with your actual key or load from config
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

        self.init_ui()
        self.init_yolo()
        self.init_signal()
        self.init_config()

        self.update_user_info_on_all_interfaces(self.user_info)

    def init_config(self):
        self.change_model()
        # Ensure yolo_predict is initialized before accessing its attributes
        if hasattr(self, 'yolo_predict'):
            self.yolo_predict.task = TASK.pose
        else:
            print("Warning: yolo_predict not initialized before init_config")

    def init_ui(self):
        self.show()
        QApplication.processEvents()
        if hasattr(self, 'analyzeInterface') and self.analyzeInterface:
            self.analyzeInterface.progress_bar.setValue(0)
            image = QImage('resource/images/icons/office-man.png')
            resized_image = image.scaled(96, 96)
            self.analyzeInterface.AvatarWidget.setImage(resized_image)
            self.classesInterface.AvatarWidget_2.setImage(resized_image)

        if hasattr(self, 'userInterface') and self.userInterface:
            resized_image_user = QImage('resource/images/icons/office-man.png').scaled(96,
                                                                                       96)  # Use a different variable name or ensure scope
            self.userInterface.AvatarWidget.setImage(resized_image_user)

    def init_signal(self):
        if hasattr(self, 'analyzeInterface') and self.analyzeInterface:
            self.analyzeInterface.run_button.clicked.connect(self.run_or_continue)
            self.analyzeInterface.stop_button.clicked.connect(self.stop)
            self.analyzeInterface.ToolButton.clicked.connect(self.get_image)
            self.analyzeInterface.ToolButton_2.clicked.connect(self.get_video)
            self.analyzeInterface.ToolButton_3.clicked.connect(self.get_webcam)
            self.analyzeInterface.PrimaryToolButton.clicked.connect(self.analyzeInterface.run_button.click)
            if self.analyzeInterface.res_video:  # Check if widget exists
                self.analyzeInterface.res_video.installEventFilter(self)
            if self.analyzeInterface.pre_video:  # Check if widget exists
                self.analyzeInterface.pre_video.installEventFilter(self)

        if hasattr(self, 'userInterface') and self.userInterface:
            self.userInterface.refresh_button_2.clicked.connect(self.update_chart)
            self.userInterface.ComboBox_4.currentTextChanged.connect(self.update_chart)
            self.userInterface.ComboBox_5.currentTextChanged.connect(self.update_chart)
            self.userInterface.start_date.dateChanged.connect(self.update_chart)
            self.userInterface.end_date.dateChanged.connect(self.update_chart)
            self.update_chart()

        self.is_resizing = False
        self.resizing_timer = QTimer(self)
        self.resizing_timer.setInterval(500)
        self.resizing_timer.timeout.connect(self.on_timer_timeout)
        self.resizing_timer.start()

    def on_timer_timeout(self):
        self.is_resizing = False
        if hasattr(self, 'analyzeInterface') and hasattr(self.analyzeInterface,
                                                         'refresh_cards') and self.analyzeInterface.refresh_cards == True:
            self.refresh_cards()
            self.analyzeInterface.refresh_cards = False

    def refresh_cards(self):
        if hasattr(self, 'postsInterface') and self.postsInterface:
            self.postsInterface.load_cards()

    def init_yolo(self):
        self.select_model = 'yolov11n-pose.pt'
        self.task = TASK.pose  # Default task
        self.yolo_predict = YoloPredictor()
        self.yolo_predict.save_res = cfg.get(cfg.is_save_results)
        self.yolo_predict.save_dir = Path(cfg.get(cfg.save_path))
        self.yolo_thread = QThread()

        if hasattr(self, 'analyzeInterface') and self.analyzeInterface:
            self.yolo_predict.yolo2main_pre_img.connect(
                lambda x: self.show_image(x, self.analyzeInterface.pre_video, 'origin'))
            self.yolo_predict.yolo2main_res_img.connect(
                lambda x: self.show_image(x, self.analyzeInterface.res_video, 'img'))
            self.yolo_predict.yolo2main_progress.connect(lambda x: self.analyzeInterface.progress_bar.setValue(x))

        self.yolo_predict.yolo2main_stop.connect(self.stop)
        self.main2yolo_begin_sgl.connect(self.yolo_predict.run)
        self.yolo_predict.moveToThread(self.yolo_thread)

    def update_user_info_on_all_interfaces(self, info):
        self.user_info = info

        username = info.get('username', '')
        points = info.get('points', 0)

        if hasattr(self, 'analyzeInterface') and self.analyzeInterface:
            self.analyzeInterface.StrongBodyLabel.setText(str(username))
            self.analyzeInterface.BodyLabel_7.setText(str(info.get('training_days', 0)))
            self.analyzeInterface.BodyLabel_10.setText(str(info.get('training_time', 0)))
            self.analyzeInterface.BodyLabel_8.setText(str(info.get('level', 0)))
            self.analyzeInterface.BodyLabel_9.setText(str(points))
            if hasattr(self.analyzeInterface, 'user_name'):  # Check before assigning
                self.analyzeInterface.user_name = username

        if hasattr(self, 'userInterface') and self.userInterface:
            self.userInterface.user_info = info
            self.userInterface.update_user_info(info)

        # if hasattr(self, 'postsInterface') and self.postsInterface:
        #     if hasattr(self.postsInterface, 'user_name'):  # Check before assigning
        #         self.postsInterface.user_name = username

        if hasattr(self, 'postsInterface') and self.postsInterface:
            # Pass the full user_info dictionary to postsInterface
            if hasattr(self.postsInterface, 'set_user_context'):
                self.postsInterface.set_user_context(info)
            else: # Fallback if only username was set before
                self.postsInterface.user_name = username

        if hasattr(self, 'classesInterface') and self.classesInterface:
            self.classesInterface.set_user_context(info)

    def switchToSample(self, task):
        self.detect_page(task)

    def change_model(self):
        # Ensure yolo_predict is initialized
        if not hasattr(self, 'yolo_predict'):
            self.init_yolo()  # Or handle error appropriately
        self.yolo_predict.new_model_name = f"./models/pose/{self.select_model}"

    def detect_page(self, task):
        self.task = task
        if not hasattr(self, 'yolo_predict'): self.init_yolo()
        self.yolo_predict.task = self.task
        self.yolo_predict.new_model_name = f"./models/{self.task.folder}/{self.select_model}"

    def get_image(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Image', cfg.get(cfg.open_fold), "Picture File(*.jpg *.png *.jpeg)")
        if name and hasattr(self, 'analyzeInterface') and self.analyzeInterface:
            cfg.set(cfg.open_fold, os.path.dirname(name))
            self.input_source = INPUT_SOURCE.IMG
            if not hasattr(self, 'yolo_predict'): self.init_yolo()
            self.yolo_predict.source = name
            self.clear_canvas()
            self.stop()
            self.stackedWidget.setCurrentWidget(self.analyzeInterface)

    def get_video(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Video', cfg.get(cfg.open_fold),
                                              "Video File(*.gif *.mp4 *.mkv *.avi *.flv)")
        if name and hasattr(self, 'analyzeInterface') and self.analyzeInterface:
            cfg.set(cfg.open_fold, os.path.dirname(name))
            self.input_source = INPUT_SOURCE.VIDEO
            if not hasattr(self, 'yolo_predict'): self.init_yolo()
            self.yolo_predict.source = name
            self.stop()
            self.stackedWidget.setCurrentWidget(self.analyzeInterface)

    def get_webcam(self):
        if hasattr(self, 'analyzeInterface') and self.analyzeInterface:
            self.input_source = INPUT_SOURCE.WEBCAM
            if not hasattr(self, 'yolo_predict'): self.init_yolo()
            self.yolo_predict.source = 0
            if self.yolo_thread.isRunning():
                self.stop()
            self.stackedWidget.setCurrentWidget(self.analyzeInterface)

    def run_or_continue(self):
        if self.input_source and hasattr(self, 'analyzeInterface') and self.analyzeInterface:
            if not hasattr(self, 'yolo_predict'): self.init_yolo()

            # Allow 0 for webcam source
            is_source_invalid = not self.yolo_predict.source and self.yolo_predict.source != 0

            if is_source_invalid:
                self.analyzeInterface.run_button.setChecked(False)
                InfoBar.warning("No Input", "Please select an image, video, or webcam.", parent=self)
                return

            self.yolo_predict.stop_dtc = False
            if self.analyzeInterface.run_button.isChecked():
                self.yolo_predict.continue_dtc = True
                if not self.yolo_thread.isRunning():
                    self.yolo_thread.start()
                    self.main2yolo_begin_sgl.emit()
            else:
                self.yolo_predict.continue_dtc = False

    def clear_canvas(self):
        if hasattr(self, 'analyzeInterface') and self.analyzeInterface:
            if self.analyzeInterface.pre_video: self.analyzeInterface.pre_video.clear()
            if self.analyzeInterface.res_video: self.analyzeInterface.res_video.clear()
            if self.analyzeInterface.progress_bar: self.analyzeInterface.progress_bar.setValue(0)

    def stop(self):
        if hasattr(self, 'yolo_predict'):
            self.yolo_predict.stop_dtc = True

        if hasattr(self, 'yolo_thread') and self.yolo_thread.isRunning():
            self.yolo_thread.quit()
            self.yolo_thread.wait(1000)

        if hasattr(self, 'analyzeInterface') and self.analyzeInterface and self.analyzeInterface.run_button:
            self.analyzeInterface.run_button.setChecked(False)

        if self.input_source != INPUT_SOURCE.IMG or \
                (hasattr(self, 'yolo_predict') and not self.yolo_predict.stop_dtc):
            self.clear_canvas()

    # --- AI Related Methods - KEPT AS PER YOUR ORIGINAL ---
    def get_ai_responce(self, img_src):
        if not hasattr(self, 'client') or self.client is None:
            print("OpenAI client not initialized.")
            return "Error: AI client not configured."

        _, buffer = cv2.imencode('.jpg', img_src)
        image_base64 = base64.b64encode(buffer).decode('utf-8')
        image_to_base64 = f"data:image/jpeg;base64,{image_base64}"
        messages = [
            {
                "role": "system",
                "content": [{"type": "text", "text": "You are a yoga instructor assistant."}],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_to_base64
                        },
                    },
                    {
                        "type": "text",
                        "text": "Analyze the yoga pose in the image and provide feedback in three parts: "
                                "'Correct posture', 'User's posture', and 'Adjustment suggestions'. "
                                "Include the name of the yoga pose in the 'Correct posture' section, "
                                "formatted as 'known as [Sanskrit name]'. "
                                "Use English for the response and clearly label each section as '**Correct posture:** ', "
                                "'**User's posture:** ', and '**Adjustment suggestions:** ' followed by the description."
                    },
                ],
            },
        ]
        try:
            completion = self.client.chat.completions.create(
                model="qwen-omni-turbo",
                messages=messages,
                # modalities=["text"], # Note: 'modalities' might be specific to your endpoint/SDK version.
                # Standard OpenAI API does not use this parameter for chat completions.
                # Keeping it as it was in your original code.
                stream=True,
                stream_options={"include_usage": True}
            )

            full_response = ""
            for chunk in completion:
                if chunk.choices and chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
            return full_response
        except Exception as e:
            print(f"Error getting AI response: {e}")
            return f"Error communicating with AI: {e}"

    def split_response(self, response):
        parts = response.split('\n\n')
        response_dict = {
            "Correct posture": "N/A",
            "User's posture": "N/A",
            "Adjustment suggestions": "N/A"
        }
        if len(parts) >= 1:  # Handle cases where splitting doesn't yield 3 parts cleanly
            response_dict["Correct posture"] = parts[0].replace("**Correct posture:** ", "").strip()
        if len(parts) >= 2:
            response_dict["User's posture"] = parts[1].replace("**User's posture:** ", "").strip()
        if len(parts) >= 3:
            response_dict["Adjustment suggestions"] = parts[2].replace("**Adjustment suggestions:** ", "").strip()
            # You could also concatenate remaining parts if any, e.g. parts[2:] if more than 3 parts.

        # The "Pose name" extraction from your original code was not directly used for labels.
        # If you need it for other purposes, you can add it here.
        # For example:
        # pose_name = "Unknown"
        # if "known as" in response_dict["Correct posture"]:
        #     try: ... # your extraction logic ...
        #     except: pass
        # response_dict["Pose name"] = pose_name
        return response_dict

    # --- END AI Related Methods ---

    def show_image(self, img_src, label, flag):
        if self.is_resizing or label is None: return

        try:
            processed_img_src = None
            if isinstance(img_src, str) and flag == "path":
                processed_img_src = cv2.imdecode(np.fromfile(img_src, dtype=np.uint8), -1)
            elif isinstance(img_src, np.ndarray):  # Already a numpy array
                processed_img_src = img_src.copy()  # Work with a copy
            else:
                # print(f"Invalid img_src type: {type(img_src)} for show_image")
                return

            if processed_img_src is None or not hasattr(processed_img_src, 'shape') or len(processed_img_src.shape) < 3:
                return

            # --- AI Response part - KEPT AND UNCOMMENTED ---
            if flag == "origin" and self.input_source == INPUT_SOURCE.IMG and \
                    hasattr(self, 'analyzeInterface') and self.analyzeInterface and \
                    hasattr(self.analyzeInterface, 'BodyLabel_12'):  # Check if labels exist

                full_response = self.get_ai_responce(processed_img_src)  # Pass the processed image
                response_parts = self.split_response(full_response)

                self.analyzeInterface.BodyLabel_12.setText(response_parts.get("Correct posture", "N/A"))
                self.analyzeInterface.BodyLabel_13.setText(response_parts.get("User's posture", "N/A"))
                self.analyzeInterface.BodyLabel_14.setText(response_parts.get("Adjustment suggestions", "N/A"))
            # --- END AI Response part ---

            ih, iw, _ = processed_img_src.shape
            if ih == 0 or iw == 0: return

            w = label.width()
            h = label.height()
            if w == 0 or h == 0: return

            # Keep aspect ratio and resize
            img_resized = None
            if iw / ih > w / h:
                scal = w / iw
                nw = w
                nh = int(scal * ih)
                if nw > 0 and nh > 0:
                    img_resized = cv2.resize(processed_img_src, (nw, nh))
            else:
                scal = h / ih
                nw = int(scal * iw)
                nh = h
                if nw > 0 and nh > 0:
                    img_resized = cv2.resize(processed_img_src, (nw, nh))

            if img_resized is not None:
                frame = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
                q_img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3,
                               QImage.Format.Format_RGB888)
                label.setPixmap(QPixmap.fromImage(q_img))
            # else:
            # label.clear() # Or set a placeholder if resize failed

        except Exception as e:
            print(f"Error in show_image for {label.objectName() if label else 'None'}: {e}")
            traceback.print_exc()

    def update_chart(self):
        if hasattr(self, 'userInterface') and self.userInterface and hasattr(self.userInterface,
                                                                             'db') and self.userInterface.db:
            start_date = self.userInterface.start_date.getDate()
            end_date = self.userInterface.end_date.getDate()

            query_result = self.userInterface.db.query_activities_by_date_and_pose(start_date, end_date)
            if isinstance(query_result, str):
                InfoBar.warning("Chart Data Error", query_result, parent=self, duration=3000)
                return

            dates, counts_by_category, yoga_poses = query_result

            chart_type = self.userInterface.ComboBox_5.text()
            current_text = self.userInterface.ComboBox_4.currentText()

            if current_text == "By week":
                dates, counts_by_category = self.userInterface.aggregate_by_week(dates, counts_by_category)
            elif current_text == "By month":
                dates, counts_by_category = self.userInterface.aggregate_by_month(dates, counts_by_category)

            if dates:
                if chart_type == 'Bar chart':
                    self.userInterface.update_bar_chart(dates, yoga_poses, counts_by_category)
                elif chart_type == 'Line chart':
                    self.userInterface.update_line_chart(dates, yoga_poses, counts_by_category)
            else:
                InfoBar.info("No Data", "No activity data for selected criteria.", orient=Qt.Orientation.Horizontal,
                             isClosable=True, position=InfoBarPosition.BOTTOM_RIGHT, parent=self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.Resize:
            self.is_resizing = True
        return super().eventFilter(obj, event)

    def closeEvent(self, event):
        self.stop()

        # Cleanly close DB connections in child interfaces
        interfaces_with_db = ['classesInterface', 'userInterface', 'postsInterface',
                              'analyzeInterface']  # Add others if they have DB
        for interface_name in interfaces_with_db:
            if hasattr(self, interface_name):
                interface_instance = getattr(self, interface_name)
                if interface_instance and hasattr(interface_instance, 'db') and interface_instance.db:
                    print(f"Closing DB for {interface_name}")
                    interface_instance.db.close()
                    interface_instance.db = None  # Prevent further use

        w = Dialog('Exit', "Closing the software, please wait a moment.", self)
        w.setTitleBarVisible(False)
        w.yesButton.setEnabled(False)

        self.close_timer = QTimer(self)
        self.close_timer.setSingleShot(True)
        self.close_timer.timeout.connect(w.accept)
        self.close_timer.start(500)  # Shortened for quicker close

        if w.exec():
            event.accept()
        else:
            event.ignore()