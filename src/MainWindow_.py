import threading

# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow 
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import QObject, pyqtSignal
# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.UART import DataCollectionThread

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)   


        for placa_id in range(7):
            RollLabel = f'RollLabel_{placa_id}'
            TiltLabel = f'TiltLabel_{placa_id}'
            OrientationLabel = f'OrientationLabel_{placa_id}'

            
            # Crear y conectar
            label = QLabel("50")
            setattr(self, RollLabel, label)
            setattr(self, TiltLabel, label)
            setattr(self, OrientationLabel, label)





         # Inicializa el hilo de recopilación de datos
        self.data_thread = DataCollectionThread()
        self.data_thread.data_ready_signal.connect(self.update_gui)  # Conecta la señal al método
        self.data_thread.start()




        # Conecta el evento de cierre de la ventana
        self.closeEvent = self.on_close_event


    def update_gui(self, packet_data):
        print("Signal received:", packet_data.id , packet_data.value_rolling)
    # Actualiza los campos de texto en la GUI para la placa especificada
        # text_edit_rolling = getattr(self, f'RollLabel_{packet_data.id}')
        # text_edit_tilt = getattr(self, f'TiltLabel_{packet_data.id}')
        # text_edit_orientation = getattr(self, f'OrientationLabel_{packet_data.id}')

        # text_edit_rolling.setText(str(packet_data.value_rolling))
        # text_edit_tilt.setText(str(packet_data.value_tilt))
        # text_edit_orientation.setText(str(packet_data.value_orientation))
        text_edit_rolling = getattr(self, f'RollLabel_0')
        text_edit_tilt = getattr(self, f'TiltLabel_0')
        text_edit_orientation = getattr(self, f'OrientationLabel_0')
       
        text_edit_rolling.setText(str(packet_data.value_rolling))
        text_edit_tilt.setText(str(packet_data.value_tilt))
        text_edit_orientation.setText(str(packet_data.value_orientation))
        self.RollLabel_0.setText(str(packet_data.value_rolling))

    def stop_data_thread(self):
        # Detiene el hilo de recopilación de datos de manera controlada
        self.data_thread.stop()

    def on_close_event(self, event: QCloseEvent):
        # Maneja el evento de cierre de la ventana
        # Detiene el hilo antes de cerrar la ventana
        self.stop_data_thread()
        event.accept()  # Acepta el evento de cierre

