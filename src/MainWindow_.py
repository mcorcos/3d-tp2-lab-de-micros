import threading

# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow 
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import QObject, pyqtSignal
# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.UART import DataCollectionThread , detenerHiloCom_data

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)   


         # Inicializa el hilo de recopilación de datos
        self.data_thread = DataCollectionThread()
        self.data_thread.data_ready_signal.connect(self.update_gui)  # Conecta la señal al método
        self.data_thread.start()




        # Conecta el evento de cierre de la ventana
        self.closeEvent = self.on_close_event


    def update_gui(self, packet_data):
        print("Signal received:", packet_data.id , packet_data.value_rolling)
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
        detenerHiloCom_data()
        event.accept()  # Acepta el evento de cierre

