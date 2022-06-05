import sys
import platform

#import function_ui
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

#Функции, файлы
from modules_app import *








class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()


        self.ui.pushButton.clicked.connect(lambda: UIFunctions.yes())
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.btn_page_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))

        self.ui.pushButton_3.clicked.connect(lambda: self.showMinimized())

        self.ui.btn_page_1.clicked.connect(lambda: self.ui.label_5.setText('Браузеры'))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.label_5.setText('Редакторы'))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.label_5.setText('Утилиты'))

        self.ui.label_3.setFont(QFont('Montserrat',14 , QtGui.QFont.Bold))
        self.ui.label_8.setFont(QFont('Montserrat', 14, QtGui.QFont.Bold))
        self.ui.label_11.setFont(QFont('Montserrat', 14, QtGui.QFont.Bold))
        self.ui.label_13.setFont(QFont('Montserrat', 14, QtGui.QFont.Bold))
        self.ui.label_15.setFont(QFont('Montserrat', 14, QtGui.QFont.Bold))

        #self.ui.label_3.setText('Google Chrome  ')
        #self.ui.label_8.setText('Firefox         ')
        #self.ui.label_11.setText('Opera          ')
        #self.ui.label_13.setText('Yandex         ')
        #self.ui.label_15.setText('Opera Gx       ')

        self.ui.frame_left_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.ui.frame_left_menu.setMaximumSize(QtCore.QSize(0, 16777215))

        self.ui.pushButton.setGeometry(QtCore.QRect(910, 0, 41, 41))
        self.ui.pushButton_3.setGeometry(QtCore.QRect(870, 0, 41, 41))


        #-------------------------ИКОНКИ-------------------------
        #self.ui.btn_page_1.setIcon(QtGui.QIcon('chrome_browser_logo_icon_153007.png'))
        self.ui.Btn_Toggle.setIcon(QtGui.QIcon('hamburger_button_menu_icon_155296.png'))
        self.ui.label_2.setPixmap(QtGui.QPixmap('googlechrome_103832.png'))
        #--------------------------------------------------------
        self.ui.btn_page_1.setFont(QFont('Montserrat', 14))
        self.ui.btn_page_2.setFont(QFont('Montserrat', 14))
        self.ui.btn_page_3.setFont(QFont('Montserrat', 14))
        self.ui.btn_page_4.setFont(QFont('Montserrat', 14))
        self.ui.btn_page_5.setFont(QFont('Montserrat', 14))

        self.ui.Btn_Toggle.setFont(QFont('Montserrat', 14))
        self.ui.pushButton_2.setFont(QFont('Montserrat',16 , QtGui.QFont.Bold))
        self.ui.pushButton_4.setFont(QFont('Montserrat', 16, QtGui.QFont.Bold))
        self.ui.pushButton.setFont(QFont('Montserrat', 12))
        self.ui.pushButton_3.setFont(QFont('Montserrat', 14))

        self.ui.label_5.setFont(QFont('Montserrat', 13))

    def mousePressEvent(self, event):
        # Если нажата левая кнопка мыши
        if event.button() == QtCore.Qt.LeftButton:
            # получаем координаты окна относительно экрана
            x_main = self.geometry().x()
            y_main = self.geometry().y()
            # получаем координаты курсора относительно окна нашей программы
            cursor_x = QtGui.QCursor.pos().x()
            cursor_y = QtGui.QCursor.pos().y()
            # проверяем условием позицию курсора на нужной области программы(у нас это верхний бар)
            # если всё ок - перемещаем
            # иначе игнорируем
            if x_main <= cursor_x <= x_main + self.geometry().width():
                if y_main <= cursor_y <= y_main + self.ui.frame_top.geometry().height():
                    self.old_pos = event.pos()
                else:
                    self.old_pos = None
        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    # вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())