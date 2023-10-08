import serial 
import sys
from PyQt5.QtCore import QObject, pyqtSignal , QThread
import time

#--------------------------------------------------------------
#           ENUM
#----------------------------------------------------------------
#no se como hcaer defines en python 

ID = 0
ID_NUMBER1 = 1
ID_NUMBER2 = 2
ID_NUMBER3 = 3
SIGN_ROLL = 4
ROLL1 = 5
ROLL2 = 6
ROLL3 = 7
SIGN_TILT = 8
TILT1 = 9
TILT2 = 10
TILT3 = 11
SIGN_OR = 12
ORIENTATION1 = 13
ORIENTATION2 = 14
ORIENTATION3 = 15
TERMINATOR = 16
SLASH_N = 17
PACK_LEN = 3

# termino de hacer el enum

#--------------------------------------------------------------
#           CLASES
#----------------------------------------------------------------

class Board:
    def __init__(self, id, value_rolling, value_tilt, value_orientation):
        self.id = id
        self.value_rolling = value_rolling
        self.value_tilt = value_tilt
        self.value_orientation = value_orientation

# Crear una instancia de la clase
Board0 = Board(id=0, value_rolling=0, value_tilt=1, value_orientation=0)
Board1 = Board(id=1, value_rolling=0, value_tilt=2, value_orientation=0)
Board2 = Board(id=2, value_rolling=0, value_tilt=3, value_orientation=0)
Board3 = Board(id=3, value_rolling=0, value_tilt=4, value_orientation=0)
Board4 = Board(id=4, value_rolling=0, value_tilt=5, value_orientation=0)
Board5 = Board(id=5, value_rolling=0, value_tilt=6, value_orientation=0)
Board6 = Board(id=6, value_rolling=0, value_tilt=7, value_orientation=0)
Board7 = Board(id=7, value_rolling=0, value_tilt=8, value_orientation=0)



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
            time.sleep(0.01)  # Espera durante el intervalo especificado

    except KeyboardInterrupt:
        # Cierra el puerto COM cuando se interrumpe el programa (Ctrl+C)
        print(f"KeyboardInterrupt")
        
    except serial.SerialException as e:
        # Maneja la excepción si no se puede abrir el puerto COM1
        print(f"No se pudo abrir el puerto COM1: {e}")
    except Exception as e:
        # Maneja otras excepciones que puedan ocurrir
        print(f"Ocurrió un error inesperado: {e}")
   # finally:
      #  ser.close()  # Asegura que se cierre el puerto COM1 en caso de excepción




# Función para procesar los datos recibidos
def process_data(data):  # los datos son [ID , id , + , Val_roll , + , Val_tilt , - , Val_or , T , '\n']  puede ser + o -
    data_len = len(data) #el tamanio tiene que ser 9 + el terminador 

    # Verifica si los datos tienen al menos el tamaño mínimo esperado
    if( data_len == (SLASH_N +1)  ):
        if((data[ID] == 'I') and (data[SIGN_ROLL] == '+') or( data[SIGN_ROLL] == '-' )and (data[TERMINATOR] == 'T') ):
            
            
            if(data[SIGN_ROLL] == '+' ):
                temp = data[ROLL1:ROLL1+PACK_LEN]
                temp_rolling = charsArrayToByte(temp)  # Obtiene el valor numérico
            else:
                temp = data[ROLL1:ROLL1+PACK_LEN]
                temp_rolling = (-1)*(charsArrayToByte(temp))


            if(data[SIGN_TILT] == '+' ):
                temp = data[TILT1:TILT1+PACK_LEN]
                temp_tilt = charsArrayToByte(temp)  # Obtiene el valor numérico
            else:
                temp = data[TILT1:TILT1+PACK_LEN]
                temp_tilt = (-1)*(charsArrayToByte(temp))


            if(data[SIGN_OR] == '+' ):
                temp = data[ORIENTATION1:ORIENTATION1+PACK_LEN]
                temp_orientation = charsArrayToByte(temp)  # Obtiene el valor numérico
            else:
                temp = data[ORIENTATION1:ORIENTATION1+PACK_LEN]
                temp_orientation = (-1)*(charsArrayToByte(temp))

            temp = data[ID_NUMBER1:ID_NUMBER1+PACK_LEN]
            packet.id = charsArrayToByte(temp)

            if(packet.id == 0):
                Board0.value_rolling = temp_rolling
                Board0.value_tilt = temp_tilt
                Board0.value_orientation = temp_orientation
            
            if(packet.id == 1):
                Board1.value_rolling = temp_rolling
                Board1.value_tilt = temp_tilt
                Board1.value_orientation = temp_orientation
            
            if(packet.id == 2):
                Board2.value_rolling = temp_rolling
                Board2.value_tilt = temp_tilt
                Board2.value_orientation = temp_orientation
            if(packet.id == 3):
                Board3.value_rolling = temp_rolling
                Board3.value_tilt = temp_tilt
                Board3.value_orientation = temp_orientation
            if(packet.id == 4):
                Board4.value_rolling = temp_rolling
                Board4.value_tilt = temp_tilt
                Board4.value_orientation = temp_orientation

            if(packet.id == 5):
                Board5.value_rolling = temp_rolling
                Board5.value_tilt = temp_tilt
                Board5.value_orientation = temp_orientation

            if(packet.id == 6):
                Board6.value_rolling = temp_rolling
                Board6.value_tilt = temp_tilt
                Board6.value_orientation = temp_orientation





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



# class DataCollectionThread(QThread):
#     data_ready_signal = pyqtSignal(object)  # Señal personalizada para enviar datos


#     def __init__(self):
#         super().__init__()
#         self.interval = 0.01  # Intervalo de tiempo en segundos

#     def run(self):
#         while not detener_hilo_data:
#             # Recopila datos en la variable Packet
#             packet_data = self.collect_data()  # Reemplaza con tu lógica de recopilación de datos
#             self.data_ready_signal.emit(packet_data)
#             time.sleep(self.interval)  # Espera durante el intervalo especificado


#     def collect_data(self):
#             return packet


# # Función para detener el hilo de lectura del puerto COM1
# def detenerHiloCom_data():
#     global detener_hilo_data
#     detener_hilo_data = True


def charsArrayToByte(chars_array):

    digit1 = int(chars_array[0])
    digit2 = int(chars_array[1])
    digit3 = int(chars_array[2])

    if digit1 < 0 or digit1 > 9 or digit2 < 0 or digit2 > 9 or digit3 < 0 or digit3 > 9:
        raise ValueError("Los elementos del arreglo deben ser dígitos del 0 al 9")

    byte = digit1 * 100 + digit2 * 10 + digit3
    if byte > 255:
        raise ValueError("El valor resultante excede 255")

    return byte


