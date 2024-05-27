"/Sys : Funciones y parametros especificos del sistema operativo/"
import sys

"/Os: Interfaz con el sistema operativo/"
import os 

"/Os.path: Funciones de acceso a las rutas del sistema/"
import os.path

"/Io: Oara manejo de flujo de datos y ficheros/"
import io

"/String: Cadena de caracteres/"
import string

"/Datetime: Fechas y tiempos/"
import datetime

"/Math: Funciones matematicas/"
import math

"/Statistics: Funciones con estadisticas/"
import statistics

"/Random: Numeros aleatorios/"
import random

"/Ejemplos para entender/"

"/Ejemplo de uso de la libreria sys/"
print(sys.platform) #Imprime el nombre de la plataforma que estamos ejecutando

#os
print(os.listdir('/')) # Imprime el nombre de los archivos y del raiz del sistema

#os.path
ruta_absoluta = os.path.abspath('lectura.txt') #Obtiene la ruta absoluta del archivo
print(ruta_absoluta)

#io abrir y leer un archivo
with io.open('lectura.txt', 'r') as f:
    contenido = f.read()
    print(contenido)

#String
print(string.ascii_lowercase) #Abecedario en minuscula

#Datetime
fecha_actual = datetime.datetime.now()
print (fecha_actual) # Imprime la fecha actual

#Math
print(math.sqrt(16)) #Raiz cuadrada

# Statitistics
datos = [1, 2, 3, 4, 5]
print(statistics.mean(datos))

#Random
print(random.randint(1, 100)) # Numero random de 1 a 100




