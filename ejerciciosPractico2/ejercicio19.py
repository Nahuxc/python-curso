#ejercicio 9 nivel medio Pedí una palabra y creá un diccionario que cuente cada letra.

palabra = input("Ingresá una palabra: ").lower()

dic_letras = {}

for letra in palabra:
    if letra in dic_letras:
        dic_letras[letra] += 1
    else:
        dic_letras[letra] = 1

print(dic_letras)