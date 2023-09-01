from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
import sqlite3

class Ui_RegistrationForm(object):
    def SubmitForm(self):
        self.symptoms_list = []

        # Diagnosed
        if self.radio_no.isChecked():
          self.diagnosed = self.radio_no.text()
        if self.radio_yes.isChecked():
          self.diagnosed = self.radio_yes.text()

        # Symptoms
        if self.symptoms_tastesmell.isChecked():
          self.symptoms_list.append(self.symptoms_tastesmell.text())
        
        if self.symptoms_breathing.isChecked():
          self.symptoms_list.append(self.symptoms_breathing.text())

        if self.symptoms_cough.isChecked():
          self.symptoms_list.append(self.symptoms_cough.text())

        if self.symptoms_nose.isChecked():
          self.symptoms_list.append(self.symptoms_nose.text())

        if self.symptoms_nose.isChecked():
          self.symptoms_list.append(self.symptoms_nose.text())

        if self.symptoms_body.isChecked():
          self.symptoms_list.append(self.symptoms_body.text())
        
        if self.symptoms_throat.isChecked():
          self.symptoms_list.append(self.symptoms_throat.text())

        if len(self.symptoms_list) == 0:
          mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='jm_health_care_db')
          mycur = mydb.cursor()
          mycur.execute('Insert into jm_health_care_submitted_forms values(null,%s,%s,%s,%s,%s,%s,%s)',
          (self.first_name.text(),self.last_name.text(),self.datebirth.text(),self.contact_number.text(),self.address.toPlainText(),self.diagnosed,'N/A'))
          mydb.commit()
        else:
          mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='jm_health_care_db')
          mycur = mydb.cursor()
          mycur.execute('Insert into jm_health_care_submitted_forms values(null,%s,%s,%s,%s,%s,%s,%s)',
          (self.first_name.text(),self.last_name.text(),self.datebirth.text(),self.contact_number.text(),self.address.toPlainText(),self.diagnosed,str(self.symptoms_list)))
          mydb.commit()
          if self.radio_no.isChecked():
                mycur.execute('Insert into jm_health_care_diagnosed values(null,%s)',(1))
                mydb.commit()
          if self.radio_yes.isChecked():
                mycur.execute('Insert into jm_health_care_diagnosed values(%s,null)',(1))
                mydb.commit()
        from PyQt6.QtWidgets import QMessageBox
        self.messagebox = QMessageBox()
        self.messagebox.setWindowTitle('JM Healthcare')
        self.messagebox.setWindowIcon(QtGui.QIcon('images/logo2.png'))
        self.messagebox.setIcon(QMessageBox.Icon.Information)
        self.messagebox.setText('Thank You                                           ')
        self.messagebox.setInformativeText('The form was submitted successfully.')
        self.messagebox.exec()

    def setupUi(self, RegistrationForm):
        RegistrationForm.setObjectName("RegistrationForm")
        RegistrationForm.setGeometry(410,50,736, 762)
        font = QtGui.QFont()
        font.setPointSize(5)
        RegistrationForm.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        RegistrationForm.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(RegistrationForm)
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
        self.label_6.setGeometry(QtCore.QRect(43, 37, 61, 16))
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
        self.datebirth = QtWidgets.QDateEdit(self.groupBox)
        self.datebirth.setGeometry(QtCore.QRect(40, 133, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.datebirth.setFont(font)
        self.datebirth.setStyleSheet("border: 1px solid rgb(122, 122, 122);\n"
"color:rgb(122, 122, 122);\n"
"padding-left:5px;\n"
"background-color:white;\n"
"")
        self.datebirth.setCalendarPopup(True)
        self.datebirth.setDate(QtCore.QDate(2000, 1, 1))
        self.datebirth.setObjectName("datebirth")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 591, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.first_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.first_name.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.first_name.setFont(font)
        self.first_name.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    color:rgb(122, 122, 122);\n"
"    border-radius:8px;\n"
"    padding: 5px;\n"
"}")
        self.first_name.setObjectName("first_name")
        self.horizontalLayout.addWidget(self.first_name)
        self.last_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.last_name.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.last_name.setFont(font)
        self.last_name.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    color:rgb(122, 122, 122);\n"
"    border-radius:8px;\n"
"    padding: 5px;\n"
"}")
        self.last_name.setObjectName("last_name")
        self.horizontalLayout.addWidget(self.last_name)
        self.contact_number = QtWidgets.QLineEdit(self.groupBox)
        self.contact_number.setGeometry(QtCore.QRect(340, 133, 291, 40))
        self.contact_number.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.contact_number.setFont(font)
        self.contact_number.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    color:rgb(122, 122, 122);\n"
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
        self.address.setGeometry(QtCore.QRect(40, 206, 591, 87))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.address.setFont(font)
        self.address.setStyleSheet("QPlainTextEdit\n"
" {\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    color:rgb(122, 122, 122);\n"
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
        self.symptoms_tastesmell = QtWidgets.QCheckBox(self.groupBox_2)
        self.symptoms_tastesmell.setGeometry(QtCore.QRect(21, 141, 160, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.symptoms_tastesmell.setFont(font)
        self.symptoms_tastesmell.setObjectName("symptoms_tastesmell")
        self.symptoms_breathing = QtWidgets.QCheckBox(self.groupBox_2)
        self.symptoms_breathing.setGeometry(QtCore.QRect(188, 141, 164, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.symptoms_breathing.setFont(font)
        self.symptoms_breathing.setObjectName("symptoms_breathing")
        self.symptoms_cough = QtWidgets.QCheckBox(self.groupBox_2)
        self.symptoms_cough.setGeometry(QtCore.QRect(359, 141, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.symptoms_cough.setFont(font)
        self.symptoms_cough.setObjectName("symptoms_cough")
        self.symptoms_nose = QtWidgets.QCheckBox(self.groupBox_2)
        self.symptoms_nose.setGeometry(QtCore.QRect(441, 141, 114, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.symptoms_nose.setFont(font)
        self.symptoms_nose.setObjectName("symptoms_nose")
        self.symptoms_body = QtWidgets.QCheckBox(self.groupBox_2)
        self.symptoms_body.setGeometry(QtCore.QRect(21, 181, 114, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.symptoms_body.setFont(font)
        self.symptoms_body.setObjectName("symptoms_body")
        self.symptoms_throat = QtWidgets.QCheckBox(self.groupBox_2)
        self.symptoms_throat.setGeometry(QtCore.QRect(142, 181, 108, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.symptoms_throat.setFont(font)
        self.symptoms_throat.setObjectName("symptoms_throat")
        self.radio_yes = QtWidgets.QRadioButton(self.groupBox_2)
        self.radio_yes.setGeometry(QtCore.QRect(14, 74, 53, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radio_yes.setFont(font)
        self.radio_yes.setObjectName("radio_yes")
        self.radio_no = QtWidgets.QRadioButton(self.groupBox_2)
        self.radio_no.setGeometry(QtCore.QRect(77, 74, 47, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radio_no.setFont(font)
        self.radio_no.setObjectName("radio_no")
        self.SubmitButton = QtWidgets.QPushButton(self.groupBox)
        self.SubmitButton.setGeometry(QtCore.QRect(536, 553, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.SubmitButton.setStyleSheet("QPushButton {\n"
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
        self.SubmitButton.setObjectName("SubmitButton")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.frame = QtWidgets.QFrame(RegistrationForm)
        self.frame.setGeometry(QtCore.QRect(0, 0, 741, 95))
        self.frame.setStyleSheet("background-color:white;\n"
"border: solid rgb(83, 67, 52);\n"
"border-width: 2px 0px 0px 0px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(210, 0, 211, 81))
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
        self.label = QtWidgets.QLabel(RegistrationForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 741, 761))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/bg.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.frame.raise_()
        self.frame_2.raise_()

        self.retranslateUi(RegistrationForm)
        QtCore.QMetaObject.connectSlotsByName(RegistrationForm)
        RegistrationForm.setTabOrder(self.first_name, self.last_name)
        RegistrationForm.setTabOrder(self.last_name, self.datebirth)
        RegistrationForm.setTabOrder(self.datebirth, self.contact_number)
        RegistrationForm.setTabOrder(self.contact_number, self.address)
        RegistrationForm.setTabOrder(self.address, self.SubmitButton)
        RegistrationForm.setTabOrder(self.SubmitButton, self.radio_yes)
        RegistrationForm.setTabOrder(self.radio_yes, self.radio_no)

        self.SubmitButton.clicked.connect(self.SubmitForm)

    def retranslateUi(self, RegistrationForm):
        _translate = QtCore.QCoreApplication.translate
        RegistrationForm.setWindowTitle(_translate("RegistrationForm", "Covid-19 Vaccine Registration Form"))
        self.groupBox.setTitle(_translate("RegistrationForm", "Registration Form"))
        self.label_6.setText(_translate("RegistrationForm", "Name"))
        self.label_7.setText(_translate("RegistrationForm", "Date of Birth"))
        self.first_name.setPlaceholderText(_translate("RegistrationForm", "First Name"))
        self.last_name.setPlaceholderText(_translate("RegistrationForm", "Last Name"))
        self.contact_number.setPlaceholderText(_translate("RegistrationForm", "Contact No."))
        self.label_8.setText(_translate("RegistrationForm", "Address"))
        self.groupBox_2.setTitle(_translate("RegistrationForm", "Medical History"))
        self.label_9.setText(_translate("RegistrationForm", "Have you been diagnosed with Covid-19?"))
        self.label_10.setText(_translate("RegistrationForm", "Please check all sysmptoms that apply."))
        self.symptoms_tastesmell.setText(_translate("RegistrationForm", "Loss of taste/smell"))
        self.symptoms_breathing.setText(_translate("RegistrationForm", "Difficulty breathing"))
        self.symptoms_cough.setText(_translate("RegistrationForm", "Cough"))
        self.symptoms_nose.setText(_translate("RegistrationForm", "Runny nose"))
        self.symptoms_body.setText(_translate("RegistrationForm", "Body aches"))
        self.symptoms_throat.setText(_translate("RegistrationForm", "Sore throat"))
        self.radio_yes.setText(_translate("RegistrationForm", "Yes"))
        self.radio_no.setText(_translate("RegistrationForm", "No"))
        self.SubmitButton.setText(_translate("RegistrationForm", "Submit"))
        self.label_5.setText(_translate("RegistrationForm", "Known for our expertise. Chosen for our care."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistrationForm = QtWidgets.QDialog()
    ui = Ui_RegistrationForm()
    ui.setupUi(RegistrationForm)
    RegistrationForm.show()
    sys.exit(app.exec())
