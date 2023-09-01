from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6 import QtCore
from PyQt6 import uic

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        uic.loadUi('CALCULATOR_UI.ui',self)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)


app = QApplication([])
window = Window()
window.show()
app.exec()
