from PyQt6 import QtCore, QtGui, QtWidgets
from LoginAdmin import Ui_LoginAdmin
from LoginStudent import Ui_LoginStudent
from StudentRegistration import Ui_StudentRegistration


class Ui_Dashboard(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(539, 271)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(270, 0, 271, 271))
        self.frame.setStyleSheet("background-color:rgb(34, 54, 90)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.ButtonAdminLogin = QtWidgets.QPushButton(self.frame)
        self.ButtonAdminLogin.setGeometry(QtCore.QRect(60, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(11)
        self.ButtonAdminLogin.setFont(font)
        self.ButtonAdminLogin.setStyleSheet("background-color:rgb(177, 177, 177);color:black")
        self.ButtonAdminLogin.setIconSize(QtCore.QSize(15, 15))
        self.ButtonAdminLogin.setObjectName("ButtonAdminLogin")
        self.ButtonStudentLogin = QtWidgets.QPushButton(self.frame)
        self.ButtonStudentLogin.setGeometry(QtCore.QRect(60, 120, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(11)
        self.ButtonStudentLogin.setFont(font)
        self.ButtonStudentLogin.setStyleSheet("background-color:rgb(177, 177, 177);color:black")
        self.ButtonStudentLogin.setIconSize(QtCore.QSize(15, 15))
        self.ButtonStudentLogin.setObjectName("ButtonStudentLogin")
        self.ButtonStudentRegistration = QtWidgets.QPushButton(self.frame)
        self.ButtonStudentRegistration.setGeometry(QtCore.QRect(60, 170, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(11)
        self.ButtonStudentRegistration.setFont(font)
        self.ButtonStudentRegistration.setStyleSheet("background-color:rgb(177, 177, 177);color:black")
        self.ButtonStudentRegistration.setIconSize(QtCore.QSize(15, 15))
        self.ButtonStudentRegistration.setObjectName("ButtonStudentRegistration")
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

        self.ButtonAdminLogin.clicked.connect(self.OpenAdminLogin)
        self.ButtonStudentLogin.clicked.connect(self.OpenStudentLogin)
        self.ButtonStudentRegistration.clicked.connect(self.OpenStudentRegistration)
        self.CreateDatabaseAndTable()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def CreateDatabaseAndTable(self):
        import mysql.connector
        DatabaseConnection = mysql.connector.connect(host = 'localhost',user = 'root', password = 'root')
        DatabaseCursor = DatabaseConnection.cursor()
        DatabaseCursor.execute('create database if not exists ccms_studentinfosystem')
        DatabaseConnection = mysql.connector.connect(host = 'localhost',user = 'root', password = 'root',database = 'ccms_studentinfosystem')
        DatabaseCursor = DatabaseConnection.cursor()
        DatabaseCursor.execute('create table if not exists StudentAccountsTB(Username varchar(256) not null, Password varchar(256) not null)')
        DatabaseCursor.execute('create table if not exists StudentInformationTB(StudentID int primary key auto_increment not null, Name varchar(256) not null, Contact varchar(256) not null, Email varchar(256) not null, Gender varchar(256) not null, Age varchar(256) not null, Date_of_birth varchar(256) not null, Course varchar(256) not null, Track varchar(256) not null, YearLevel varchar(256)not null, Address text not null)')
        DatabaseCursor.execute('create table if not exists StudentCountPerCourseTB(BSIT_StudentCount int not null, BSCS_StudentCount int not null, BSEMC_StudentCount int not null)')

        DatabaseCursor.execute('select * from StudentCountPerCourseTB')
        StudentCount = 0
        for sd in DatabaseCursor.fetchall():
            StudentCount+=1
        if StudentCount == 0:
            DatabaseCursor.execute(f'insert into StudentCountPerCourseTB values({0},{0},{0})')
            DatabaseConnection.commit()

    def OpenAdminLogin(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_LoginAdmin()
        self.ui.setupUi(self.window)
        self.window.show()

    def OpenStudentLogin(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_LoginStudent()
        self.ui.setupUi(self.window)
        self.window.show()

    def OpenStudentRegistration(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_StudentRegistration()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QtGui.QIcon('images/ccmslogo.jpg'))
        Form.setWindowTitle(_translate("Form", "CCMS Student Information System | Dashboard"))
        self.ButtonAdminLogin.setText(_translate("Form", "Admin Login"))
        self.ButtonStudentLogin.setText(_translate("Form", "Student Login"))
        self.ButtonStudentRegistration.setText(_translate("Form", "Student Registration"))
        self.label.setText(_translate("Form", "CCMS Student\n"
"Information System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Dashboard()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
