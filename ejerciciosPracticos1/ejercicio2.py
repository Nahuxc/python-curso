# Pedí un número decimal (float)
# Mostrá su valor entero (//), su cuadrado (**2)
# y si es mayor o menor que 100.

numero = float(input("ingresa un numero decimal: "))

valor_entero = int(numero) # numero // 1

valor_exponencial = numero ** 2

print(valor_entero)
print(valor_exponencial)


if numero > 100:
    print("el numero es mayor a 100")
elif numero < 100:
    print("el numero es menor que 100")
else:
    print("el numero es igual a 100")