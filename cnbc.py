#!/usr/bin/env python3.4

# Author - KO . All rights reserved.

import sys                                             # for QApplication in main loop

import logging.config
logging.config.fileConfig('./Support/logging.conf')    # create and configure logger

from PyQt5.QtWidgets import QApplication               # for QApplication in main loop
from cnbcMainForm import MainForm                      # Main


def main():
    logger = logging.getLogger('CNBC.Startup ')
    logger.debug(" ")
    logger.debug("*" * 60)
    logger.debug('Starting the CNBC program')
    logger.debug ( "*" * 60 )
    app = QApplication(sys.argv)
    mf = MainForm()
    mf.show()
    sys.exit ( app.exec_ ( ) )

if __name__ == "__main__":
        main()