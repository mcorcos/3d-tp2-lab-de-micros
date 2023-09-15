import serial as sr

# Configura el puerto COM y la velocidad de baudios (baud rate)
puerto_com = 'COM11'  # Reemplaza con el nombre de tu puerto COM . hay que chequear en Device Manager
velocidad_baudios = 9600  # Reemplaza con la velocidad de baudios correcta

# Abre el puerto COM
ser = sr.Serial(puerto_com, velocidad_baudios)

def readCOM(ser):
    try:
        while True:
            # Lee una línea de datos desde el puerto COM
            linea_de_datos = ser.readline()
            print(linea_de_datos.decode('utf-8'))  # Decodifica los bytes a texto (ajusta el encoding según tus necesidades)
    except KeyboardInterrupt:
        # Cierra el puerto COM cuando se interrumpe el programa (Ctrl+C)
        ser.close()

