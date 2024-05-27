#Modulos 
# Formas de importar 

#import NombreModulo o NombreFichero 
#Import M 

#Importarcion Parcial 
# from M Import NombreFuncion a importar
# from M import * (Todo)

# Ejemplo
import calendar
print (calendar.month(2024, 5))

print ('espacios') 

#Importamos el modulo de ejercicios 
import ejercicios

ejercicios.fib(1000)

ejercicios.__name__
'ejercicios'

#Si pretendemos utilizar una funcion frecuentemente le podems asignar un nombre local
fib = ejercicios.fib
fib (500)

#Importacion de manera parcial
from ejercicios import fib
fib (500)

#Importacion con *
from ejercicios import *
fib (500)

# Se utiliza para ligarlo a una varible
import ejercicios as fibo
fibo.fib(500)

#as importacion parcial 
from ejercicios import fib as fibonacci
fibonacci (800)

# Sys 
import sys 
print (sys.path)

print(' ')
print ('espacios')
print (' ')

# La funcion de Dir
print (dir(ejercicios))
print  (dir(sys))

print (' ')
print('Espacios')
print (' ')

a = [1, 2, 3, 4, 5]
import ejercicios

fib = ejercicios.fib
print (dir())

print (' ')
print('Espacios')
print (' ')

# Ejemplo con aritmetica
import ejemploaritmetica as arit
print (arit.suma(7, 5))
print (' ')

#Una sintaxis alternativa 
from ejemploaritmetica import suma
print(suma(7,5))

#Importsr parcial una a una
from ejemploaritmetica import suma, restar, mult, div

print(suma(7, 5))
print(restar(7, 5))
print(mult(7, 5))
print(div(7, 5))

#Importsr parcial una a una
from ejemploaritmetica import *

print(suma(7, 5))
print(restar(7, 5))
print(mult(7, 5))
print(div(7, 5))

#Importar ficheros dentro de paquetes
import matematica.aritmetica
print (matematica.aritmetica.suma(5,9))

"/Segunda forma/"
from matematica import aritmetica 
print (aritmetica.suma(5,9))

"""Tercera forma"""
from matematica.aritmetica import suma 
print(suma(9,5))



