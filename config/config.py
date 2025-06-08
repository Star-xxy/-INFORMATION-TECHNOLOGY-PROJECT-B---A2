import yaml
from pydantic import BaseModel
# coding:utf-8
import datetime

from qfluentwidgets import (qconfig, QConfig, ConfigItem, BoolValidator, ColorConfigItem, FolderValidator, Theme)


class Config(QConfig):
    user = ConfigItem("User", "user", '123')
    password = ConfigItem("User", "password", '123')
    save_password = ConfigItem("MainWindow", "save_password", True, BoolValidator())

    open_fold = ConfigItem("Yolo", "open_fold", "image_test", FolderValidator())
    ip = ConfigItem("Yolo", "ip", "rtsp://admin:admin888@192.168.1.2:555")
    iou = ConfigItem("Yolo", "iou", 0.35)
    conf = ConfigItem("Yolo", "conf", 0.75)
    delay = ConfigItem("Yolo", "delay", 0)
    is_save_results = ConfigItem("Yolo", "save", True, BoolValidator())
    save_path = ConfigItem("Yolo", "save_path", "save_dir", FolderValidator())


YEAR = datetime.datetime.now().year
cfg = Config()
cfg.themeMode.value = Theme.LIGHT
qconfig.load('config/config.json', cfg)