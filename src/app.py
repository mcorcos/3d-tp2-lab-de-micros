import threading
# PyQt5 modules
from PyQt5 import QtWidgets
# Python modules
import sys
# Main window ui import
from src.MainWindow_ import MainWindow 
from src.UART import readCOM ,detenerHiloCom



def main():

# Crea un hilo para la lectura del puerto COM1
    com_thread = threading.Thread(target=readCOM)
    com_thread.start()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # Conectar la señal aboutToQuit de la aplicación para detener el hilo
    app.aboutToQuit.connect(detenerHiloCom) 

    
    window.show()
    sys.exit(app.exec())



