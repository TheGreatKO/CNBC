#!/usr/bin/env python3.4

# Author - KO . All rights reserved.
import logging.config

logging.config.fileConfig('./Support/logging.conf')              # create and configure logger
logger = logging.getLogger('CNBC.MainForm')                      # Set Logger Prefix column

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from MainForm import Ui_MainForm

class MainForm(Ui_MainForm, QMainWindow):
    def __init__(self, parent = None):
        super(MainForm, self).__init__(parent)
        logger.debug("Initializing Main Form")
        self.setupUi(self)

    def closeEvent(self, event):
         reply = QMessageBox.question ( self, 'Message',"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No )
         if reply == QMessageBox.Yes:
             logger.debug ( "*" * 60 )
             logger.debug ( "Ending the CNBC Program" )
             logger.debug ( "*" * 60 )
             event.accept ( )
         else:
             event.ignore ( )




