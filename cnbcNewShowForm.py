#!/usr/bin/env python3.4

# Author - KO . All rights reserved.
__author__ = 'ko'

import logging.config
logging.config.fileConfig('./Support/logging.conf')           # create and configure logger
logger = logging.getLogger('CNBC.NewShow ')                   # Set Logger Prefix column

from PyQt5.QtWidgets import QWidget, QAction, QStatusBar, QMenu, QDialog, QMessageBox
from newShowFormDialog import Ui_newShowDialog
from PyQt5.QtCore import  QDate
import psycopg2
from pony.orm import *
from cnbcPeopleAdminForm import PeopleAdmin
import psycopg2
from datetime import date

db = Database ( )

# Create the Database entities
class Show(db.Entity):
    createdDate = Required(date)
    showDate = Required(date)
    moderator = Required(str)
    trader1 = Required(str)
    trader2 = Required(str)
    trader3 = Optional(str)
    trader4 = Optional(str)
    chartist = Optional(str)
    guest = Optional(str)
    security1 = Optional(str)
    security2 = Optional(str)
    security3 = Optional(str)
    security4 = Optional(str)
    security5 = Optional(str)
    active1 = Required(bool)
    active2 = Required(bool)
    active3 = Required(bool)
    active4 = Required(bool)
    active5 = Required(bool)
    showNotes = Optional(str)

class People(db.Entity):
    name = Required(str)
    role = Required(str)

# PostgreSQL
db.bind ( 'postgres', user='ko', password='morgan', host='localhost', database='moaa' )
db.generate_mapping(create_tables=True)

