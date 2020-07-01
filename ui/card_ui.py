# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Card(object):
    def setupUi(self, Card):
        if not Card.objectName():
            Card.setObjectName(u"Card")
        Card.resize(200, 300)
        Card.setStyleSheet(u".QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#shape {\n"
"border: 2px solid black;\n"
"}\n"
"")
        self.shape = QLabel(Card)
        self.shape.setObjectName(u"shape")
        self.shape.setGeometry(QRect(0, 0, 200, 300))
        font = QFont()
        font.setPointSize(96)
        self.shape.setFont(font)
        self.shape.setAlignment(Qt.AlignCenter)
        self.number_bottom = QLabel(Card)
        self.number_bottom.setObjectName(u"number_bottom")
        self.number_bottom.setGeometry(QRect(0, 0, 200, 300))
        font1 = QFont()
        font1.setFamily(u"\ubc14\ud0d5")
        font1.setPointSize(49)
        font1.setBold(True)
        font1.setWeight(75)
        self.number_bottom.setFont(font1)
        self.number_bottom.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.number_bottom.setIndent(-1)
        self.number_top = QLabel(Card)
        self.number_top.setObjectName(u"number_top")
        self.number_top.setGeometry(QRect(0, 0, 200, 300))
        self.number_top.setFont(font1)
        self.number_top.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.number_top.setIndent(-1)

        self.retranslateUi(Card)

        QMetaObject.connectSlotsByName(Card)
    # setupUi

    def retranslateUi(self, Card):
        Card.setWindowTitle(QCoreApplication.translate("Card", u"Card", None))
        self.shape.setText(QCoreApplication.translate("Card", u"\u2663", None))
        self.number_bottom.setText(QCoreApplication.translate("Card", u"7", None))
        self.number_top.setText(QCoreApplication.translate("Card", u"7", None))
    # retranslateUi

