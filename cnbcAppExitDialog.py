# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RoccoAppExitDialog.ui'
#
# Created by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExitDialog(QtWidgets.QDialog):
    def setupUi(self, ExitDialog):
        ExitDialog.setObjectName("ExitDialog")
        ExitDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ExitDialog.resize(633, 362)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ExitDialog.sizePolicy().hasHeightForWidth())
        ExitDialog.setSizePolicy(sizePolicy)
        ExitDialog.setModal(True)
        self.btnNo = QtWidgets.QPushButton(ExitDialog)
        self.btnNo.setGeometry(QtCore.QRect(338, 274, 114, 41))
        self.btnNo.setObjectName("btnNo")
        self.label = QtWidgets.QLabel(ExitDialog)
        self.label.setGeometry(QtCore.QRect(334, 67, 272, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ExitDialog)
        self.label_2.setGeometry(QtCore.QRect(43, 63, 242, 234))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("cnbcResource/MENO005.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.btnYes = QtWidgets.QPushButton(ExitDialog)
        self.btnYes.setGeometry(QtCore.QRect(488, 273, 114, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cnbcResource/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnYes.setIcon(icon)
        self.btnYes.setObjectName("btnYes")

        self.retranslateUi(ExitDialog)
        QtCore.QMetaObject.connectSlotsByName(ExitDialog)

    def retranslateUi(self, ExitDialog):
        _translate = QtCore.QCoreApplication.translate
        ExitDialog.setWindowTitle(_translate("ExitDialog", "Exit Program"))
        self.btnNo.setText(_translate("ExitDialog", "No"))
        self.label.setText(_translate("ExitDialog", "Do you want to Exit the Program?"))
        self.btnYes.setText(_translate("ExitDialog", "Yes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExitDialog = QtWidgets.QDialog()
    ui = Ui_ExitDialog()
    ui.setupUi(ExitDialog)
    ExitDialog.show()
    sys.exit(app.exec_())

