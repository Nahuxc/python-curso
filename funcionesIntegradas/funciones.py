#estructura para crear una funcion es como una void

def nombre_funcion(parametro):
    print(parametro)
    
#nombre_funcion("hola")


#crear una funcion que nos retorne valores esta es como una de retorno

def calculo(x, y):
    resultado = x + y
    return resultado


def crear_contraseña_random(num):
    chars = "abcdefghi"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña #retornamos un valor mediante la funcion

#print(crear_contraseña_random(73))
#print(calculo(1,3))


#retorno de multiples valores
def calculo5(x, y):
    resultado_suma = x + y
    resultado_multiplicacion = x * y
    return resultado_suma, resultado_multiplicacion

#para acceder hacemos lo siguiente, lo transforma a una tupla

#print(calculo5(2,4)) #aca lo vemos

resultado_sum = calculo5(2,4)[0] #accedemos por el indice
print(resultado_sum)
resultado_mul = calculo5(2,4)[1] #accedemos por el indice
print(resultado_mul)


#otra forma y la que se usa es (ES FORMA OPTIMA)

resultado_sum, resultado_mul = calculo5(2,5) #evitamos acceder por indice ya que desglosamos la tupla

#print(resultado_sum)
#print(resultado_mul)


#formas de pasarle datos y hacerlo en lista

def suma_lista(*numeros):  #lo transforma a lista *
    return sum(numeros)


suma_lista(1,24,56,7,4) #de esta forma devuelve la suma de todos esos numeros transformandolos dentro de la funcion como lista

#acceder a valores de una lista por parametros  forma optima de sumar valores

def lista(numeros):
    print(*numeros) #devuelve sus valores * 
    print([*numeros])
    print(f"suma de la lista: {sum([*numeros])}") #debemos transformarlo a lista denuevo para su uso

lista([1,8,9,5,63,2]) #toma una lista