class NewShowForm(Ui_newShowDialog, QDialog):
    db = Database ( )

    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi ( self )
        self.startUp ( )

        # Log Actions
        logger.debug ( 'Initializing New Show Form')

        # Set up Connections
        self.pushButtonReset.clicked.connect ( self.setDefaults )
        self.pushButtonNoAdd.clicked.connect (self.noAdd )
        self.pushButtonAdd.clicked.connect (self.addShowData)
        self.pushButtonPeople.clicked.connect (self.peopleAdmin)

    def startUp(self):
        self.setDefaults()

    def setDefaults(self):
        # Set the DATE controls
        self.dateEditCreatedDate.setDate(QDate.currentDate())
        self.dateEditShowDate.setDate((QDate.currentDate()))
        # Set the COMBOBOX controls
        self.comboBoxModerator.clear()
        self.comboBoxTrader1.clear()
        self.comboBoxTrader2.clear()
        self.comboBoxTrader3.clear()
        self.comboBoxTrader4.clear()
        self.comboBoxChartist.clear()
        self.comboBoxGuest.clear()
        # Set the LINEEDIT controls
        self.lineEditSecurity1.clear()
        self.lineEditSecurity2.clear()
        self.lineEditSecurity3.clear()
        self.lineEditSecurity4.clear()
        self.lineEditSecurity5.clear()
        # Set the CHECKBOX controls
        self.checkBoxActive1.setChecked(False)
        self.checkBoxActive2.setChecked(False)
        self.checkBoxActive3.setChecked(False)
        self.checkBoxActive4.setChecked(False)
        self.checkBoxActive5.setChecked(False)
        # Set the TEXTEDIT controls
        self.textEditShowNotes.clear()
        # Set the PUSHBUTTON controls
        self.pushButtonPlay1.setEnabled(False)
        self.pushButtonPlay2.setEnabled ( False )
        self.pushButtonPlay3.setEnabled ( False )
        self.pushButtonPlay4.setEnabled ( False )
        self.pushButtonPlay5.setEnabled ( False )
        # Load the Moderator COMBOBOX from database
        self.loadModerator()
        self.loadChartist()
        self.loadTrader()
        self.loadGuest()

    def noAdd(self):
        logger.debug ( "Leaving New Show Form w/o saving data" )
        self.close()

    def addShowData(self):
        '''
        This method captures the data from the cnbcNewShowForm
        and creates and inserts a record into the Show Table.
        :return:
        '''
        # Log the Actions
        logger.debug ( "Saving New Show Data" )
        logger.debug ( "Leaving New Show Form" )

        # Check for Error conditions
        # Check for Required Moderator
        if self.comboBoxModerator.currentText ( ) == ' ':
            logger.debug ( 'Error in adding a new Show - No Moderator provided' )
            # build dialog
            msg = QMessageBox ( )
            msg.setIcon ( QMessageBox.Critical )
            msg.setText ( "<B><font color = red>No Moderator Provided - Record Error</B>" )
            msg.setInformativeText ( "No data in the Moderator field. This field must not be blank and is required." )
            msg.setWindowTitle ( "Show Record Error" )
            msg.setStandardButtons ( QMessageBox.Ok )
            msg.setDefaultButton ( QMessageBox.Ok )

            # show dialog
            retval = msg.exec_ ( )
            return

            # Check for Required Trader 1
        if self.comboBoxTrader1.currentText ( ) == ' ':
            logger.debug ( 'Error in adding a new Show - No Trader 1 provided' )
            # build dialog
            msg = QMessageBox ( )
            msg.setIcon ( QMessageBox.Critical )
            msg.setText ( "<B><font color = red>No Trader 1 Provided - Record Error</B>" )
            msg.setInformativeText ( "No data in the Trader 1 field. This field must not be blank and is required." )
            msg.setWindowTitle ( "Show Record Error" )
            msg.setStandardButtons ( QMessageBox.Ok )
            msg.setDefaultButton ( QMessageBox.Ok )

            # show dialog
            retval = msg.exec_ ( )
            return

         # Check for Required Trader 2
        if self.comboBoxTrader2.currentText ( ) == ' ':
            logger.debug ( 'Error in adding a new Show - No Trader 2 provided' )
            # build dialog
            msg = QMessageBox ( )
            msg.setIcon ( QMessageBox.Critical )
            msg.setText ( "<B><font color = red>No Trader 2 Provided - Record Error</B>" )
            msg.setInformativeText ( "No data in the Trader 2 field. This field must not be blank and is required." )
            msg.setWindowTitle ( "Show Record Error" )
            msg.setStandardButtons ( QMessageBox.Ok )
            msg.setDefaultButton ( QMessageBox.Ok )

            # show dialog
            retval = msg.exec_ ( )
            return

        with db_session:
            temp_var = self.dateEditCreatedDate.date()
            cd = temp_var.toPyDate ( )
            temp_var = self.dateEditShowDate.date()
            sd = temp_var.toPyDate ( )
            m = self.comboBoxModerator.currentText()
            t1 = self.comboBoxTrader2.currentText()
            t2 = self.comboBoxTrader2.currentText()
            t3 = self.comboBoxTrader3.currentText()
            t4 = self.comboBoxTrader4.currentText()
            c = self.comboBoxChartist.currentText()
            g = self.comboBoxGuest.currentText()
            s1 = self.lineEditSecurity1.text()
            s2 = self.lineEditSecurity2.text()
            s3 = self.lineEditSecurity3.text()
            s4 = self.lineEditSecurity4.text()
            s5 = self.lineEditSecurity5.text()
            a1 = self.checkBoxActive1.isChecked()
            a2 = self.checkBoxActive2.isChecked()
            a3 = self.checkBoxActive3.isChecked()
            a4 = self.checkBoxActive4.isChecked()
            a5 = self.checkBoxActive5.isChecked()
            sn = self.textEditShowNotes.toPlainText()
            s = 'Added the Show Date: {} to the Show Table'.format ( sd )
            logger.debug ( s )

            # Add the record
            p = Show ( createdDate=cd,
                       showDate = sd,
                       moderator = m,
                       trader1 = t1,
                       trader2 = t2,
                       trader3 = t3,
                       trader4 = t4,
                       chartist = c,
                       guest = g,
                       security1 = s1,
                       security2 = s2,
                       security3 = s3,
                       security4 = s4,
                       security5 = s5,
                       active1 = a1,
                       active2 = a2,
                       active3 = a3,
                       active4 = a4,
                       active5 = a5,
                       showNotes = sn)
            logger.debug ( "Leaving New Show Form after saving data" )
            self.close ( )

    def loadModerator(self):
        self.comboBoxModerator.addItem(" ")
        with db_session:
            for p in People.select ( lambda p: p.role == 'Moderator' ):
                self.comboBoxModerator.addItem(p.name)


    def loadChartist(self):
        self.comboBoxChartist.addItem ( " " )
        with db_session:
            for p in People.select ( lambda p: p.role == 'Chartist' ):
                self.comboBoxChartist.addItem ( p.name )

    def loadGuest(self):
        self.comboBoxGuest.addItem ( " " )
        with db_session:
            for p in People.select ( lambda p: p.role == 'Guest' ):
                self.comboBoxGuest.addItem ( p.name )

    def loadTrader(self):
        self.comboBoxTrader1.addItem ( " " )
        self.comboBoxTrader2.addItem ( " " )
        self.comboBoxTrader3.addItem ( " " )
        self.comboBoxTrader4.addItem ( " " )
        with db_session:
            for p in People.select ( lambda p: p.role == 'Trader' ):
                self.comboBoxTrader1.addItem ( p.name )
                self.comboBoxTrader2.addItem ( p.name )
                self.comboBoxTrader3.addItem ( p.name )
                self.comboBoxTrader4.addItem ( p.name )

    def peopleAdmin(self):
        # Call the peopleAdminForm
        self.f = PeopleAdmin()
        self.f.exec_ ( )

#TODO Refresh Database when coming from the cnbcPeopleAdminForm



