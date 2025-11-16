#creando diccionarios con dict()
diccionario = dict(nombre = "lucas", apellido = "jorge")

#las listas no pueden ser claves y usamos fronzenset para meter conjuntos

diccionario = {frozenset(["dalto", "rancio"]): "hola"}

#otra forma de crear diccionario
diccionario = {
    "nombre ": "nahuel",
    "apellido": "martinez"
}

#creando diccionarios con fromKeys() , para que no vaya por letra por letra, debemos ponerlo [ ]
diccionario = dict.fromkeys(["nombre","apellido"]) #nos pondria los valores en None por defecto

#dict.fromkeys() el primer dato es a lo que vamos a iterar y el segundo dato es al que le vamos asignar
diccionario = dict.fromkeys("ABCDE", "valores")
diccionario = dict.fromkeys(["nombre", "apellido"], "nahuel")

print(diccionario)