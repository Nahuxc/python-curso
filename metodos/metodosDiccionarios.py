#METODOS CON DICCIONARIOS (OBJETOS)

diccionario = {
    "id" : 1,
    "nombre" : "jorge",
    "apellido" : "martinez",
    "edad" : 23423,
    "estudianteActivo" : True

}

#metodos que podemos usar
# keys() -> devuelve las claves ej: nombre, id, edad
#get() -> devuelve el valor de una clave ej: 1 , jorge, martinez
#clear() -> elimina todos los elementos
# pop() -> elimina un elemento
# items() -> para iterar el dict



#keys devuelve objeto dict_item que se puede iterar

claves = diccionario.keys(); #de esta forma vemos las key, nos van a servir para iteraciones o busquedas

#print(claves)

#get obtenemos el valor indicando la clave por parametro
values = diccionario.get("nombre"); #sino lo encuentra tira none
#print(values)


#pop sacar un elemento del dicionario

diccionario.pop("nombre")
diccionario.pop("nombre", "apellido") #podemos sacar mas elementos


#items un elemento dict_items iterable

diccionario_iterable = diccionario.items()
print(diccionario_iterable)



#clear -> elimina todo del diccionario

diccionario.clear();
