from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_FormsTable(object):
    def DeleteAllWarn(self):
        from PyQt6.QtWidgets import QMessageBox
        self.deleteall = QMessageBox()
        self.deleteall.setWindowTitle('JM Healthcare')
        self.deleteall.setWindowIcon(QtGui.QIcon('images/logo2.png'))
        self.deleteall.setIcon(QMessageBox.Icon.Critical)
        self.deleteall.setText('This action cannot be undone                                   ')
        self.deleteall.setInformativeText('Are you sure you want to delete all the forms?')
        self.deleteall.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        self.deleteall.buttonClicked.connect(self.DeleteAllForms)
        self.deleteall.exec()
    def DeleteAllForms(self, warning):
        if warning.text() == '&Yes':
                mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='jm_health_care_db')
                mycur = mydb.cursor()
                mycur.execute(f'Delete from jm_health_care_submitted_forms')
                mydb.commit()
                from PyQt6.QtWidgets import QMessageBox
                self.deleted = QMessageBox()
                self.deleted.setWindowTitle('JM Healthcare')
                self.deleted.setWindowIcon(QtGui.QIcon('images/logo2.png'))
                self.deleted.setIcon(QMessageBox.Icon.Information)
                self.deleted.setText('This action cannot be undone                                   ')
                self.deleted.setInformativeText('All forms was deleted successfully.')
                self.deleted.exec()

    def GetId(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='jm_health_care_db')
        mycur = mydb.cursor()
        mycur.execute('Select * from jm_health_care_submitted_forms')
        Ids = mycur.fetchall()

        diagnosed_yes = 0
        diagnosed_no = 0

        for id in Ids:
                self.listWidget.addItem(f'Form {id[0]}')
                if id[6] == 'No': diagnosed_no += 1
                if id[6] == 'Yes': diagnosed_yes += 1
        self.diagnosed_count.setText(f'Yes: {diagnosed_yes}     |     No: {diagnosed_no}')

    def GoViewForm(self):
        from view_form import Ui_ViewForm
        self.table = QtWidgets.QMainWindow()
        self.ui = Ui_ViewForm()
        self.ui.setupUi(self.table)
        self.Id = self.listWidget.currentItem().text().replace('Form','').strip()

        # ================================== Table ===================================
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='jm_health_care_db')
        mycur = mydb.cursor()
        mycur.execute(f'Select * from jm_health_care_submitted_forms where Form_Id = {str(self.Id)}')
        Ids = mycur.fetchall()
        for id in Ids:
                self.symptoms_list = str(id[7]).replace('[','').replace(']','').replace("'",'').replace(',',', ')
                self.ui.first_name.setText(id[1])
                self.ui.last_name.setText(id[2])
                self.ui.datebirth.setText(id[3])
                self.ui.contact_number.setText(id[4])
                self.ui.address.setPlainText(id[5])
                self.ui.diagnosed.setText(id[6])
                self.ui.symptoms.setPlainText(self.symptoms_list)
        self.ui.DeleteButton.clicked.connect(self.ui.DeleteForm)
        self.ui.DeleteButton.clicked.connect(lambda: self.table.close())
        self.ui.DeleteButton.clicked.connect(lambda: FormsTable.close())
        self.ui.DeleteButton.clicked.connect(self.ui.ReOpenFormsTable)   
        # 0 Id
        # 1 Fname
        # 2 Lname
        # 3 Birthdate
        # 4 Contact 
        # 5 Address
        # 6 Diagnosed
        # 7 Symptoms

        # ==================================================== SQLITE3 ====================================================
        # mydb = sqlite3.connect('jm_health_care.db')
        # mycur = mydb.cursor()
        # mycur.execute(f'Select * from jm_health_care_submitted_forms where Form_Id = {str(self.Id)}')
        # Ids = mycur.fetchall()
        # for id in Ids:
        #         self.symptoms_list = str(id[7]).replace('[','').replace(']','').replace("'",'').replace(',',', ')
        #         self.ui.first_name.setText(id[1])
        #         self.ui.last_name.setText(id[2])
        #         self.ui.datebirth.setText(id[3])
        #         self.ui.contact_number.setText(id[4])
        #         self.ui.address.setPlainText(id[5])
        #         self.ui.diagnosed.setText(id[6])
        #         self.ui.symptoms.setPlainText(self.symptoms_list)
        

        self.table.show()

    def setupUi(self, FormsTable):
        FormsTable.setObjectName("FormsTable")
        FormsTable.setGeometry(410,50,824, 762)
        font = QtGui.QFont()
        font.setPointSize(5)
        FormsTable.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        FormsTable.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(FormsTable)
        self.frame_2.setGeometry(QtCore.QRect(22, 117, 781, 621))
        self.frame_2.setStyleSheet("QFrame {\n"
"background-color:rgba(68, 135, 193,230.0)\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(12, 82, 761, 481))
        self.listWidget.setStyleSheet("background-color:white;color:black;padding:10px;color:rgb(35, 36, 38);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setFont(QtGui.QFont('Arial', 15))
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 761, 61))
        self.frame_3.setStyleSheet("background-color:white;color:black")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 761, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(126, 126, 126);\n"
