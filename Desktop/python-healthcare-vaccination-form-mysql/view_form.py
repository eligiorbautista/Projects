from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_ViewForm(object):
    def ReOpenFormsTable(self):
        from forms_table import Ui_FormsTable
        self.forms = QtWidgets.QMainWindow()
        self.ui = Ui_FormsTable()
        self.ui.setupUi(self.forms)
        self.forms.show()

    def DeleteForm(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='jm_health_care_db')
        mycur = mydb.cursor()
        mycur.execute(f'Delete from jm_health_care_submitted_forms where First_Name = "{self.first_name.text()}"')
        mydb.commit()
        from PyQt6.QtWidgets import QMessageBox
        self.deleted = QMessageBox()
        self.deleted.setWindowTitle('JM Healthcare')
        self.deleted.setWindowIcon(QtGui.QIcon('images/logo2.png'))
        self.deleted.setIcon(QMessageBox.Icon.Information)
        self.deleted.setText('This action cannot be undone                                   ')
        self.deleted.setInformativeText('The form was deleted successfully.')
        self.deleted.exec()

    def setupUi(self, ViewForm):
        ViewForm.setObjectName("ViewForm")
        ViewForm.setGeometry(410,50,736, 762)
        font = QtGui.QFont()
        font.setPointSize(5)
        ViewForm.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ViewForm.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(ViewForm)
        self.frame_2.setGeometry(QtCore.QRect(22, 117, 691, 621))
        self.frame_2.setStyleSheet("QFrame {\n"
"background-color:rgba(68, 135, 193,230.0)\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    color:rgb(126, 126, 126);\n"
"    background-color:white;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(43, 37, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(126, 126, 126);\n"
"background-color:white;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(43, 110, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(126, 126, 126);\n"
"background-color:white;")
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 591, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.first_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.first_name.setEnabled(False)
        self.first_name.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.first_name.setFont(font)
        self.first_name.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    color:rgb(0, 0, 0);\n"
"    border-radius:8px;\n"
"    padding: 5px;\n"
"}")
        self.first_name.setObjectName("first_name")
        self.horizontalLayout.addWidget(self.first_name)
        self.last_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.last_name.setEnabled(False)
        self.last_name.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.last_name.setFont(font)
        self.last_name.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    color:rgb(0, 0, 0);\n"
"    border-radius:8px;\n"
"    padding: 5px;\n"
"}")
        self.last_name.setObjectName("last_name")
        self.horizontalLayout.addWidget(self.last_name)
        self.contact_number = QtWidgets.QLineEdit(self.groupBox)
        self.contact_number.setEnabled(False)
        self.contact_number.setGeometry(QtCore.QRect(340, 133, 291, 40))
        self.contact_number.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.contact_number.setFont(font)
        self.contact_number.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    color:rgb(0, 0, 0);\n"
"    border-radius:8px;\n"
"    padding: 5px;\n"
"}")
        self.contact_number.setObjectName("contact_number")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(43, 182, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(126, 126, 126);\n"
"background-color:white;")
        self.label_8.setObjectName("label_8")
        self.address = QtWidgets.QPlainTextEdit(self.groupBox)
        self.address.setEnabled(False)
        self.address.setGeometry(QtCore.QRect(40, 206, 591, 87))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.address.setFont(font)
        self.address.setStyleSheet("QPlainTextEdit\n"
" {\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    color:rgb(0, 0, 0);\n"
"    border-radius:8px;\n"
"    padding: 5px;\n"
"    background-color:white;\n"
"}")
        self.address.setObjectName("address")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 310, 641, 231))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    color:rgb(126, 126, 126);\n"
