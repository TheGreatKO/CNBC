#!/usr/bin/env python3.4

# Author - KO . All rights reserved.

__author__ = "KO"
__version__ = 1.01
__date__ = "1 Oct 2016"

import logging.config

logging.config.fileConfig('./Support/logging.conf')              # create and configure logger
logger = logging.getLogger('CNBC.MainForm')                      # Set Logger Prefix column

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QAction, QStatusBar, QMenu
from PyQt5.QtCore import QSettings
from PyQt5.Qt import QIcon
from MainForm import Ui_MainForm

class MainForm(Ui_MainForm, QMainWindow):
    def __init__(self, parent = None):
        super(MainForm, self).__init__(parent)
        self.setupUi ( self )
        self.showMaximized()
        self.setWindowIcon(QIcon(":/img/CNBC_Program.png"))

        # Log Actions
        logger.debug("Initializing Main Form")

        # Get Settings
        self.settings = QSettings ( "KnockOut Programmers", 'CNBC' )
        self.settings.setValue ( 'Author', __author__ )
        self.settings.setValue ( 'Version', __version__ )
        self.settings.setValue ( 'Date', __date__ )

        # Set up Connections
        self.actionAbout_CNBC.triggered.connect ( self.about )

        # Setup Context Menu
    def contextMenuEvent(self, event):
        '''
        This method creates and displays a context menu for the main window.
        :param event:
        :return:
        '''
        menu = QMenu ( self )
        newContextAction = menu.addAction ( "New Show" )
        aboutContextAction = menu.addAction ( "About" )
        quitContextAction = menu.addAction ( "Quit" )
        action = menu.exec_ ( self.mapToGlobal ( event.pos ( ) ) )
        if action == quitContextAction:
            self.close()
        if action == aboutContextAction:
            self.about()
        if action == newContextAction:
            self.newShow()

    def closeEvent(self, event):
        self.statusBar ( ).showMessage ( 'Confirm You Want to Exit Program...' )
        # Show exit message box
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Exit Message")
        msg.setText("Are you sure you want to quit?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Yes)

        reply = msg.exec_ ( )
        self.statusbar.clearMessage()
        if reply == msg.Yes:
            # We want to quit
            logger.debug ( "*" * 60 )
            logger.debug ( "Ending the CNBC Program" )
            logger.debug ( "*" * 60 )
            event.accept ( )
        else:
            # Don't want to quit
            event.ignore ( )


    def about(self):
        '''
        This method Builds and displays the programs About dialog.
        :return:
        '''
        # Post status bar message
        self.statusBar ( ).showMessage ( 'Displaying the About Box' )
        self.settings = QSettings ( "KnockOut Programmers", 'CNBC' )
        # build dialog
        msg = QMessageBox ( )
        msg.setIcon ( QMessageBox.Information )
        msg.setText ( "<B><font color = red>About the CNBC Options Action TV Show Audit Tool</B>")
        msg.setInformativeText ( "The CNBC Audit Tool provides information for comparing how"
                                 "each of the Option Players perform over time and against"
                                 "one another.")
        msg.setWindowTitle ( "CNBC Audit Tool" )
        aut = self.settings.value("Author")
        ver = self.settings.value("Version")
        dat = self.settings.value("Date")
        msg.setDetailedText ( u"The details are as follows:\n\n"
                              u" Each Weekly show that is televised it is copied. \n"
                              u" The copy is watched in detail.\n"
                              u" The data is entered into the CNBC Tool Audit program\n"
                              u" The program stores data into a Postgresql database\n"
                              u" and allows for analysis of the data over time.\n\n"
                              u" Author: {author}\n"
                              u" Version: {version}\n"
                              u" Date: {da} " .format (author=aut, version=float(ver), da=dat))


        msg.setStandardButtons ( QMessageBox.Ok )
        msg.setDefaultButton(QMessageBox.Ok)

        #show dialog
        retval = msg.exec_ ( )

        # Clear status bar message
        self.statusbar.clearMessage()

    def newShow(self):
        pass


