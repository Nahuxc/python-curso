#ejercicio 8 Creá una lista con los números del 1 al 10 y mostrá el cuadrado de cada número.

#opcion 1
i = 1

while(i <= 10):
    print(i ** 2)
    
    i += 1
    
#opcion 2

lista = [1,2,3,4,5,6,7,8,9,10]

for num in lista:
    print(num ** 2)
    

#opcion 3
for num in range(1, 11):
    print(num ** 2)
    
#opcion 4
cuadrados = [num ** 2 for num in range(1, 11)]
print(cuadrados)