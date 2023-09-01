from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt6 import uic, QtCore, QtGui
import sys, os

class Ui_YoutubeDownloader(QMainWindow):
    def __init__(self):
      super(Ui_YoutubeDownloader,self).__init__ ()
      uic.loadUi('main.ui',self)
      self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint) 
      self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)


app = QApplication(sys.argv)
window = Ui_YoutubeDownloader()
window.show()
sys.exit(app.exec())