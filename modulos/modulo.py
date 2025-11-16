#modulo es para poder formar paquetes e ir implementando en distintos archivos


#tenemos modulos de python que fueron creados en c

#modulos de terceros


#formas de importar el modulo creado saludar

#luego del import es poner el nombre del archivo/modulo sin la extension .py

#con as podemos asignar nombre
import modulo_saludar as m_saludo


#si quisieramos solo sacar una funcion del modulo usamos
from modulo_saludar import hello

#si queremos importar mas de uno ponemos una , y el nombre de la otra funcion
from modulo_saludar import hello, hello_raro

#con el * importamos todo y podemos usar directamente las funciones
from modulo_saludar import * 

print(type(m_saludo))

saludo = m_saludo.hello("nahue")
print(saludo)