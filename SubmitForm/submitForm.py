# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'submitForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QButtonGroup
import mysql.connector


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 331)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nomEntry = QtWidgets.QTextEdit(self.centralwidget)
        self.nomEntry.setGeometry(QtCore.QRect(10, 30, 231, 21))
        self.nomEntry.setObjectName("nomEntry")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.prenomEntry = QtWidgets.QTextEdit(self.centralwidget)
        self.prenomEntry.setGeometry(QtCore.QRect(10, 80, 231, 21))
        self.prenomEntry.setObjectName("prenomEntry")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.adressEntry = QtWidgets.QTextEdit(self.centralwidget)
        self.adressEntry.setGeometry(QtCore.QRect(10, 130, 231, 81))
        self.adressEntry.setObjectName("adressEntry")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(250, 10, 101, 221))
        font = QtGui.QFont()
        font.setKerning(True)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 40, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 60, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 80, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 100, 70, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 120, 70, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 140, 70, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 160, 70, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 180, 70, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.radioGroup=QButtonGroup()
        self.hommeRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.hommeRadio.setGeometry(QtCore.QRect(60, 230, 82, 17))
        self.hommeRadio.setObjectName("hommeRadio")
        self.femmeRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.femmeRadio.setGeometry(QtCore.QRect(130, 230, 82, 17))
        self.femmeRadio.setObjectName("femmeRadio")
        self.radioGroup.addButton(self.hommeRadio)
        self.radioGroup.addButton(self.femmeRadio)
        self.okBtn = QtWidgets.QPushButton(self.centralwidget)
        self.okBtn.setGeometry(QtCore.QRect(50, 260, 81, 31))
        self.okBtn.setObjectName("okBtn")
        self.okBtn.clicked.connect(self.retrieveData)

        self.annulerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.annulerBtn.setGeometry(QtCore.QRect(190, 260, 81, 31))
        self.annulerBtn.setObjectName("annulerBtn")
        self.annulerBtn.clicked.connect(self.cleanInputs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 356, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def checkAllNotEmpty(self,nom,prenom,adress,sexe,sports_selected):
        if nom=='' or prenom=='' or adress=='' or sexe=='' or len(sports_selected)==0:
            return False
        return True

    def show_popUp(self):
        msgBox=QMessageBox()
        msgBox.setText('Please Fill all Fields')
        msgBox.setIcon(QMessageBox.Critical)
        x=msgBox.exec_()

    def addDataToDb(self,nom,prenom,adress,sexe,sports_selected):
        msgBox=QMessageBox()
        try:
            mydb = mysql.connector.connect(
              host="localhost",
              user="root",
              password="",
              database='user'
            )
            mycursor = mydb.cursor()

            sql=f'insert into user(nom,prenom,address,sexe,sports) values("{nom}","{prenom}","{adress}","{sexe}","{",".join(sports_selected)}")' 
            mycursor.execute(sql)
            mydb.commit()

            msgBox.setText('Data inserted Successfully')
            msgBox.setIcon(QMessageBox.Information)
        except:
            msgBox.setText('Error in Connecting with Database')
            msgBox.setIcon(QMessageBox.Critical)

        x=msgBox.exec_()

        

    def retrieveData(self):
        nom=self.nomEntry.toPlainText()
        prenom=self.prenomEntry.toPlainText()
        adress=self.adressEntry.toPlainText()
        if self.hommeRadio.isChecked():
            sexe='homme'
        else:
            sexe='femme'
    
        sports_selected=[]

        if self.checkBox.isChecked():
            sports_selected.append(self.checkBox.text())
        if self.checkBox_2.isChecked():
            sports_selected.append(self.checkBox_2.text())
        if self.checkBox_3.isChecked():
            sports_selected.append(self.checkBox_3.text())
        if self.checkBox_4.isChecked():
            sports_selected.append(self.checkBox_4.text())
        if self.checkBox_5.isChecked():
            sports_selected.append(self.checkBox_5.text())
        if self.checkBox_6.isChecked():
            sports_selected.append(self.checkBox_6.text())
        if self.checkBox_7.isChecked():
            sports_selected.append(self.checkBox_7.text())
        if self.checkBox_8.isChecked():
            sports_selected.append(self.checkBox_8.text())
        if self.checkBox_9.isChecked():
            sports_selected.append(self.checkBox_9.text())

        if self.checkAllNotEmpty(nom,prenom,adress,sexe,sports_selected):
            self.addDataToDb(nom,prenom,adress,sexe,sports_selected)
        else:
            self.show_popUp()
            
    def cleanInputs(self):
        self.nomEntry.setText('')
        self.prenomEntry.setText('')
        self.adressEntry.setText('')
        #if you wanna select multi radio buttons
        # self.radioGroup.setExclusive(False)
        self.hommeRadio.setChecked(False)
        self.femmeRadio.setChecked(False)
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nom"))
        self.nomEntry.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Prenom"))
        self.label_3.setText(_translate("MainWindow", "Adresse"))
        self.checkBox.setText(_translate("MainWindow", "Tennis"))
        self.checkBox_2.setText(_translate("MainWindow", "Squach"))
        self.checkBox_3.setText(_translate("MainWindow", "Natation"))
        self.checkBox_4.setText(_translate("MainWindow", "Athletisme"))
        self.checkBox_5.setText(_translate("MainWindow", "Randonne"))
        self.checkBox_6.setText(_translate("MainWindow", "Foot"))
        self.checkBox_7.setText(_translate("MainWindow", "Basket"))
        self.checkBox_8.setText(_translate("MainWindow", "Volley"))
        self.checkBox_9.setText(_translate("MainWindow", "Petanque"))
        self.label_4.setText(_translate("MainWindow", "Sexe"))
        self.hommeRadio.setText(_translate("MainWindow", "Homme"))
        self.femmeRadio.setText(_translate("MainWindow", "Femme"))
        self.okBtn.setText(_translate("MainWindow", "OK"))
        self.annulerBtn.setText(_translate("MainWindow", "Annuler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())