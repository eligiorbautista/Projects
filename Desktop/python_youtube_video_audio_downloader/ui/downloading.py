from PyQt6 import QtCore, QtGui, QtWidgets
import time


class Ui_Downloading(object):
    def setupUi(self, Downloading):
        Downloading.setObjectName("Downloading")
        Downloading.resize(400, 131)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/youtube-logo-circle2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Downloading.setWindowIcon(icon)
        Downloading.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.frame = QtWidgets.QFrame(Downloading)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 131))
        self.frame.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 381, 111))
        self.frame_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 48, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Downloading)
        QtCore.QMetaObject.connectSlotsByName(Downloading)


    def retranslateUi(self, Downloading):
        _translate = QtCore.QCoreApplication.translate
        Downloading.setWindowTitle(_translate("Downloading", "Youtube Video & Audio Downloader"))
        self.label.setText(_translate("Downloading", "Downloading... Please wait."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Downloading = QtWidgets.QWidget()
    ui = Ui_Downloading()
    ui.setupUi(Downloading)
    Downloading.show()
    sys.exit(app.exec())
