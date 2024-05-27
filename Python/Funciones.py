
"""
#EXPO HYRUM

#Funciones: Bloque de codigo que tiene un nombre al cual le asignamos unos procesos
#Se llama en el main par horrar tiempo y codigo

'''def <nombrefuncion>(<paramer>)
return '''

# Ejemplo funcion bienvenido

def bienvenida (nombre ):
    print("¡ Bienvenido a python" , nombre , "!!!")
    return (nombre)

print(type(bienvenida))
bienvenida('Camilo')

# Ejemplo con dos argumentos pocisionales

def bienvenida (nombre, apellido ):
    print("¡ Bienvenido a python" , nombre , apellido, "!!!")
    return (nombre)

print(type(bienvenida))
bienvenida('Camilo', 'Rincon')

# Argumentos nominales

# No importan el orden por que estoy nombrando cada uno
bienvenida(apellido = 'Rincon', nombre = 'Camilo')

# Return

def area_rectangulo (base, altura):
    return base * altura / 2

print (area_rectangulo(5, 7))

#_______________________________________________________________________________"""



"""#Expo Vocera

#Argumentaion predeterminada

def bienvenidos (nombre, lenguaje = "python"):
    print ("! Bienvenido a ", lenguaje, nombre, "!")
    return

bienvenidos ("Crack")
bienvenidos ("Crack", "Java")

# Argumentacion indeterminada

def menu (*platos):
    print ('Hoy tenemos: ', end='')
    for plato in platos:
        print (plato, end=', ')
    return

menu ('pasta', 'pizza', 'ensaladas')

#Ambitos de los parametros y variables de una funcion 

#Ambito local: Dentro de la funcion
#Ambito global: Fuera de la funcion 

lenguaje = "Java"
def bienvenido (nombre):
    lenguaje = "python"
    print ("\n !Bienvenido a ", lenguaje, nombre, "!")
    return

bienvenido (nombre = "Crack")
print ("Crack")

#Paso de argumentos por referencia 

primer_curso = ['Matematicas', 'Fisica']
print (primer_curso)

def añade_asignatura (curso, asignatura):
    curso.append(asignatura)
    return

añade_asignatura(primer_curso , 'Quimica')

print (primer_curso)
"""
#______________________________________________________________________________
#Expo Duvan

#Documentacion de funciones

#def sumar (a, b):
    
""" Funcion para sumar dos valores.
    Parametros:
    Valor a: Un numero entero o real
    Valor b: un numero entero o real
    Salida:
    Un numero entero o real con la suma de los dos valores
    """
   # return a + b
'''print(sumar(12, 21))
print(sumar.__doc__)

# print (help(sumar))

# Recursividad

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print (factorial(10))

# Recursividad multiple

def fibonacci (n):
    if n <= 1:
        return n
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)
    
print (fibonacci(10))


def fibonnacci (n):
    a = 0
    b = 1
    
    for i in range(n):
        c = a + b
        a = b
        b = c
    return b

print (fibonnacci(100))
    '''
'''#_______________________________________________________________________
#Rafael

#zip

asigaturas = ['Matematicas', 'Fisica', 'Quimica', 'Economia']

notas = [6.0, 3.5, 7.5, 8.0]

print (list(zip(asigaturas, notas))) 

from functools import reduce
def producto (n, m):
    return n+m

print (reduce (producto, range (1, 5)))

cad = ['C', 'i', 'n', 'c', 'o']

print (reduce (producto, cad))

#Creacion de diccionarios elegantes
cuadrado = {x: x**2 for x in range(10)}
print(cuadrado)

#Creacion de listas
redondo = [ (x*1 for x in range (10)), (x**2 for x in range (10))]
print(redondo)'''

#_________________________________________________
# Hamilton

#Ficheros 

#Archivo que contiene datos en un sistema 
#Con o sin with
#Tipos de escritura
# R leer
#W WRITEN "ESCRIBIR"
# W+ LEER Y ESCRIBIR
# A escribir al final

#su usan para Almacenar datos en el disco duro

#CREAr

'''archivo = open ('Fichero.txt', 'r')
contenido = archivo.read()
print (contenido)
archivo.close()'''

"""with open ('Fichero.txt', 'w') as archivo:
    archivo.write("YZ 450")"""
    
"""archivo = open ('Motos.txt', 'a')
archivo.write("YZ 125 \n")
archivo.close()"""
    
"""archivo = open ('Motos.txt', 'r')
contenido = archivo.read()
archivo.close()    

print (contenido)"""

#___________________________________________
# Sebastian 

# Crear

f=open("bienvenido.txt", 'w')