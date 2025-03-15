# coding: utf-8
from enum import Enum

from qfluentwidgets import StyleSheetBase, Theme, isDarkTheme, qconfig


class StyleSheet(StyleSheetBase, Enum):
    """ Style sheet  """

    TYPE_CARD = "type_card"
    WIDGET_HOME = 'widget_home'
    WIDGET_TABLE = 'widget_table'
    WIDGET_DETECT = 'widget_detect'
    WIDGET_CHART = 'widget_chart'

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f":/yolo/qss/{theme.value.lower()}/{self.value}.qss"
