from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StudentRegistration(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(542, 270)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/ccmslogo.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(270, 0, 271, 271))
        self.frame.setStyleSheet("background-color:rgb(34, 54, 90)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 251, 231))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("border:1px solid white;color:white;")
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.groupBox.setObjectName("groupBox")
        self.LineEditPassword = QtWidgets.QLineEdit(self.groupBox)
        self.LineEditPassword.setGeometry(QtCore.QRect(40, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineEditPassword.setFont(font)
        self.LineEditPassword.setStyleSheet("background-color:white;color:black;border:1px solid black")
        self.LineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.LineEditPassword.setPlaceholderText(" Password")
        self.LineEditPassword.setObjectName("LineEditPassword")
        self.LineEditUsername = QtWidgets.QLineEdit(self.groupBox)
        self.LineEditUsername.setGeometry(QtCore.QRect(40, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineEditUsername.setFont(font)
        self.LineEditUsername.setStyleSheet("background-color:white;color:black;border:1px solid black")
        self.LineEditUsername.setObjectName("LineEditUsername")
        self.ButtonRegister = QtWidgets.QPushButton(self.groupBox)
        self.ButtonRegister.setGeometry(QtCore.QRect(140, 180, 81, 22))
        self.ButtonRegister.setStyleSheet("background-color:rgb(177, 177, 177);color:black")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/register.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ButtonRegister.setIcon(icon1)
        self.ButtonRegister.setIconSize(QtCore.QSize(15, 15))
        self.ButtonRegister.setObjectName("ButtonRegister")
        self.LineEditConfirmPassword = QtWidgets.QLineEdit(self.groupBox)
        self.LineEditConfirmPassword.setGeometry(QtCore.QRect(40, 140, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineEditConfirmPassword.setFont(font)
        self.LineEditConfirmPassword.setStyleSheet("background-color:white;color:black;border:1px solid black")
        self.LineEditConfirmPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.LineEditConfirmPassword.setPlaceholderText(" Confirm Password")
        self.LineEditConfirmPassword.setObjectName("LineEditConfirmPassword")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 271, 271))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setStyleSheet("QFrame{background-color:rgb(243, 243, 243);}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 150, 241, 81))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(25, 39, 65);border:none")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 121, 121))
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:none")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/ccmslogo.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.ButtonRegister.clicked.connect(self.RegisterAccount)
        Form.setTabOrder(self.LineEditUsername,self.LineEditPassword)
        Form.setTabOrder(self.LineEditPassword,self.LineEditConfirmPassword)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def RegisterAccount(self):
        if len(self.LineEditUsername.text()) != 0 and len(self.LineEditPassword.text()) != 0 and len(self.LineEditConfirmPassword.text()) != 0: 
            if self.LineEditPassword.text() == self.LineEditConfirmPassword.text():
                import mysql.connector
                DatabaseConnection = mysql.connector.connect(host = 'localhost',user = 'root', password = 'root',database = 'ccms_studentinfosystem')
                DatabaseCursor = DatabaseConnection.cursor()
                DatabaseCursor.execute('select * from studentaccountstb')
                Accounts = DatabaseCursor.fetchall()

                Validation = 0

                for Account in Accounts:
                    if Account[0] == self.LineEditUsername.text():
                        Validation += 1
                if Validation == 0:
                    import mysql.connector
                    DatabaseConnection = mysql.connector.connect(host = 'localhost',user = 'root', password = 'root',database = 'ccms_studentinfosystem')
                    DatabaseCursor = DatabaseConnection.cursor()
                    DatabaseCursor.execute('insert into studentaccountstb values(%s,%s)',(self.LineEditUsername.text(),self.LineEditConfirmPassword.text()))
                    DatabaseConnection.commit()

                    from PyQt6.QtWidgets import QMessageBox
                    self.mbox = QMessageBox()
                    self.mbox.setWindowIcon(QtGui.QIcon("images/ccmslogo.jpg"))
                    self.mbox.setIcon(QMessageBox.Icon.Information)
                    self.mbox.setWindowTitle(' ')
                    self.mbox.setText('Student account has been successfully created.')
                    self.mbox.show()

                if Validation > 0:
                    from PyQt6.QtWidgets import QMessageBox
                    self.mbox = QMessageBox()
                    self.mbox.setWindowIcon(QtGui.QIcon("images/ccmslogo.jpg"))
                    self.mbox.setIcon(QMessageBox.Icon.Information)
                    self.mbox.setWindowTitle(' ')
                    self.mbox.setText('Student account already exists.')
                    self.mbox.show()
            else:
                from PyQt6.QtWidgets import QMessageBox
                self.mbox = QMessageBox()
                self.mbox.setWindowIcon(QtGui.QIcon("images/ccmslogo.jpg"))
                self.mbox.setIcon(QMessageBox.Icon.Warning)
                self.mbox.setWindowTitle(' ')
                self.mbox.setText('Confirm password and password do not match.')
                self.mbox.setInformativeText('Please check your inputs.')
                self.mbox.show()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QtGui.QIcon('images/ccmslogo.jpg'))
        Form.setWindowTitle(_translate("Form", "CCMS Student Information System | Student Registration"))
        self.groupBox.setTitle(_translate("Form", "STUDENT REGISTRATION"))
        self.LineEditUsername.setPlaceholderText(_translate("Form", " Username"))
        self.ButtonRegister.setText(_translate("Form", "Register"))
        self.label.setText(_translate("Form", "CCMS Student\n"
"Information System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_StudentRegistration()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
