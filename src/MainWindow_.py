import threading
import time
# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow 
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import QObject, pyqtSignal
# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.UART import Board , Board0 ,Board1 , Board2 ,Board3 ,Board4 ,Board5 ,Board6 

detener_hilo_data = True



def detenerHiloCom_data(self):
        global detener_hilo_data
        detener_hilo_data = False

class MainWindow(QMainWindow, Ui_MainWindow):


        def board_0_function(self):
                while detener_hilo_data:
                        self.RollLabel_0.setText(str(Board0.value_rolling))
                        self.TiltLabel_0.setText(str(Board0.value_tilt))
                        self.OrientationLabel_0.setText(str(Board0.value_orientation))
                        time.sleep(0.00125)  # Espera 50 ms (0.05 segundos)


        def board_1_function(self):
                while detener_hilo_data:
                        self.RollLabel_1.setText(str(Board1.value_rolling))
                        self.TiltLabel_1.setText(str(Board1.value_tilt))
                        self.OrientationLabel_1.setText(str(Board1.value_orientation))
                        time.sleep(0.00125)  # Espera 50 ms (0.05 segundos)

        def board_2_function(self):
                while detener_hilo_data:
                        self.RollLabel_2.setText(str(Board2.value_rolling))
                        self.TiltLabel_2.setText(str(Board2.value_tilt))
                        self.OrientationLabel_2.setText(str(Board2.value_orientation))
                        time.sleep(0.00125)  # Espera 50 ms (0.05 segundos)                      

        def board_3_function(self):
                while detener_hilo_data:
                        self.RollLabel_3.setText(str(Board3.value_rolling))
                        self.TiltLabel_3.setText(str(Board3.value_tilt))
                        self.OrientationLabel_3.setText(str(Board3.value_orientation))
                        time.sleep(0.00125)  # Espera 50 ms (0.05 segundos)

        def board_4_function(self):
                while detener_hilo_data:
                        self.RollLabel_4.setText(str(Board4.value_rolling))
                        self.TiltLabel_4.setText(str(Board4.value_tilt))
                        self.OrientationLabel_4.setText(str(Board4.value_orientation))
                        time.sleep(0.00125)  # Espera 50 ms (0.05 segundos)   

        def board_5_function(self):
                while detener_hilo_data:
                        self.RollLabel_5.setText(str(Board5.value_rolling))
                        self.TiltLabel_5.setText(str(Board5.value_tilt))
                        self.OrientationLabel_5.setText(str(Board5.value_orientation))
                        time.sleep(0.00125)  # Espera 50 ms (0.05 segundos)


        def board_6_function(self):
                while detener_hilo_data:
                        self.RollLabel_6.setText(str(Board6.value_rolling))
                        self.TiltLabel_6.setText(str(Board6.value_tilt))
                        self.OrientationLabel_6.setText(str(Board6.value_orientation))
                        time.sleep(0.00125)  # Espera 50 ms (0.05 segundos)






        def __init__(self):
                super(MainWindow, self).__init__()
                self.setupUi(self)   



                # Crear un objeto Thread





                # Conecta el evento de cierre de la ventana
                self.closeEvent = self.on_close_event


        def update_gui(self, packet_data):

                if(packet_data.id == 0):
                        self.RollLabel_0.setText(str(packet_data.value_rolling))
                        self.TiltLabel_0.setText(str(packet_data.value_tilt))
                        self.OrientationLabel_0.setText(str(packet_data.value_orientation))
                if(packet_data.id == 1):
                        self.RollLabel_1.setText(str(packet_data.value_rolling))
                        self.TiltLabel_1.setText(str(packet_data.value_tilt))
                        self.OrientationLabel_1.setText(str(packet_data.value_orientation))
                if(packet_data.id == 2):
                        self.RollLabel_2.setText(str(packet_data.value_rolling))
                        self.TiltLabel_2.setText(str(packet_data.value_tilt))
                        self.OrientationLabel_2.setText(str(packet_data.value_orientation))
                if(packet_data.id == 3):
                        self.RollLabel_3.setText(str(packet_data.value_rolling))
                        self.TiltLabel_3.setText(str(packet_data.value_tilt))
                        self.OrientationLabel_3.setText(str(packet_data.value_orientation))
                if(packet_data.id == 4):
                        self.RollLabel_4.setText(str(packet_data.value_rolling))
                        self.TiltLabel_4.setText(str(packet_data.value_tilt))
                        self.OrientationLabel_4.setText(str(packet_data.value_orientation))
                if(packet_data.id == 5):
                        self.RollLabel_5.setText(str(packet_data.value_rolling))
                        self.TiltLabel_5.setText(str(packet_data.value_tilt))
                        self.OrientationLabel_5.setText(str(packet_data.value_orientation))
                if(packet_data.id == 6):
                        self.RollLabel_6.setText(str(packet_data.value_rolling))
                        self.TiltLabel_6.setText(str(packet_data.value_tilt))
                        self.OrientationLabel_6.setText(str(packet_data.value_orientation))



        def on_close_event(self, event: QCloseEvent):
                # Maneja el evento de cierre de la ventana
                # Detiene el hilo antes de cerrar la ventana
                detenerHiloCom_data(self)
                event.accept()  # Acepta el evento de cierre
        

