#!/usr/bin/env python3.4

# Author - KO . All rights reserved.
__author__ = 'ko'

import logging.config

logging.config.fileConfig('./Support/logging.conf')              # create and configure logger
logger = logging.getLogger('CNBC.NewShowForm')                   # Set Logger Prefix column

from PyQt5.QtWidgets import QWidget, QAction, QStatusBar, QMenu, QDialog
from newShowFormDialog import Ui_newShowDialog
from PyQt5.QtCore import  QDate
import psycopg2
from pony.orm import *
from cnbcPeopleAdminForm import PeopleAdmin

db = Database ( )

# Create the Database entities

class People(db.Entity):
    name = Required(str)
    role = Required(str)

# PostgreSQL
db.bind ( 'postgres', user='ko', password='morgan', host='localhost', database='moaa' )

db.generate_mapping(create_tables=True)

with db_session:
    '''
    p =  People ( name='Donald Trump', role = "Moderator")
    p1 = People ( name='Hillary Clinton', role = "Guest" )
    p2 = People ( name='Bob Hope', role = "Trader")
    p3 = People ( name='KO Hanlon', role = "Trader" )
    p4 = People ( name='Billy Bob', role = "Trader")
    p5 = People ( name='Ron Caroon', role = "Chartist" )
    p6 = People ( name='Johnny Carson', role = "Moderator")
    p7 = People ( name='Susan Hanlon', role = "Chartist" )
    '''

class NewShowForm(Ui_newShowDialog, QDialog):
    db = Database ( )

    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi ( self )
        self.startUp()

        # Log Actions
        logger.debug ( "Initializing New Show Form")

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
        self.lineEdiSecurity1.clear()
        self.lineEdiSecurity2.clear()
        self.lineEdiSecurity3.clear()
        self.lineEdiSecurity4.clear()
        self.lineEdiSecurity5.clear()
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
        logger.debug ( "Saving New Show Data" )
        logger.debug ( "Leaving New Show Form" )

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


#TODO Provide ability to Add, Edit and Delete People Table entities


