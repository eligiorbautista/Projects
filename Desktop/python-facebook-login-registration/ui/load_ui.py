from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6 import uic, QtCore, QtGui
import os, shutil

class Ui_LoadUI(QWidget):
  def __init__(self):
    super(Ui_LoadUI,self).__init__()
    uic.loadUi('main.ui', self)

app = QApplication([])
win = Ui_LoadUI()
win.show()

app.exec()