#class UIFunctions(MainWindow):
#    def uiDefinitions(self):
#        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


def yes():
    quit()

def toggleMenu(self, maxWidth, enable):
    if enable:
        # GET WIDTH
        width = self.ui.frame_left_menu.width()
        maxExtend = maxWidth
        standard = 70
        # SET MAX WIDTH
        if width == 70:
            widthExtended = maxExtend
        else:
            widthExtended = standard
        # ANIMATION
        self.ui.btn_page_1.setText('Браузеры')
        self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        if width == 250:
            self.ui.btn_page_1.setText('Б...')
