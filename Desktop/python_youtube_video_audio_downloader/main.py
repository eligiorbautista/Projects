from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import sys, os, time, webbrowser


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 613)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/youtube-logo-circle2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("selection-color:black;\n"
"selection-background-color:rgb(218, 218, 218);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 811, 611))
        self.frame_4.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setGeometry(QtCore.QRect(5, 5, 801, 601))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame {\n"
"    background-color:rgb(72, 72, 72)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 801, 31))
        self.frame_2.setStyleSheet("QFrame {\n"
"    background-color:rgb(49, 49, 49)\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_exit = QtWidgets.QPushButton(self.frame_2)
        self.btn_exit.setGeometry(QtCore.QRect(770, 0, 31, 31))
        font = QtGui.QFont()
        font.setFamily("TeamViewer15")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_exit.setStyleSheet("QPushButton {\n"
"    background-color:rgb(72, 72, 72);\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.btn_exit.setFlat(True)
        self.btn_exit.setObjectName("btn_exit")
        self.btn_min = QtWidgets.QPushButton(self.frame_2)
        self.btn_min.setGeometry(QtCore.QRect(740, 0, 31, 31))
        font = QtGui.QFont()
        font.setFamily("TeamViewer15")
        font.setPointSize(22)
        self.btn_min.setFont(font)
        self.btn_min.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_min.setStyleSheet("QPushButton {\n"
"    background-color:rgb(72, 72, 72);\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.btn_min.setFlat(True)
        self.btn_min.setObjectName("btn_min")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 135, 801, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(290, 10, 221, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/icon-white-red.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(13, 210, 781, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.input_url = QtWidgets.QLineEdit(self.frame)
        self.input_url.setGeometry(QtCore.QRect(150, 270, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.input_url.setFont(font)
        self.input_url.setStyleSheet("\n"
"    padding:5px;\n"
"    border: 3px solid black;\n"
"    background-color:white;\n"
"    border-width: 3px 0px 3px 3px;\n"
"")
        self.input_url.setObjectName("input_url")
        self.combo_file_type = QtWidgets.QComboBox(self.frame)
        self.combo_file_type.setGeometry(QtCore.QRect(150, 330, 161, 37))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.combo_file_type.setFont(font)
        self.combo_file_type.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.combo_file_type.setStyleSheet("QComboBox {\n"
"    padding:5px;\n"
"    border: 2px solid black;\n"
"    background-color:white;\n"
"}\n"
"\n"
"QListView {\n"
"    background-color:white;\n"
"}")
        self.combo_file_type.setObjectName("combo_file_type")
        self.combo_file_type.addItem("")
        self.combo_file_type.addItem("")
        self.combo_file_type.addItem("")
        self.btn_dl = QtWidgets.QPushButton(self.frame)
        self.btn_dl.setGeometry(QtCore.QRect(520, 330, 141, 37))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.btn_dl.setFont(font)
        self.btn_dl.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_dl.setStyleSheet("QPushButton {\n"
"    background-color:rgb(72, 72, 72);\n"
"    border: 2px solid white;\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color:rgb(255, 0, 0);\n"
"    border: 2px solid rgb(255, 0, 0);\n"
"    color:white;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/download-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_dl.setIcon(icon1)
        self.btn_dl.setIconSize(QtCore.QSize(30, 20))
        self.btn_dl.setObjectName("btn_dl")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 566, 801, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btn_open_dl = QtWidgets.QPushButton(self.frame)
        self.btn_open_dl.setGeometry(QtCore.QRect(323, 330, 181, 37))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.btn_open_dl.setFont(font)
        self.btn_open_dl.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_open_dl.setStyleSheet("QPushButton {\n"
"    background-color:rgb(72, 72, 72);\n"
"    border: 2px solid white;\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color:rgb(255, 0, 0);\n"
"    border: 2px solid rgb(255, 0, 0);\n"
"    color:white;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/folder-icon-30.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_open_dl.setIcon(icon2)
        self.btn_open_dl.setObjectName("btn_open_dl")
        self.btn_clear = QtWidgets.QPushButton(self.frame)
        self.btn_clear.setGeometry(QtCore.QRect(620, 270, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_clear.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 255, 255);\n"
"    color:rgb(255, 255, 255);\n"
"    border: 3px solid black;\n"
"    border-width: 3px 3px 3px 0px;\n"
"    padding-bottom:5px;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"    background-color:rgb(255, 255, 255);\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.btn_clear.setFlat(True)
        self.btn_clear.setObjectName("btn_clear")
        self.btn_help = QtWidgets.QPushButton(self.frame)
        self.btn_help.setGeometry(QtCore.QRect(20, 555, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(11)
        self.btn_help.setFont(font)
        self.btn_help.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_help.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 0, 0);\n"
"    border: 2px solid rgb(255, 0, 0);\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color:rgb(255, 71, 65);\n"
"    border: 2px solid rgb(255, 0, 0);\n"
"    color:white;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/question.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_help.setIcon(icon3)
        self.btn_help.setIconSize(QtCore.QSize(18, 18))
        self.btn_help.setObjectName("btn_help")
        self.btn_open_youtube = QtWidgets.QPushButton(self.frame)
        self.btn_open_youtube.setGeometry(QtCore.QRect(650, 555, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(11)
        self.btn_open_youtube.setFont(font)
        self.btn_open_youtube.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_open_youtube.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 0, 0);\n"
"    border: 2px solid rgb(255, 0, 0);\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color:rgb(255, 71, 65);\n"
"    border: 2px solid rgb(255, 0, 0);\n"
"    color:white;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/youtube-logo-white.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_open_youtube.setIcon(icon4)
        self.btn_open_youtube.setIconSize(QtCore.QSize(18, 18))
        self.btn_open_youtube.setText('Open YouTube')
        self.btn_open_youtube.setObjectName("btn_open_youtube")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint) 
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.btn_exit.clicked.connect(lambda: MainWindow.close())
        self.btn_min.clicked.connect(lambda: MainWindow.showMinimized())
        self.combo_file_type.currentTextChanged.connect(self.Validation)
        self.input_url.textChanged.connect(self.Validation)
        self.btn_dl.setEnabled(False)
        self.btn_open_dl.clicked.connect(self.OpenDownloads)
        self.btn_clear.setEnabled(False)
        self.btn_clear.clicked.connect(lambda:self.input_url.clear())
        self.CheckDownloads()
        self.btn_dl.clicked.connect(self.ExecuteDownload)
        self.btn_open_youtube.clicked.connect(lambda: webbrowser.open('https://www.youtube.com', new=1))
        self.btn_help.clicked.connect(lambda:os.startfile('help\Tutorial.mp4'))

    def CheckDownloads(self):
      if os.path.isdir('Downloads'):
        ...
      else:
        os.makedirs('Downloads')

    def OpenDownloads(self):
      # Open Downloads Folder
      os.startfile('Downloads')

    def Validation(self):
      if len(self.input_url.text()) != 0:
        self.btn_clear.setEnabled(True)
        self.btn_clear.setStyleSheet('background-color:rgb(255, 255, 255);color:rgb(173, 173, 173);border: 3px solid black;border-width: 3px 3px 3px 0px;')
      else:
        self.btn_clear.setEnabled(False)
        self.btn_clear.setStyleSheet('background-color:rgb(255, 255, 255);color:rgb(255, 255, 255);border: 3px solid black;border-width: 3px 3px 3px 0px;')

      if self.combo_file_type.currentText() != 'Select file type' and len(self.input_url.text()) != 0:
        self.btn_dl.setEnabled(True)
      else:
        self.btn_dl.setEnabled(False)

    def ExecuteDownload(self):
          self.msg = QMessageBox()
          self.msg.setWindowTitle('Youtube Video & Audio Downloader')
          self.msg.setWindowIcon(QtGui.QIcon('images/youtube-logo-circle.ico'))
          self.msg.setIcon(QMessageBox.Icon.Information)
          self.msg.setText('Downloading... Please wait.                       ')
          self.msg.setStandardButtons(QMessageBox.StandardButton.Close)
          self.msg.exec()  

          from pytube import YouTube, exceptions
          # Link of the video to download
          url = self.input_url.text()
          try:

            youtube_video = YouTube(url) # Put the url here

            # Note : Progressive streams have the video and audio in a single file, 
            # but typically do not provide the highest quality media
            # Filter out all the files with "mp4" extension or audio
            if self.combo_file_type.currentText() == 'Video':
              youtube_video.streams.filter(progressive=True)
            if self.combo_file_type.currentText() == 'Audio':
              youtube_video.streams.filter(only_audio=True)
            
            # Get the video with the extension and resolution
            # passed in the get() function
            youtube_video = youtube_video.streams.get_highest_resolution()
            output_file = youtube_video.download(r'Downloads') # Put the save path here and download the video

            if self.combo_file_type.currentText() == 'Video':
              filename, exe = os.path.splitext(output_file)
              new_file = filename + '_video' +'.mp4'
              os.rename(output_file, new_file)

            if self.combo_file_type.currentText() == 'Audio':
              filename, exe = os.path.splitext(output_file)
              new_file = filename + '_audio' + '.mp3'
              os.rename(output_file, new_file)

            self.msg = QMessageBox()
            self.msg.setWindowTitle('Youtube Video & Audio Downloader')
            self.msg.setWindowIcon(QtGui.QIcon('images/youtube-logo-circle.ico'))
            self.msg.setIcon(QMessageBox.Icon.Information)
            self.msg.setText('Download Success                            ')
            self.msg.exec()   

          except(FileExistsError):
            self.msg = QMessageBox()
            self.msg.setWindowTitle('Youtube Video & Audio Downloader')
            self.msg.setStyleSheet('background-color:rgb(218, 218, 218) color:rgb(0,0,0)')
            self.msg.setWindowIcon(QtGui.QIcon('images/youtube-logo-circle.ico'))
            self.msg.setIcon(QMessageBox.Icon.Warning)
            self.msg.setText('File already exists.                                                 ')
            self.msg.setInformativeText('Please check the download folder')
            self.msg.exec()
          
          except(exceptions.RegexMatchError):
            self.msg = QMessageBox()
            self.msg.setWindowTitle('Youtube Video & Audio Downloader')
            self.msg.setStyleSheet('background-color:rgb(218, 218, 218) color:rgb(0,0,0)')
            self.msg.setWindowIcon(QtGui.QIcon('images/youtube-logo-circle.ico'))
            self.msg.setIcon(QMessageBox.Icon.Critical)
            self.msg.setText('Invalid Link                                              ')
            self.msg.setInformativeText('Please check your link and try again')
            self.msg.exec()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Video & Audio Downloader"))
        self.btn_exit.setText(_translate("MainWindow", "x"))
        self.btn_min.setText(_translate("MainWindow", "-"))
        self.label_2.setText(_translate("MainWindow", "Video / Audio Downloader"))
        self.input_url.setPlaceholderText(_translate("MainWindow", "Place your video link here"))
        self.combo_file_type.setItemText(0, _translate("MainWindow", "Select file type"))
        self.combo_file_type.setItemText(1, _translate("MainWindow", "Video"))
        self.combo_file_type.setItemText(2, _translate("MainWindow", "Audio"))
        self.btn_dl.setText(_translate("MainWindow", " Download "))
        self.label_3.setText(_translate("MainWindow", "© 2022 Eli Bautista Softwares"))
        self.btn_open_dl.setText(_translate("MainWindow", " Open Downloads"))
        self.btn_clear.setText(_translate("MainWindow", "x"))
        self.btn_help.setText(_translate("MainWindow", "How it works ?"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
