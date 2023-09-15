# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow ,QFileDialog  , QListWidget ,QListWidgetItem , QVBoxLayout
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from threading import Thread

# Project modules
from ui.mainwindow import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)   



