# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 27))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_About = QtWidgets.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainForm)
        self.actionExit.setObjectName("actionExit")
        self.action_New = QtWidgets.QAction(MainForm)
        self.action_New.setObjectName("action_New")
        self.actionAbout_CNBC = QtWidgets.QAction(MainForm)
        self.actionAbout_CNBC.setObjectName("actionAbout_CNBC")
        self.menu_File.addAction(self.action_New)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menu_About.addAction(self.actionAbout_CNBC)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())

        self.retranslateUi(MainForm)
        self.actionExit.triggered.connect(MainForm.close)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "CNBC Analysis"))
        self.menu_File.setTitle(_translate("MainForm", "&File"))
        self.menu_About.setTitle(_translate("MainForm", "&Help"))
        self.actionExit.setText(_translate("MainForm", "E&xit"))
        self.action_New.setText(_translate("MainForm", "&New"))
        self.actionAbout_CNBC.setText(_translate("MainForm", "About CNBC"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())

