#importamos desde otra carpeta dentro del mismo directorio/ruta con el . conectamos



#importamos poniendole otro nombre al namespace
import funcionesAritmeticas.modulo_aritmeticas as m_aritmetica

print(m_aritmetica.Suma(2,4))



#importamos solo funciones
from funcionesAritmeticas.modulo_aritmeticas import Suma, Multiplicacion, Resta, Division

print(Suma(4,3))



#si la carpeta esta fuera del directorio/ruta se accede de otra forma

#primero importamos sys

import sys #modulo de python
import os

# Agregamos la carpeta externa al path
sys.path.append(r"C:\Users\Nahuel\Desktop\CODE 2025\python-curso\funcionesChau")

# Importamos el módulo con alias
import modulo_chau as m_chau

# Usamos su contenido
print(m_chau.Chau())


print(sys.path) #sacamos el directorio
print(os.path)
print(os.path.abspath)
print(os.path.dirname)