import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QListWidgetItem
from PyQt5.uic import loadUi

class tablePage(QDialog):
    def __init__(self):

        super(tablePage, self).__init__()
        loadUi('tabla.ui', self)