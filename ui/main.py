from PySide2.QtWidgets import QWidget, QMainWindow
from PySide2.QtGui import QPalette, Qt, QCloseEvent, QMouseEvent
from PySide2.QtCore import QTimer

import random

from ui.main_ui import Ui_MainWindow
from ui.card import Card

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle("cardnorm")
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.central.setAutoFillBackground(True)

        self.mousePos = (0, 0)
        self.isPressed = False

        self.cards = []

        self.btn_create.clicked.connect(self.create_cards)

    def create_cards(self):
        c = 0
        for shape in ["♥", "♠", "♣", "◈"]:
            for num in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
                t = Card(shape, num)
                self.cards.append(t)
        random.shuffle(self.cards)

        for card in self.cards:
            card.move(self.pos().x() + c, self.pos().y() + c)
            c += 5
            card.show()

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

    def closeEvent(self, event: QCloseEvent):
        del self.cards





