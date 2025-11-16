#OPERADORES ARITMETICOS

#funcion type que es para saber el tipo de dato

nombre = "texto"

#string
print(type(nombre))

#int
print(type(23))

#float
print(type(52.2))

#lista
print(type(["kiwi", 23]))

#tuple
print(type(("mundo", 54, 2)))

#bool
print(type(True))

#conjunto / set
print(type({2,5,43,"hika"}))

#diccionario
print(type( {'nombre': "marcos"} ))

""" 
+ suma
- resta
* multiplica
/ divide
% devuelve el resto de una division
** realiza una exponencial
// devuelve el entero de una division

"""
#suma
a = 3
b = 3
resultado = a + b

print(resultado)

#resta
a = 3
b = 3
resultado = a - b

print(resultado)

#multiplicacion
a = 3
b = 3
resultado = a * b

print(resultado)

#division devuelve dato float
a = 3
b = 3
resultado = a / b

print(resultado)

#resto de una division
a = 3
b = 3
resultado = a % b

print(resultado)

#exponente o potenciacion
a = 3
b = 3
resultado = a ** b

print(resultado)

#division baja
a = 3
b = 3
resultado = a // b

print(resultado)



""" 

operadores

== es igual que     5 == 5  true
!= distinto de      5 != 6  true
< menor que         5 < 20  true
> mayor que         5 > 3   true

<= menor o igual    5 <= 20 true
>= mayor o igual    5 >= 3 true

not  negar   en otros lenguajes se usa el !


"""

x = 0

resultado = not x # x != 0 false si x == 0 true

print(resultado)