"    background-color:white;\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 621, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(126, 126, 126);\n"
"background-color:white;")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 110, 621, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(126, 126, 126);\n"
"background-color:white;")
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.diagnosed = QtWidgets.QLabel(self.groupBox_2)
        self.diagnosed.setGeometry(QtCore.QRect(10, 70, 621, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.diagnosed.setFont(font)
        self.diagnosed.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color:white;")
        self.diagnosed.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.diagnosed.setObjectName("diagnosed")
        self.symptoms = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.symptoms.setEnabled(False)
        self.symptoms.setGeometry(QtCore.QRect(20, 140, 601, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.symptoms.setFont(font)
        self.symptoms.setStyleSheet("QPlainTextEdit\n"
" {\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    color:rgb(0, 0, 0);\n"
"    border-radius:8px;\n"
"    padding: 5px;\n"
"    background-color:white;\n"
"}")
        self.symptoms.setObjectName("symptoms")
        self.DeleteButton = QtWidgets.QPushButton(self.groupBox)
        self.DeleteButton.setGeometry(QtCore.QRect(536, 553, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.DeleteButton.setStyleSheet("QPushButton {\n"
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
        self.DeleteButton.setObjectName("DeleteButton")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(340, 110, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(126, 126, 126);\n"
"background-color:white;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(340, 40, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(126, 126, 126);\n"
"background-color:white;")
        self.label_12.setObjectName("label_12")
        self.datebirth = QtWidgets.QLineEdit(self.groupBox)
        self.datebirth.setEnabled(False)
        self.datebirth.setGeometry(QtCore.QRect(40, 130, 291, 40))
        self.datebirth.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.datebirth.setFont(font)
        self.datebirth.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    color:rgb(0, 0, 0);\n"
"    border-radius:8px;\n"
"    padding: 5px;\n"
"}")
        self.datebirth.setObjectName("datebirth")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.frame = QtWidgets.QFrame(ViewForm)
        self.frame.setGeometry(QtCore.QRect(0, 0, 741, 95))
        self.frame.setStyleSheet("background-color:white;\n"
"border: solid rgb(83, 67, 52);\n"
"border-width: 2px 0px 0px 0px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(275, 0, 211, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/logo1.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 70, 741, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(9)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border:none;color:rgb(126, 126, 126)")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(ViewForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 741, 761))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/bg.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.frame.raise_()
        self.frame_2.raise_()

        self.retranslateUi(ViewForm)
        QtCore.QMetaObject.connectSlotsByName(ViewForm)
        ViewForm.setTabOrder(self.first_name, self.last_name)
        ViewForm.setTabOrder(self.last_name, self.contact_number)
        ViewForm.setTabOrder(self.contact_number, self.address)
        ViewForm.setTabOrder(self.address, self.DeleteButton)

    def retranslateUi(self, ViewForm):
        _translate = QtCore.QCoreApplication.translate
        ViewForm.setWindowTitle(_translate("ViewForm", "View Form"))
        self.groupBox.setTitle(_translate("ViewForm", "View Form"))
        self.label_6.setText(_translate("ViewForm", "First Name"))
        self.label_7.setText(_translate("ViewForm", "Date of Birth"))
        self.first_name.setPlaceholderText(_translate("ViewForm", "First Name"))
        self.last_name.setPlaceholderText(_translate("ViewForm", "Last Name"))
        self.contact_number.setPlaceholderText(_translate("ViewForm", "Contact No."))
        self.label_8.setText(_translate("ViewForm", "Address"))
        self.groupBox_2.setTitle(_translate("ViewForm", "Medical History"))
        self.label_9.setText(_translate("ViewForm", "Have you been diagnosed with Covid-19?"))
        self.label_10.setText(_translate("ViewForm", "Sysmptoms."))
        self.diagnosed.setText(_translate("ViewForm", "Yes/No"))
        self.DeleteButton.setText(_translate("ViewForm", "Delete"))
        self.label_11.setText(_translate("ViewForm", "Contact No."))
        self.label_12.setText(_translate("ViewForm", "Last Name"))
        self.datebirth.setPlaceholderText(_translate("ViewForm", "Date of Birth"))
        self.label_5.setText(_translate("ViewForm", "Known for our expertise. Chosen for our care."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewForm = QtWidgets.QDialog()
    ui = Ui_ViewForm()
    ui.setupUi(ViewForm)
    ViewForm.show()
    sys.exit(app.exec())
