#!/usr/bin/env python3.4

# Author - KO . All rights reserved.
__author__ = 'ko'

import logging.config

logging.config.fileConfig('./Support/logging.conf')              # create and configure logger
logger = logging.getLogger('CNBC.PeopleAdmin')                   # Set Logger Prefix column

from PyQt5.QtWidgets import QWidget, QDialog, QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox
from PeopleAdminFormDialog import Ui_FormPeopleAdministration

import psycopg2
from pony.orm import *

db = Database ( )

# Create the Database entities

class People(db.Entity):
    name = Required(str)
    role = Required(str)

# PostgreSQL
db.bind ( 'postgres', user='ko', password='morgan', host='localhost', database='moaa' )

db.generate_mapping(create_tables=True)


class PeopleAdmin(Ui_FormPeopleAdministration, QDialog):
    db = Database ( )

    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi ( self )

        # Log Actions
        logger.debug ( 'Initializing Person Table Form' )
        self.startup()

        # Set up Connections
        self.pushButtonClose.clicked.connect ( self.setClose)
        self.pushButtonChange.clicked.connect ( self.setChange)
        self.tableWidgetPeople.cellClicked.connect ( self.cellWasClicked )


    def setClose(self):
        '''
        This method closes dialog
        :return:
        '''
        self.close()

    def setChange(self):
        '''
        This method makes changes to People Table based on the
        checked radio button
        :return:
        '''
        # Check for Name Error
        if len ( self.lineEditName.text ( ) ) == 0:
            # If no Name provided - notify user
            logger.debug ( 'Error in adding a new Record - No name provided' )
            # build dialog
            msg = QMessageBox ( )
            msg.setIcon ( QMessageBox.Critical )
            msg.setText ( "<B><font color = red>No Name Provided - Record Error</B>" )
            msg.setInformativeText ( "No data in the Name field. This field must not be blank and is required." )
            msg.setWindowTitle ( "People Record Error" )
            msg.setStandardButtons ( QMessageBox.Ok )
            msg.setDefaultButton ( QMessageBox.Ok )

            # show dialog
            retval = msg.exec_ ( )
            return

        if self.comboBoxRole.currentText() == '':
            # If no Role provided - notify user
            logger.debug ( 'Error in adding a new Record - No role provided' )
            # build dialog
            msg = QMessageBox ( )
            msg.setIcon ( QMessageBox.Critical )
            msg.setText ( "<B><font color = red>No Role Provided - Record Error</B>" )
            msg.setInformativeText ( "No data in the Role field. This field must not be blank and is required." )
            msg.setWindowTitle ( "People Record Error" )
            msg.setStandardButtons ( QMessageBox.Ok )
            msg.setDefaultButton ( QMessageBox.Ok )

            # show dialog
            retval = msg.exec_ ( )
            return
        # Add a record if the radioActive is checked AND the change button is clicked
        if self.radioButtonAdd.isChecked():
            # Add record Action
            with db_session:
                # Log the action
                nm = self.lineEditName.text ( )
                rl = self.comboBoxRole.currentText()
                s = 'Added the Name: {} with a Role: {} to the People Table'.format ( nm, rl )
                logger.debug ( s )

                # Add the record
                p = People ( name=nm, role=rl )
                # Update the table
                self.buildTable ( )

        if self.radioButtonDelete.isChecked():
            # Delete record Action
            with db_session:
                # Log the action
                nm = self.lineEditName.text ( )
                rl = self.comboBoxRole.currentText()
                s = 'Deleted the Name: {} with a Role: {} from the People Table'.format ( nm, rl )
                logger.debug ( s )

                # Delete the record
                p = People ( name=nm, role=rl )
                delete ( p for p in People if p.name == nm and p.role == rl)
                # Repopulate name and role lineEdit controls
                row = 0
                c = self.tableWidgetPeople.item ( row, 0)
                n = self.tableWidgetPeople.item ( row, 1 )
                r = self.tableWidgetPeople.item ( row, 2 )
                self.lineEditName.setText ( n.text ( ) )
                self.comboBoxRole.setCurrentText(r.text())
                self.lineEditID.setText ( c.text() )
                # Update the table
                self.buildTable ( )

        if self.radioButtonEdit.isChecked():
            # Edit record Action
            with db_session:
                # Log the action
                nm = self.lineEditName.text ( )
                rl = self.comboBoxRole.currentText ( )
                s = 'Edited the Name: {} with a Role: {} Record in People Table'.format ( nm, rl )
                logger.debug ( s )

                # Edit the record
                peepsNum = int(self.lineEditID.text())
                peeps = People[peepsNum]
                peeps.set ( name= nm, role=rl )

                # Repopulate name and role lineEdit controls
                row = 0
                c = self.tableWidgetPeople.item ( row, 0 )
                n = self.tableWidgetPeople.item ( row, 1 )
                r = self.tableWidgetPeople.item ( row, 2 )
                self.lineEditName.setText ( n.text ( ) )
                self.comboBoxRole.setCurrentText ( r.text ( ) )
                self.lineEditID.setText ( c.text() )
                # Update the table
                self.buildTable ( )

    def startup(self):
        '''
        This method queries the Database People table and
        populates the list view widget, putting on record per line
        :return:
        '''
        self.buildTable()


    def cellWasClicked(self, row, column):
        '''
        This method (a slot) responds to clicks within the
        tableWidgetPeople.
        it parses the row data and sends appropiate data to
        th ecorespondng line edits.
        :param row:
        :param column:
        :return:
        '''
        c = self.tableWidgetPeople.item ( row, 0)
        n = self.tableWidgetPeople.item ( row, 1)
        r = self.tableWidgetPeople.item ( row, 2)
        self.lineEditName.setText(n.text())
        self.comboBoxRole.setCurrentText ( r.text ( ) )
        self.lineEditID.setText(c.text())

    def buildTable(self):
        with db_session:
            # Set the Table
            TotalRowCount = count ( c for c in People )
            self.tableWidgetPeople.setRowCount ( TotalRowCount )
            self.tableWidgetPeople.setColumnCount ( 3 )
            self.tableWidgetPeople.setHorizontalHeaderLabels ( ['ID', 'Name', 'Role'] )
            self.tableWidgetPeople.setStyleSheet ( "QTableView {selection-background-color: QColor ( 0, 0, 255, 127)}" )
            self.tableWidgetPeople.setSelectionBehavior ( QAbstractItemView.SelectRows )
            self.tableWidgetPeople.horizontalHeader ( ).setStretchLastSection ( True )

            # Populate the table
            row = 0
            for p in range ( TotalRowCount ):
                while row <= TotalRowCount:
                    for p in select ( p for p in People ):
                        self.tableWidgetPeople.setItem ( row, 0, QTableWidgetItem ( str(p.id) ) )
                        self.tableWidgetPeople.setItem ( row, 1, QTableWidgetItem ( p.name ) )
                        self.tableWidgetPeople.setItem ( row, 2, QTableWidgetItem ( p.role ) )
                        row = row + 1
