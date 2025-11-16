#ejercicio 11 pedi una palabra y comproba si es un palindromo 


palabra = input("ingresa el texto para saber si es palindromo: ")

cadena_invertida = palabra[::-1]

if (palabra == cadena_invertida):
    print("es igual al derecho y al reves")
    print(f"normal: {palabra}")
    print(f"invertida: {cadena_invertida}")
else:
    print("es distinta")
    print(f"normal: {palabra}")
    print(f"invertida: {cadena_invertida}")