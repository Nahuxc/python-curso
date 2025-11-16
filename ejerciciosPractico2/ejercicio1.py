#ejercicio 1 

division = lambda a,b : a/b
multiplicacion = lambda a,b : a*b
resta = lambda a,b : a-b
suma = lambda a,b: a+b

valor1 = int(input("ingresa el primer valor a operar: "))
valor2 = int(input("ingresa el segundo valor a operar: "))


print(f"suma: {suma(valor1, valor2)}")
print(f"resta: {resta(valor1, valor2)}")
print(f"multiplicacion: {multiplicacion(valor1, valor2)}")
print(f"division: {division(valor1, valor2)}")

