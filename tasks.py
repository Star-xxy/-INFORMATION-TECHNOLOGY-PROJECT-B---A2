from enum import Enum


class TASK(Enum):
    detect = (0, "YOLO目标检测", "detect")
    classify = (1, "YOLO图像分类", "classify")
    segment = (2, "YOLO图像分割", "segment")
    track = (3, "YOLO目标跟踪", "track")
    pose = (4, "YOLO姿态检测", "pose")
    obb = (5, "YOLO旋转检测", "obb")

    def __init__(self, value, title, folder):
        self._value_ = value
        self.title = title
        self.folder = folder

    def __str__(self):
        return self.title

    def get_value(self):
        return self._value_

    def get_folder(self):
        return self.folder


class INPUT_SOURCE(Enum):
    IMG = 0
    VIDEO = 1
    WEBCAM = 2
    RTSP = 3

if __name__ == '__main__':

    for task in TASK:
        print(task.title)
