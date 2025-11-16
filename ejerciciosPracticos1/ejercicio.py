# Pedí dos números y decí cuál es mayor o si son iguales
# Además, mostrales la diferencia absoluta entre ambos.

num1_consulta = input("ingresa el primer numero ")
num2_consulta = input("ingresa el segundo numero ")

num1 = int(num1_consulta)
num2 = int(num2_consulta)
dif = abs(num1 - num2)

if num1 > num2:
    print(f"numero 1: {num1} es mayor a {num2}")
elif num1 < num2:
    print(f"numero 2: {num2} es mayor a {num1}")
else:
    print("son iguales")

print(f"la diferencia es de: {dif}")