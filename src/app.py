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

    board_0_Thread = threading.Thread(target=MainWindow.board_0_function , args= (window,))
    board_0_Thread.start()
    board_1_Thread = threading.Thread(target=MainWindow.board_1_function , args= (window,))
    board_1_Thread.start()
    board_2_Thread = threading.Thread(target=MainWindow.board_2_function , args= (window,))
    board_2_Thread.start()
    board_3_Thread = threading.Thread(target=MainWindow.board_3_function , args= (window,))
    board_3_Thread.start()
    board_4_Thread = threading.Thread(target=MainWindow.board_4_function , args= (window,))
    board_4_Thread.start()
    board_5_Thread = threading.Thread(target=MainWindow.board_5_function , args= (window,))
    board_5_Thread.start()
    board_6_Thread = threading.Thread(target=MainWindow.board_6_function , args= (window,))
    board_6_Thread.start()
    board_7_Thread = threading.Thread(target=MainWindow.board_7_function , args= (window,))
    board_7_Thread.start()



    # Conectar la señal aboutToQuit de la aplicación para detener el hilo
    app.aboutToQuit.connect(detenerHiloCom) 

    
    window.show()
    sys.exit(app.exec())



