#ejercicio 7 Pedí un texto y devolvelo invertido (usando slicing o reversed).

#forma de invertir por palabra
texto = "hola como estas"

cadena = texto.split(" ")
cadena.reverse()

texto_invertido = " ".join(cadena)

print(texto_invertido)


#forma de invertir letra por letra usando slicing 

invertido = texto[::-1]
print(f"texto invertido: {invertido}")


#forma de invertir

invertido = "".join(reversed(texto))
print(f"Texto invertido: {invertido}")