lista = ["manzana", "banana", "granada", "pera"]

#condicional con un for

for fruta in lista:
    if fruta == "granada":
        continue #esto es para hacer un skip en este caso deja de aparecer granada
    print(fruta)


#evitar que el bucle siga ejecutandose  / tampoco se ejecuta un else en caso que haya
for fruta in lista:
    if fruta == "pera":
        break #termina el bucle hasta donde le decimos break y deja de iterar y no continua con lo que falte a diferencia del continue que si lo hace
    print(fruta)


cadena = "hola nahue"

#las cadenas recorremos caracter por caracter
for letra in cadena:
    print(letra)
    

#bucles for en una linea de codigo

numeros = [20,5,9,8,62]

numeros_duplicados = [x*2 for x in numeros] #expresion matematica adelante y luego el for

#solo para cosas sencillas seria util

print(numeros_duplicados)