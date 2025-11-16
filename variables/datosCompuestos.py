#TIPOS DE DATOS COMPUESTOS (son datos que tienen adentro otros datos)

#lista / matriz
lista = ["banana", "manzana","pera", 2432] #tenemos 3 elementos se cuentan desde la posicion 0 1 2

# 0 : banana
# 1 : manzana
# 2 : pera

#de esta manera accedemos al dato poniendo su posicion 0
print(lista[0]) #output: banana
#de esta manera accedemos al dato poniendo su posicion 1
print(lista[1]) #output: manzana
#de esta manera accedemos al dato poniendo su posicion 2
print(lista[2]) #output: pera



#aca accedemos mediante un bucle for utilizando listaObjeto para que muestre cada uno de los que estan en la lista accede a su indice automaticamente

#for listaObjeto in lista :
#    print(listaObjeto)

print("=================================")


#la tupla no se puede modificar a diferencia que las listas si
tupla = ("kiwi", "anana")

print(tupla[0])
print(tupla[1])


print("=================================")

#creando un conjunto set se pueden cambiar de lugar pero no podemos modificar elementos


conjunto = {"nombre", "apellido"}


#para acceder no se accede por indice y no te permite repetir valores

print(conjunto)

#para acceder tenemos que usar un bucle

for datos in conjunto :
    print(f"se accedio al dato: {datos} ")


print("=================================")

#creando un diccionario

#es como crear un json para mostrarlo lo mostramos por su nombreValor asignado y da su valor

#esto es key : value
diccionario = {
    #key : value de esta forma se estructura 
    'nombre': 'nahue',
    'canal': 'znahuex',
    'edad' : 23,
    'actividad' : True
}

print(diccionario['nombre'])
print(diccionario['canal'])
print(diccionario['edad'])
print(diccionario['actividad'])
