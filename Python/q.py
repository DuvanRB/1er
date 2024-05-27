#___________________________________________
# Sebastian 

# Crear

"""f=open("bienvenido.txt", 'w')

#Añadir

f.write("bienvenidos a python")

#Cerrar

f.close()

#renombrar

import os
f="bienvenido.txt"
if os.path.isfile(f):
    os.rename(f, "python.txt")
else:
    print ("¡ El fichero ", f , " no existe !")"""
  
import os  
f="python.txt"
if os.path.isfile(f):
    os.remove(f)
else:
    print ("¡ El fichero ", f , " no existe !")