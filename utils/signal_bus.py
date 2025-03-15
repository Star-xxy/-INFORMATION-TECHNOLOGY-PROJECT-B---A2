from typing import Any

from PySide6.QtCore import QObject, Signal


class SignalBus(QObject):
    """ Signal bus """
    switchToSampleCard = Signal(Any)


signalBus = SignalBus()