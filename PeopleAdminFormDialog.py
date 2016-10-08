# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PeopleAdminForm.ui'
#
# Created by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormPeopleAdministration(object):
    def setupUi(self, FormPeopleAdministration):
        FormPeopleAdministration.setObjectName("FormPeopleAdministration")
        FormPeopleAdministration.resize(640, 480)
        self.pushButtonChange = QtWidgets.QPushButton(FormPeopleAdministration)
        self.pushButtonChange.setGeometry(QtCore.QRect(510, 420, 111, 31))
        self.pushButtonChange.setObjectName("pushButtonChange")
        self.pushButtonClose = QtWidgets.QPushButton(FormPeopleAdministration)
        self.pushButtonClose.setGeometry(QtCore.QRect(370, 420, 111, 31))
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.groupBox = QtWidgets.QGroupBox(FormPeopleAdministration)
        self.groupBox.setGeometry(QtCore.QRect(370, 20, 231, 191))
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(0, 20, 231, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.radioButtonAdd = QtWidgets.QRadioButton(self.frame)
        self.radioButtonAdd.setGeometry(QtCore.QRect(30, 20, 104, 22))
        self.radioButtonAdd.setChecked(True)
        self.radioButtonAdd.setObjectName("radioButtonAdd")
        self.radioButtonEdit = QtWidgets.QRadioButton(self.frame)
        self.radioButtonEdit.setGeometry(QtCore.QRect(30, 70, 104, 22))
        self.radioButtonEdit.setObjectName("radioButtonEdit")
        self.radioButtonDelete = QtWidgets.QRadioButton(self.frame)
        self.radioButtonDelete.setGeometry(QtCore.QRect(30, 120, 131, 22))
        self.radioButtonDelete.setObjectName("radioButtonDelete")
        self.label = QtWidgets.QLabel(FormPeopleAdministration)
        self.label.setGeometry(QtCore.QRect(370, 260, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FormPeopleAdministration)
        self.label_2.setGeometry(QtCore.QRect(370, 330, 31, 21))
        self.label_2.setObjectName("label_2")
        self.lineEditName = QtWidgets.QLineEdit(FormPeopleAdministration)
        self.lineEditName.setGeometry(QtCore.QRect(420, 260, 191, 27))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditRole = QtWidgets.QLineEdit(FormPeopleAdministration)
        self.lineEditRole.setGeometry(QtCore.QRect(420, 330, 191, 27))
        self.lineEditRole.setObjectName("lineEditRole")
        self.tableWidgetPeople = QtWidgets.QTableWidget(FormPeopleAdministration)
        self.tableWidgetPeople.setGeometry(QtCore.QRect(10, 30, 331, 421))
        self.tableWidgetPeople.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidgetPeople.setObjectName("tableWidgetPeople")
        self.tableWidgetPeople.setColumnCount(0)
        self.tableWidgetPeople.setRowCount(0)

        self.retranslateUi(FormPeopleAdministration)
        QtCore.QMetaObject.connectSlotsByName(FormPeopleAdministration)

    def retranslateUi(self, FormPeopleAdministration):
        _translate = QtCore.QCoreApplication.translate
        FormPeopleAdministration.setWindowTitle(_translate("FormPeopleAdministration", "People Table Administration"))
        self.pushButtonChange.setToolTip(_translate("FormPeopleAdministration", "Check for Errors and Commit changes to People Table"))
        self.pushButtonChange.setText(_translate("FormPeopleAdministration", "Change Table"))
        self.pushButtonClose.setToolTip(_translate("FormPeopleAdministration", "Close the Dialog - No changes to People Table"))
        self.pushButtonClose.setText(_translate("FormPeopleAdministration", "Close"))
        self.groupBox.setTitle(_translate("FormPeopleAdministration", "Action:"))
        self.radioButtonAdd.setToolTip(_translate("FormPeopleAdministration", "Add a New Record - After Name and Role are Entered"))
        self.radioButtonAdd.setText(_translate("FormPeopleAdministration", "Add Record"))
        self.radioButtonEdit.setToolTip(_translate("FormPeopleAdministration", "Edit the Current record"))
        self.radioButtonEdit.setText(_translate("FormPeopleAdministration", "Edit Record"))
        self.radioButtonDelete.setToolTip(_translate("FormPeopleAdministration", "Delete the current record"))
        self.radioButtonDelete.setText(_translate("FormPeopleAdministration", "Delete Record"))
        self.label.setText(_translate("FormPeopleAdministration", "Name:"))
        self.label_2.setText(_translate("FormPeopleAdministration", "Role:"))

