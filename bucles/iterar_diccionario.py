dic = {
    "nombre": "majul",
    "apellido": "fernandez",
    "edad": 23
}

#asi sea lo que sea que pongamos solo sacamos la key
for key in dic:
    print(key)



#RECORRER DICCIONARIO OBTENIENDO CLAVE Y VALOR

#asi seria la forma de poner recorrer un diccionario con su clave y valor  /key y value


for datos in dic.items(): #para recordar: con items le indicamos que queremos los valores y la clave
    key = datos[0]
    value = datos[1]
    print(f"esta es la key: {key}  y este es su valor: {value}")