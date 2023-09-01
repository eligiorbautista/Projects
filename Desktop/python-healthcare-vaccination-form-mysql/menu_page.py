from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
class Ui_MenuWindow(object):
    def GoSubmittedForms(self):
        from forms_table import Ui_FormsTable
        self.forms = QtWidgets.QMainWindow()
        self.ui = Ui_FormsTable()
        self.ui.setupUi(self.forms)
        self.forms.show()

    def GoRegistrationForm(self):
        from registration_form import Ui_RegistrationForm
        self.reg = QtWidgets.QMainWindow()
        self.ui = Ui_RegistrationForm()
        self.ui.setupUi(self.reg)
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.first_name.clear())
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.last_name.clear())
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.datebirth.setDate(QtCore.QDate(1,1,2000)))
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.contact_number.clear())
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.address.clear())
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.radio_yes.setChecked(False))
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.radio_no.setChecked(False))
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.symptoms_body.setChecked(False))
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.symptoms_breathing.setChecked(False))
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.symptoms_cough.setChecked(False))
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.symptoms_nose.setChecked(False))
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.symptoms_tastesmell.setChecked(False))
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.symptoms_throat.setChecked(False))
        self.ui.SubmitButton.clicked.connect(lambda: self.ui.symptoms_list.clear())

        self.reg.show()

    def CreateDatabase(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='root')
        mycur = mydb.cursor()
        mycur.execute('Create database if not exists jm_health_care_db')
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='jm_health_care_db')
        mycur = mydb.cursor()
        mycur.execute('Create table if not exists jm_health_care_submitted_forms(Form_Id int primary key auto_increment, First_Name varchar(60) not null, Last_Name varchar(60) not null, Date_of_Birth varchar(60) not null, Contact_Num varchar(60) not null, Address text not null, Diagnosed_covid varchar(3) not null, Symptoms longtext not null)')
        mycur.execute('Create table if not exists jm_health_care_diagnosed(Diagnosed_Yes int not null, Diagnoed_No int not null)')

    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.resize(611, 479)
        MenuWindow.setMinimumSize(QtCore.QSize(611, 479))
        MenuWindow.setMaximumSize(QtCore.QSize(611, 479))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MenuWindow.setWindowIcon(icon)
        MenuWindow.setStyleSheet("background-color:rgb(102, 102, 102)")
        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/bg.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 611, 95))
        self.frame.setStyleSheet("background-color:white;\n"
"border: solid rgb(83, 67, 52);\n"
"border-width: 2px 0px 0px 0px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(210, 0, 211, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/logo1.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 611, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(9)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:none;color:rgb(126, 126, 126)")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(180, 210, 281, 131))
        self.frame_2.setStyleSheet("background-color:rgba(255, 255, 255,210.0)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.RegistrationButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RegistrationButton.setFont(font)
        self.RegistrationButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.RegistrationButton.setStyleSheet("QPushButton {\n"
"    background-color:rgb(76, 150, 215);\n"
"    color:#fff;\n"
"    border-radius:2px;\n"
"    padding-top:5px;\n"
"    padding-bottom:5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color:rgb(38, 76, 109);\n"
"}")
        self.RegistrationButton.setObjectName("RegistrationButton")
        self.verticalLayout.addWidget(self.RegistrationButton)
        self.SubmittedButtons = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SubmittedButtons.setFont(font)
        self.SubmittedButtons.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.SubmittedButtons.setStyleSheet("QPushButton {\n"
"    background-color:rgb(76, 150, 215);\n"
"    color:#fff;\n"
"    border-radius:2px;\n"
"    padding-top:5px;\n"
"    padding-bottom:5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color:rgb(38, 76, 109);\n"
"}")
        self.SubmittedButtons.setObjectName("SubmittedButtons")
        self.verticalLayout.addWidget(self.SubmittedButtons)
        MenuWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)
        self.RegistrationButton.clicked.connect(self.GoRegistrationForm)
        self.CreateDatabase()
        self.SubmittedButtons.clicked.connect(self.GoSubmittedForms)

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "JM Healthcare"))
        self.label_3.setText(_translate("MenuWindow", "Known for our expertise. Chosen for our care."))
        self.RegistrationButton.setText(_translate("MenuWindow", "Covid-19 Vaccine Registration Form"))
        self.SubmittedButtons.setText(_translate("MenuWindow", "View Submitted Forms"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuWindow()
    ui.setupUi(MenuWindow)
    MenuWindow.show()
    sys.exit(app.exec())
