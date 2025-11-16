### set o conjuntos 

conjunto = set([1,3,4,8,9,6])

print(conjunto)

#metiendo un conjunto dentro de otro conjunto

conjunto1 = frozenset({"dato",324,3}) #fronzenset sirve para meter dentro de otro conjunto0
conjunto2 = {conjunto1, 232, 42}


print(conjunto2)


#teoria de conjuntos

#si es subconjuto
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5}

resultado = conjunto2.issubset(conjunto1) #indica que si conjunto 2 es un subconjunto de conjunto 2
resultado = conjunto2 <= (conjunto1) #indica lo mismo que el anterior pero con operadores

#si es super conjunto

resultado = conjunto1.issuperset(conjunto2) #indica que si conjunto1 es super conjunto de conjunto 2
resultado = conjunto1 >= (conjunto2) #indica lo mismo que el anterior pero con operadores


#verificar si hay un algun numero en comun

resultado = conjunto2.isdisjoint(conjunto1)