"background-color:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.diagnosed_count = QtWidgets.QLabel(self.frame_3)
        self.diagnosed_count.setGeometry(QtCore.QRect(0, 33, 761, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.diagnosed_count.setFont(font)
        self.diagnosed_count.setStyleSheet("color:rgb(126, 126, 126);\n"
"background-color:white;")
        self.diagnosed_count.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.diagnosed_count.setObjectName("diagnosed_count")
        self.frame = QtWidgets.QFrame(FormsTable)
        self.frame.setGeometry(QtCore.QRect(0, 0, 831, 95))
        self.frame.setStyleSheet("background-color:white;\n"
"border: solid rgb(83, 67, 52);\n"
"border-width: 2px 0px 0px 0px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(320, 0, 211, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/logo1.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 70, 821, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(9)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border:none;color:rgb(126, 126, 126)")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(FormsTable)
        self.label.setGeometry(QtCore.QRect(0, 0, 831, 761))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/bg.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.DeleteAllButton = QtWidgets.QPushButton(self.frame_2)
        self.DeleteAllButton.setGeometry(QtCore.QRect(630, 575, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteAllButton.setFont(font)
        self.DeleteAllButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.DeleteAllButton.setStyleSheet("QPushButton {\n"
"    background-color:rgb(213, 0, 0);\n"
"    color:#fff;\n"
"    border-radius:2px;\n"
"    padding-top:5px;\n"
"    padding-bottom:5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color:rgb(0, 0, 0);\n"
"}")
        self.DeleteAllButton.setObjectName("DeleteAllButton")

        self.retranslateUi(FormsTable)
        QtCore.QMetaObject.connectSlotsByName(FormsTable)
        self.GetId()
        self.listWidget.doubleClicked.connect(self.GoViewForm)
        self.DeleteAllButton.clicked.connect(self.DeleteAllWarn)

    def retranslateUi(self, FormsTable):
        _translate = QtCore.QCoreApplication.translate
        FormsTable.setWindowTitle(_translate("FormsTable", "Submitted Forms"))
        self.label_2.setText(_translate("FormsTable", "No. of Diagnosed Person"))
        self.diagnosed_count.setText(_translate("FormsTable", "Yes: 10     |     No: 9"))
        self.DeleteAllButton.setText(_translate("Dialog", "Delete All"))
        self.label_5.setText(_translate("FormsTable", "Known for our expertise. Chosen for our care."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormsTable = QtWidgets.QDialog()
    ui = Ui_FormsTable()
    ui.setupUi(FormsTable)
    FormsTable.show()
    sys.exit(app.exec())
