
#se puede crear una lista con list
lista = list([1,2,3,4,5])

#crear lista con []
lista2 = [456,5,3,88,6]



#devolver los elementos de la lista

print(len(lista2))

#agregando un valor a la lista
lista2.append("nuevo elemento") #lo agrega al final de la lista


#agregando un elemento a la lista en un indice especifico
lista2.insert(2, "estoy en la posicion 8") #esto es como la primitiva de los nodo deja cambia lo apuntado al nuevo nodo y el nuevo apunta al siguiente

#extend agregar varios elementos a la lista
lista2.extend(lista) #pasamos otra lista de muchos elementos y la agrega


#pop eliminar un elemento de la lista
lista2.pop(0) #me borra el elemento dado por la posicion
              #si pones -1 elimina el ultimo y si pones -2 el anteultimo

#remove eliminar un elemento por su valor
lista2.remove(2) #le pasamos el valor del elemento si esta lo elimina

#clear elimina todos los elementos de la lista

#lista.clear()


#sort ordena ascendentemente pero tienen que ser solo numeros no permite cadenas de texto
lista.sort()
lista.sort(reverse=True) #si le pasas el reverse como parametro lo ordena en reversa


#invertir los elementos de una lista solo permite numeros

lista.reverse() #funciona para cualquier lista invertirla no importa si hay texto

#listas con index

lista.index(5) #debe buscar el elemento igual a diferencia de las tuplas que con solo pasarle un valor que exista en el elemento buscado devuelve todo


##################### ANOTACIONES##########################

#en la tupla solo podemos contar elementos y buscar elementos nada mas, ya que las tuplas y los conjuntos son inmutables

#conjuntos se hacen con set para poder ver que funciones podemos usar hay que poner dir(set([15,6,8]))

#####################################################


#recorrer lista
for element in lista :
    print(element)



