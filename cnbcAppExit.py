#!/usr/bin/env python3.4

# Author - KO . All rights reserved.

__author__ = 'ko'

import logging.config

logging.config.fileConfig('./Support/logging.conf')  # create and configure logger
logger = logging.getLogger('CNBC.ExitDialog')

from cnbcAppExitDialog import Ui_ExitDialog
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui

class MyExitDialog(QDialog):
    def __init__(self, parent=None):
        super(MyExitDialog, self).__init__()
        self.ui = Ui_ExitDialog()
        self.ui.setupUi(self)
        # use new style signals
        self.ui.btnYes.clicked.connect(self.accept)
        self.ui.btnNo.clicked.connect(self.reject)



