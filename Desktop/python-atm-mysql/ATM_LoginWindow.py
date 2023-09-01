from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(742, 512)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/credit-card.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Login.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 741, 511))
        self.frame_2.setStyleSheet("background-color:rgb(7, 44, 112)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(20, 20, 701, 471))
        self.frame.setStyleSheet("QFrame{background-color:rgb(11, 58, 151);border: 3px solid rgb(7, 44, 112)}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.btn_Minimize = QtWidgets.QPushButton(self.frame)
        self.btn_Minimize.setGeometry(QtCore.QRect(620, 0, 41, 38))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Minimize.setFont(font)
        self.btn_Minimize.setStyleSheet("background:none;border-radius: 16px;color:white")
        self.btn_Minimize.setFlat(True)
        self.btn_Minimize.setObjectName("btn_Minimize")
        self.btn_Exit = QtWidgets.QPushButton(self.frame)
        self.btn_Exit.setGeometry(QtCore.QRect(660, 0, 41, 38))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Exit.setFont(font)
        self.btn_Exit.setStyleSheet("background:none;border-radius: 16px;color:white")
        self.btn_Exit.setFlat(True)
        self.btn_Exit.setObjectName("btn_Exit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(320, 140, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;color:white")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(260, 140, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border:none;color:white")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("images/credit-card.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_ID = QtWidgets.QLabel(self.frame)
        self.label_ID.setGeometry(QtCore.QRect(20, 290, 55, 16))
        self.label_ID.setStyleSheet("background-color:rgb(11, 58, 151);color::rgb(11, 58, 151);border:none;")
        self.label_ID.setText("")
        self.label_ID.setObjectName("label_ID")
        self.lineEdit_CardID = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_CardID.setGeometry(QtCore.QRect(230, 200, 261, 31))
        self.lineEdit_CardID.setStyleSheet("border:2px solid black;background-color:white;color:black;padding:2px")
        self.lineEdit_CardID.setText("")
        self.lineEdit_CardID.setObjectName("lineEdit_CardID")
        self.lineEdit_Pin = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Pin.setGeometry(QtCore.QRect(230, 240, 261, 31))
        self.lineEdit_Pin.setStyleSheet("border:2px solid black;background-color:white;color:black;padding:2px")
        self.lineEdit_Pin.setText("")
        self.lineEdit_Pin.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_Pin.setObjectName("lineEdit_Pin")
        self.btn_GoCreateAccount = QtWidgets.QPushButton(self.frame)
        self.btn_GoCreateAccount.setGeometry(QtCore.QRect(230, 310, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_GoCreateAccount.setFont(font)
        self.btn_GoCreateAccount.setStyleSheet("background-color:rgb(11, 58, 151);color:rgb(1, 143, 250)")
        self.btn_GoCreateAccount.setFlat(True)
        self.btn_GoCreateAccount.setObjectName("btn_GoCreateAccount")
        self.btn_Login = QtWidgets.QPushButton(self.frame)
        self.btn_Login.setGeometry(QtCore.QRect(421, 275, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.btn_Login.setFont(font)
        self.btn_Login.setStyleSheet("background-color:rgb(44, 48, 61);color:white")
        self.btn_Login.setObjectName("btn_Login")
        self.passwordHideShow = QtWidgets.QPushButton(self.frame)
        self.passwordHideShow.setGeometry(QtCore.QRect(461, 242, 27, 27))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.passwordHideShow.setFont(font)
        self.passwordHideShow.setStyleSheet("background:none;color:black;")
        self.passwordHideShow.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/hidepw.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.passwordHideShow.setIcon(icon1)
        self.passwordHideShow.setIconSize(QtCore.QSize(16, 16))
        self.passwordHideShow.setCheckable(True)
        self.passwordHideShow.setFlat(True)
        self.passwordHideShow.setObjectName("passwordHideShow")
        Login.setCentralWidget(self.centralwidget)
        Login.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Login.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.btn_Exit.clicked.connect(Login.close)
        self.btn_Minimize.clicked.connect(Login.showMinimized)
        self.passwordHideShow.toggled.connect(self.ShowHidePw)
        self.btn_GoCreateAccount.clicked.connect(self.ShowRegistrationWindow)
        #self.lineEdit_Pin.editingFinished.connect(self.CheckAccountInDatabase)
        
        DATABASE = mysql.connector.connect(host='localhost',user='root',passwd='root')
        CURSOR = DATABASE.cursor()
        CURSOR.execute('CREATE DATABASE IF NOT EXISTS ATM_DB')

        self.btn_Login.clicked.connect(self.CheckAccountInDatabase)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)


    def ShowRegistrationWindow(self):
        from ATM_RegistrationWindow import Ui_Registration
        self.reg = QtWidgets.QMainWindow()
        self.ui = Ui_Registration()
        self.ui.setupUi(self.reg)
        self.reg.show()
    
    def CheckAccountInDatabase(self):
        CARD_ID = self.lineEdit_CardID.text()
        CARD_PIN = self.lineEdit_Pin.text()
        if len(CARD_ID) !=0 and len(CARD_PIN) != 0:
            try:
                DATABASE = mysql.connector.connect(host='localhost',user='root',passwd='root',database='ATM_DB')
                CURSOR = DATABASE.cursor()
                CURSOR.execute('CREATE TABLE IF NOT EXISTS ACCOUNT_TRANSACTIONS(CARD VARCHAR(60) NOT NULL,AMOUNT FLOAT NOT NULL ,TRANSACTION_TYPE VARCHAR(60) NOT NULL, DATETIME_ VARCHAR(60) NOT NULL)')

                CURSOR.execute(f'SELECT * FROM account_information')
                ACCOUNTS_CHECK = CURSOR.fetchall()
                ACCOUNTS_COUNT = 0
                for ACCOUNT_CHECK in ACCOUNTS_CHECK:
                    if CARD_ID == ACCOUNT_CHECK[0]:
                        ACCOUNTS_COUNT+=1
                        break


                if ACCOUNTS_COUNT == 0:
                    from PyQt6.QtWidgets import QMessageBox
                    self.message = QMessageBox()
                    self.message.setWindowIcon(QtGui.QIcon('images/credit-card.png'))
                    self.message.setWindowTitle('HS ATM')
                    self.message.setIcon(QMessageBox.Icon.Warning)
                    self.message.setText("Account doesn't exists")
                    self.message.show()

                CURSOR.execute(f'SELECT * FROM account_information WHERE CARD = "{CARD_ID}"')
                ACCOUNTS = CURSOR.fetchall()
                for ACCOUNT in ACCOUNTS:
                    if CARD_ID == ACCOUNT[0] and CARD_PIN == ACCOUNT[1]:
                        self.lineEdit_CardID.clear()
                        self.lineEdit_Pin.clear()
                        
                        from ATM_DashboardWindow import Ui_Dashboard
                        self.dashboard = QtWidgets.QMainWindow()
                        self.ui = Ui_Dashboard()
                        self.ui.setupUi(self.dashboard)
                        self.ui.label_User.setText(ACCOUNT[2])
                        self.ui.label_ID.setText(ACCOUNT[0])

                        DATABASE = mysql.connector.connect(host='localhost',user='root',passwd='root',database='ATM_DB')
                        CURSOR = DATABASE.cursor()
                        CURSOR.execute(f'SELECT * FROM account_balance WHERE CARD = "{CARD_ID}"')
                        ACCOUNTS = CURSOR.fetchall()
                        for ACCOUNT in ACCOUNTS:
                            converted_number = '{:,}'.format(ACCOUNT[1])
                            self.ui.label_Balance.setText(str(converted_number))
                        self.btn_Login.clicked.connect(lambda:Login.close())
                        self.dashboard.show()

                    else:
                        from PyQt6.QtWidgets import QMessageBox
                        self.message = QMessageBox()
                        self.message.setWindowIcon(QtGui.QIcon('images/credit-card.png'))
                        self.message.setWindowTitle('HS ATM')
                        self.message.setIcon(QMessageBox.Icon.Warning)
                        self.message.setText('Incorrect Username/Password. Please try again.')
                        self.message.show()
            except:
                    from PyQt6.QtWidgets import QMessageBox
                    self.message = QMessageBox()
                    self.message.setWindowIcon(QtGui.QIcon('images/credit-card.png'))
                    self.message.setWindowTitle('HS ATM')
                    self.message.setIcon(QMessageBox.Icon.Warning)
                    self.message.setText("Account doesn't exists")
                    self.message.show()


        else:
            from PyQt6.QtWidgets import QMessageBox
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon('images/credit-card.png'))
            self.message.setWindowTitle('HS ATM')
            self.message.setIcon(QMessageBox.Icon.NoIcon)
            self.message.setText('Please fill all the fields.')
            self.message.show()

    def ShowHidePw(self):
        if self.passwordHideShow.isChecked():
            self.passwordHideShow.setIcon(QtGui.QIcon('images/showpw.png'))
            self.lineEdit_Pin.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.passwordHideShow.setIcon(QtGui.QIcon('images/hidepw.png'))
            self.lineEdit_Pin.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)


    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "HS ATM Login"))
        self.btn_Minimize.setText(_translate("Login", "-"))
        self.btn_Exit.setText(_translate("Login", "x"))
        self.label.setText(_translate("Login", "HS ATM"))
        self.lineEdit_CardID.setPlaceholderText(_translate("Login", "Card ID"))
        self.lineEdit_Pin.setPlaceholderText(_translate("Login", "Pin"))
        self.btn_GoCreateAccount.setText(_translate("Login", "Don\'t have an account yet? Create new account."))
        self.btn_Login.setText(_translate("Login", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec())
