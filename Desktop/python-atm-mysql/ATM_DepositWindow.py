from PyQt6 import QtCore, QtGui, QtWidgets
import datetime, mysql.connector

class Ui_Deposit(object):
    def setupUi(self, Deposit):
        Deposit.setObjectName("Deposit")
        Deposit.resize(742, 512)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/credit-card.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Deposit.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Deposit)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 741, 511))
        self.frame_2.setStyleSheet("background-color:rgb(7, 44, 112)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
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
        self.label.setGeometry(QtCore.QRect(310, 80, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;color:white")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(250, 80, 51, 51))
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
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(160, 140, 391, 231))
        self.frame_3.setStyleSheet("background-color:rgb(7, 44, 111)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:none;color:white")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btn_Deposit = QtWidgets.QPushButton(self.frame_3)
        self.btn_Deposit.setGeometry(QtCore.QRect(240, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.btn_Deposit.setFont(font)
        self.btn_Deposit.setStyleSheet("background-color:rgb(44, 48, 61);color:white")
        self.btn_Deposit.setObjectName("btn_Deposit")
        self.lineEdit_Pin = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_Pin.setGeometry(QtCore.QRect(69, 88, 261, 31))
        self.lineEdit_Pin.setStyleSheet("border:2px solid black;background-color:white;color:black;padding:2px")
        self.lineEdit_Pin.setText("")
        self.lineEdit_Pin.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_Pin.setObjectName("lineEdit_Pin")
        self.lineEdit_CardID = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_CardID.setGeometry(QtCore.QRect(69, 48, 261, 31))
        self.lineEdit_CardID.setStyleSheet("border:2px solid black;background-color:white;color:black;padding:2px")
        self.lineEdit_CardID.setText("")
        self.lineEdit_CardID.setObjectName("lineEdit_CardID")
        self.passwordHideShow = QtWidgets.QPushButton(self.frame_3)
        self.passwordHideShow.setGeometry(QtCore.QRect(300, 90, 27, 27))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.passwordHideShow.setFont(font)
        self.passwordHideShow.setStyleSheet("background:none;color:black;")
        self.passwordHideShow.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/hidepw.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.passwordHideShow.setIcon(icon1)
        self.passwordHideShow.setIconSize(QtCore.QSize(21, 21))
        self.passwordHideShow.setCheckable(True)
        self.passwordHideShow.setFlat(True)
        self.passwordHideShow.setObjectName("passwordHideShow")
        self.doubleSpinBox_DepositAmount = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.doubleSpinBox_DepositAmount.setGeometry(QtCore.QRect(70, 130, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.doubleSpinBox_DepositAmount.setFont(font)
        self.doubleSpinBox_DepositAmount.setStyleSheet("border:2px solid black;background-color:white;color:black;padding:2px")
        self.doubleSpinBox_DepositAmount.setMaximum(9999999999.0)
        self.doubleSpinBox_DepositAmount.setSingleStep(100.0)
        self.doubleSpinBox_DepositAmount.setObjectName("doubleSpinBox_DepositAmount")
        Deposit.setCentralWidget(self.centralwidget)
        Deposit.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Deposit.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.btn_Deposit.clicked.connect(self.Deposit)
        self.btn_Exit.clicked.connect(self.ShowDashboard)
        self.btn_Exit.clicked.connect(Deposit.close)
        self.btn_Minimize.clicked.connect(Deposit.showMinimized)
        self.passwordHideShow.toggled.connect(self.ShowHidePw)

        Deposit.setTabOrder(self.lineEdit_CardID, self.lineEdit_Pin)
        Deposit.setTabOrder(self.lineEdit_Pin, self.doubleSpinBox_DepositAmount)
        Deposit.setTabOrder(self.doubleSpinBox_DepositAmount, self.btn_Deposit)

        from ATM_DashboardWindow import Ui_Dashboard
        self.dashboard = QtWidgets.QMainWindow()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self.dashboard)
        self.dashboard.close()

        self.retranslateUi(Deposit)
        QtCore.QMetaObject.connectSlotsByName(Deposit)
    
    def ShowDashboard(self):
        CARD_ID = self.lineEdit_CardID.text()
        CARD_PIN = self.lineEdit_Pin.text()
        if len(CARD_ID) !=0 and len(CARD_PIN) != 0:
            try:
                DATABASE = mysql.connector.connect(host='localhost',user='root',passwd='root',database='ATM_DB')
                CURSOR = DATABASE.cursor()
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
                            self.ui.label_Balance.setText(str(ACCOUNT[1]))

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
    
    def Deposit(self):
        if len(self.lineEdit_Pin.text()) != 0 and len(self.lineEdit_CardID.text()) != 0:
            SETDATE = datetime.datetime.now()
            STRINGDATE = SETDATE.strftime('%B %d,%Y [%I:%M%p]')
            DATE_ = STRINGDATE
            CARD_ID = self.lineEdit_CardID.text()
            CARD_PIN = self.lineEdit_Pin.text()
            DEPOSIT_AMOUNT = self.doubleSpinBox_DepositAmount.value()
            NEW_BALANCE = DEPOSIT_AMOUNT
            DATABASE = mysql.connector.connect(host='localhost',user='root',passwd='root',database='ATM_DB')
            CURSOR = DATABASE.cursor()

            CURSOR.execute(f'SELECT * FROM account_balance WHERE CARD = "{CARD_ID}"')
            ACCOUNT_BALANCE = CURSOR.fetchall() 
            for BALANCE in ACCOUNT_BALANCE:
                NEW_BALANCE = float(BALANCE[1]) + DEPOSIT_AMOUNT



            CURSOR.execute(f'SELECT * FROM account_information WHERE CARD = "{CARD_ID}"')
            ACCOUNTS = CURSOR.fetchall()
            for ACCOUNT in ACCOUNTS:
                if CARD_ID == ACCOUNT[0] and CARD_PIN == ACCOUNT[1]:
                    CURSOR.execute(f'UPDATE account_balance SET BALANCE = {NEW_BALANCE} WHERE CARD = "{CARD_ID}"')
                    DATABASE.commit()

                    from PyQt6.QtWidgets import QMessageBox
                    self.message = QMessageBox()
                    self.message.setWindowIcon(QtGui.QIcon('images/credit-card.png'))
                    self.message.setWindowTitle('HS ATM')
                    self.message.setIcon(QMessageBox.Icon.NoIcon)
                    self.message.setText('Transaction Complete.')
                    converted_number_deposit = '{:,}'.format(DEPOSIT_AMOUNT)
                    converted_number_balance = '{:,}'.format(NEW_BALANCE)
                    self.message.setInformativeText(f'Total amount of ₱{converted_number_deposit} was added to your account.\nYour new balance is ₱{converted_number_balance}.')
                    self.message.show()
                    self.doubleSpinBox_DepositAmount.setValue(0.00)

                    CURSOR.execute('INSERT INTO ACCOUNT_TRANSACTIONS VALUES(%s,%s,%s,%s)',(CARD_ID,DEPOSIT_AMOUNT,'Deposit',DATE_))
                    DATABASE.commit()
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
            self.passwordHideShow.setIcon(QtGui.QIcon('images/showpw.png'))
            self.lineEdit_Pin.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def retranslateUi(self, Deposit):
        _translate = QtCore.QCoreApplication.translate
        Deposit.setWindowTitle(_translate("Deposit", "HS ATM Deposit"))
        self.btn_Minimize.setText(_translate("Deposit", "-"))
        self.btn_Exit.setText(_translate("Deposit", "x"))
        self.label.setText(_translate("Deposit", "HS ATM"))
        self.label_2.setText(_translate("Deposit", "Deposit"))
        self.btn_Deposit.setText(_translate("Deposit", "Deposit"))
        self.lineEdit_Pin.setPlaceholderText(_translate("Deposit", "Pin"))
        self.lineEdit_CardID.setPlaceholderText(_translate("Deposit", "Card ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Deposit = QtWidgets.QMainWindow()
    ui = Ui_Deposit()
    ui.setupUi(Deposit)
    Deposit.show()
    sys.exit(app.exec())
