#Dada una lista de números, devolvé una nueva lista con solo los impares.
lista_numeros = [1,2,3,4,5,6,7,8,9]
nueva_lista = []

for numeros in lista_numeros:
    if (numeros %2 == 1):
        nueva_lista.append(numeros)

for num in nueva_lista:
    print(num)
    

#otra posible solucion

lista_numeros = [1,2,3,4,5,6,7,8,9]
nueva_lista = [n for n in lista_numeros if n % 2 == 1]
print(nueva_lista)