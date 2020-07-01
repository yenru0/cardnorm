from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QMouseEvent
from PySide2.QtCore import QTimer, Qt

from ui.card_ui import Ui_Card


class Card(QWidget, Ui_Card):
    def __init__(self, shape, number, parent=None,):
        super().__init__(parent=parent, f=Qt.FramelessWindowHint)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.shape.setText(shape)
        self.number_top.setText(str(number))
        self.number_bottom.setText(str(number))

        self.mousePos = (0, 0)
        self.isPressed = False



    def mousePressEvent(self, event: QMouseEvent):
        self.isPressed = True
        self.mousePos = event.x(), event.y()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.isPressed = False

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.RightButton:
            self.close()
        elif event.buttons() & Qt.MiddleButton:
            pass

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.isPressed: self.move(event.globalX() - self.mousePos[0], event.globalY() - self.mousePos[1])