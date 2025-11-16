#ejercicio 2 Pedí un número y mostrale su tabla de multiplicar del 1 al 10.

#pedir valor a multiplicar
valor = int(input("ingresa tu valor para devolver su tabla: "))

for i in range(1,11):
    print(f" {valor} x {i}: {i*valor}")