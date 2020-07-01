# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 289)
        MainWindow.setStyleSheet(u"#central {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"}")
        self.central = QWidget(MainWindow)
        self.central.setObjectName(u"central")
        self.centralLayout = QGridLayout(self.central)
        self.centralLayout.setObjectName(u"centralLayout")
        self.banner = QLabel(self.central)
        self.banner.setObjectName(u"banner")
        font = QFont()
        font.setFamily(u"\ub3cb\uc6c0")
        font.setPointSize(72)
        self.banner.setFont(font)
        self.banner.setAlignment(Qt.AlignCenter)

        self.centralLayout.addWidget(self.banner, 0, 0, 1, 1)

        self.btn_create = QPushButton(self.central)
        self.btn_create.setObjectName(u"btn_create")
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(32)
        self.btn_create.setFont(font1)
        self.btn_create.setStyleSheet(u"QPushButton {\n"
"	padding-top: 24px;\n"
"	padding-bottom: 24px;\n"
"}")

        self.centralLayout.addWidget(self.btn_create, 0, 1, 1, 1)

        self.centralLayout.setColumnStretch(0, 3)
        self.centralLayout.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.central)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.banner.setText(QCoreApplication.translate("MainWindow", u"\uce74\ub4dc", None))
        self.btn_create.setText(QCoreApplication.translate("MainWindow", u"\uc0dd\uc131", None))
    # retranslateUi

