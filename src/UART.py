import serial 
import sys
from PyQt5.QtCore import QObject, pyqtSignal , QThread
import time

#--------------------------------------------------------------
#           ENUM
#----------------------------------------------------------------
#no se como hcaer defines en python 

ID = 0
ID_NUMBER = 1
SIGN_ROLL = 2
ROLL = 3
SIGN_TILT = 4
TILT = 5
SIGN_OR = 6
ORIENTATION = 7
TERMINATOR = 9
SLASH_N = 10

# termino de hacer el enum

#--------------------------------------------------------------
#           CLASES
#----------------------------------------------------------------



# Estructura para almacenar los datos recibidos
class DataPacket:
    def __init__(self, id = 0,value_rolling=0 ,value_tilt=0  ,value_orientation=0 ) :
        self.id = id  # ID del dato
        self.value_rolling = value_rolling  # Valor (0-360)
        self.value_tilt = value_tilt
        self.value_orientation = value_orientation





#--------------------------------------------------------------
#           OBJETO
#----------------------------------------------------------------
packet = DataPacket(id= 0 , value_rolling= 0 , value_tilt= 0 , value_orientation= 0 )

#--------------------------------------------------------------
#           FUNCIONES
#----------------------------------------------------------------
detener_hilo = False

def readCOM():
    try:
        # Abre el puerto COM1 con un baudrate de 9600
        ser = serial.Serial('COM1', baudrate=9600)

        # Realiza las operaciones que necesitas en el puerto COM1 aquí

        while not detener_hilo:
            # Lee una línea de datos desde el puerto COM
            linea_de_datos = ser.readline().decode('utf-8')
            process_data(linea_de_datos)
            print("Raw data" , linea_de_datos)  # Decodifica los bytes a texto (ajusta el encoding según tus necesidades)
            sys.stdout.flush()
            time.sleep(2)  # Espera durante el intervalo especificado

    except KeyboardInterrupt:
        # Cierra el puerto COM cuando se interrumpe el programa (Ctrl+C)
        print(f"KeyboardInterrupt")
        
    except serial.SerialException as e:
        # Maneja la excepción si no se puede abrir el puerto COM1
        print(f"No se pudo abrir el puerto COM1: {e}")
    except Exception as e:
        # Maneja otras excepciones que puedan ocurrir
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        ser.close()  # Asegura que se cierre el puerto COM1 en caso de excepción




# Función para procesar los datos recibidos
def process_data(data):  # los datos son [ID , id , + , Val_roll , + , Val_tilt , - , Val_or , T , '\n']  puede ser + o -
    data_len = len(data) #el tamanio tiene que ser 9 + el terminador 

    # Verifica si los datos tienen al menos el tamaño mínimo esperado
    if( data_len == SLASH_N  ):
        if((data[ID] == 'I') and (data[SIGN_ROLL] == '+') or( data[SIGN_ROLL] == '-' )and (data[TERMINATOR] == 'T') ):
            id = int(data[ID_NUMBER])  # Obtiene el ID del dato
            if(data[SIGN_ROLL] == '+' ):
                temp_rolling = char_to_decimal(data[ROLL])  # Obtiene el valor numérico
            else:
                temp_rolling = (-1)*(char_to_decimal(data[ROLL]))
            if(data[SIGN_TILT] == '+' ):
                temp_tilt = char_to_decimal(data[TILT])  # Obtiene el valor numérico
            else:
                temp_tilt = (-1)*(char_to_decimal(data[TILT]))
            if(data[SIGN_OR] == '+' ):
                temp_orientation = char_to_decimal(data[ORIENTATION])  # Obtiene el valor numérico
            else:
                temp_orientation = (-1)*(char_to_decimal(data[ORIENTATION]))

            packet.id = data[ID_NUMBER]
            packet.value_rolling = temp_rolling
            packet.value_tilt = temp_tilt
            packet.value_orientation = temp_orientation

            # Realiza alguna acción con el paquete de datos, como imprimirlo
            print(f"Processed Data = ID: {packet.id}, temp_rolling: {packet.value_rolling}, temp_tilt: {packet.value_tilt}, temp_orientation: {packet.value_orientation}")   

# Función para detener el hilo de lectura del puerto COM1
def detenerHiloCom():
    global detener_hilo
    detener_hilo = True

#Utility func
def char_to_decimal(char):
    return ord(char)



class DataCollectionThread(QThread):
    data_ready_signal = pyqtSignal(object)  # Señal personalizada para enviar datos


    def __init__(self):
        super().__init__()
        self.interval = 2  # Intervalo de tiempo en segundos

    def run(self):
        while True:
            # Recopila datos en la variable Packet
            packet_data = self.collect_data()  # Reemplaza con tu lógica de recopilación de datos
            self.data_ready_signal.emit(packet_data)
            time.sleep(self.interval)  # Espera durante el intervalo especificado


    def collect_data(self):
            return packet


