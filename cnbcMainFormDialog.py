# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainMain(object):
    def setupUi(self, MainMain):
        MainMain.setObjectName("MainMain")
        MainMain.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainMain)
        self.centralwidget.setObjectName("centralwidget")
        MainMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 27))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_About = QtWidgets.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")
        MainMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMain)
        self.statusbar.setObjectName("statusbar")
        MainMain.setStatusBar(self.statusbar)
        self.actionE_xit = QtWidgets.QAction(MainMain)
        self.actionE_xit.setObjectName("actionE_xit")
        self.menu_File.addAction(self.actionE_xit)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())

        self.retranslateUi(MainMain)
        QtCore.QMetaObject.connectSlotsByName(MainMain)

    def retranslateUi(self, MainMain):
        _translate = QtCore.QCoreApplication.translate
        MainMain.setWindowTitle(_translate("MainMain", "CNBC Analysis"))
        self.menu_File.setTitle(_translate("MainMain", "&File"))
        self.menu_About.setTitle(_translate("MainMain", "&About"))
        self.actionE_xit.setText(_translate("MainMain", "E&xit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMain = QtWidgets.QMainWindow()
    ui = Ui_MainMain()
    ui.setupUi(MainMain)
    MainMain.show()
    sys.exit(app.exec_())

