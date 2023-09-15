# PyQt5 modules
from PyQt5 import QtWidgets



# Python modules
import sys

# Main window ui import
from src.MainWindow_ import MainWindow
from src.UART import readCOM


def main():
    readCOM()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



