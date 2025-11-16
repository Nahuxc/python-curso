###### BUCLES ##########

#funciona para lista, tuplas y sets

#BUCLE FOR

lista = [1,2,3,4,5,6]
animales = ["bellena", "cocodrilo", "ave"]




print("##### BUCLE NORMAL CON ITERAR VALORES #########")
for nums in lista:
    print(nums)





print("############con zip 2 listas juntas del mismo tamaño################")
#para iterar 2 listas juntas del mismo tamaño con la funcion zip
for numero, animal in zip(lista, animales):
    print(numero)
    print(animal)




print("############con rannge  1################")
#iterar numeros utilizando la funcion range itera desde el 5 hasta el 9
for num in range(5,10):
    print(num)




print("############con rannge  2################") #NO ES UNA FORMA OPTIMA DE RECORRER UNA LISTA CON INDICE MALA PRACTICA
#funcionamiento en una lista poniendo el indice
for num in range(len(lista)): #esto arranca de 0 a 6
    print(lista[num]) #esto porque iteramos asi lista[0], lista[1] ...




print("### FORMA CORRECTA DE RECORRER UN BUCLE CON INDICES ##")
#RECORRER UNA LISTA CON INDICES USANDO ENUMERATE
for num in enumerate(lista):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")





#usando el else
for num in lista:
    print(f"ejecutando el ultimo bucle valor actual: {num}")
else:
    print("la lista se termino de ejecutar")