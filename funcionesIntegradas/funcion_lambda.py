#es similar a la funcion flecha en js

#crea funciones anonimas que despues podemos almacenar en variables

#funcion lamnda para multiplicar: beneficios: podemos usarlo para casos sencillos y rapidos, no hace falta hacer retornos

#cuando hay que dar mas de una expresion es mejor def funcion

multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(5))

numeros = [1,2,3,4,56,8,9]

#def es_par(num):
#    if (num %2 == 0):
#        return True



#usando filter que es una funcion comun que devuelve true o false
#esto es pudiendo usar lambda dentro de filter
numeros_pares = filter(lambda num: num%2 == 0, numeros)

print(list(numeros_pares))