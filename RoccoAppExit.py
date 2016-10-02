__author__ = 'ko'

import logging
import logging.config
import sys

logging.config.fileConfig('logging.conf')  # create and configure logger
logger = logging.getLogger('Rocco.ExitDialog')

from cnbcAppExitDialog import Ui_ExitDialog
from PyQt5.QtWidgets import QDialog, QMainWindow



class MyExitDialog(QDialog):
    def __init__(self, parent=None):
        super(MyExitDialog, self).__init__()
        self.ui = Ui_ExitDialog()
        self.ui.setupUi(self)
        # use new style signals
        self.ui.btnYes.clicked.connect(self.e)
        self.ui.btnNo.clicked.connect(self.reject)

    def close_app(self):
        logger.debug("Closing the Rocco Program via Exit Dialog")
        QApplication.quit()

    def close_dia(self):
        logger.debug("Closing the Exit Dialog")
        MyExitDialog.close()
