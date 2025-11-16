#encontrando el numero mayor de una lista con -  max()
numeros = [4,5,68,2,1,3]
numero_mas_alto = max(numeros)
print(f"el maximo es: {numero_mas_alto}")


#encontrando el numero menor de una lista con - min()
numero_menor = min(numeros)
print(f"el minimo es: {numero_menor}")

#redondeando a 6 decimales
numero = round(12.156165, 2)
print(f"cantidad de decimales: {2} resultado del round: {numero}")


#retorna false -> 0 vacio, false, ninguno / true numero distinto de 0 o una cadena, datos no vacios - funcion bool()

resultado = bool(0) # ([]) false, (none) false,etc
print(resultado)


#retorna true si todos los valores son verdaderos   all()
resultado = all([1235, "true", [5321,62,2]]) # si le pasamos un 0 o un none es falso siempre, sino es verdadero
print(resultado)


#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)


#sacar el valor absoluto o modulo de un numero abs()
modulo = abs(-1)
print(modulo)

#otras funciones que podemos usar

# ==========================================================
# 🧩 FUNCIONES INTEGRADAS (BUILT-IN) MÁS USADAS EN PYTHON
# ==========================================================

# ----------------------------------------------------------
# 1️⃣ FUNCIONES BÁSICAS DE ENTRADA Y SALIDA
# ----------------------------------------------------------
# print()         → Muestra texto o variables en pantalla
# input()         → Pide un dato al usuario
# len()           → Devuelve la longitud de una secuencia (lista, string, etc.)
# type()          → Muestra el tipo de dato
# id()            → Devuelve el identificador único de un objeto

# ----------------------------------------------------------
# 2️⃣ FUNCIONES NUMÉRICAS
# ----------------------------------------------------------
# abs(x)          → Devuelve el valor absoluto
# round(x, n)     → Redondea un número a n decimales
# pow(x, y)       → Eleva x a la potencia y (igual que x**y)
# sum(iterable)   → Suma todos los elementos de una lista o tupla
# max(iterable)   → Devuelve el valor máximo
# min(iterable)   → Devuelve el valor mínimo

# ----------------------------------------------------------
# 3️⃣ FUNCIONES DE CONVERSIÓN DE TIPO
# ----------------------------------------------------------
# int(x)          → Convierte a número entero
# float(x)        → Convierte a número decimal
# str(x)          → Convierte a cadena de texto
# bool(x)         → Convierte a booleano (True o False)
# list(x)         → Convierte a lista
# tuple(x)        → Convierte a tupla
# set(x)          → Convierte a conjunto (sin elementos repetidos)
# dict(x)         → Convierte a diccionario (si es posible)

# ----------------------------------------------------------
# 4️⃣ FUNCIONES PARA SECUENCIAS Y COLECCIONES
# ----------------------------------------------------------
# sorted(iterable)        → Devuelve una lista ordenada
# reversed(iterable)      → Devuelve un iterador con los elementos en orden inverso
# enumerate(iterable)     → Devuelve índices y valores al iterar
# zip(a, b)               → Combina dos listas en pares (tuplas)
# all(iterable)           → Devuelve True si todos los elementos son verdaderos
# any(iterable)           → Devuelve True si alguno es verdadero
# range(inicio, fin, paso)→ Genera una secuencia de números (usado en bucles)

# ----------------------------------------------------------
# 5️⃣ FUNCIONES DE MANEJO GENERAL
# ----------------------------------------------------------
# help(obj)         → Muestra documentación de una función u objeto
# dir(obj)          → Lista los métodos y atributos de un objeto
# isinstance(x, t)  → Comprueba si un objeto es de un tipo específico
# hasattr(obj, a)   → Verifica si un objeto tiene un atributo
# getattr(obj, a, d)→ Obtiene un atributo (si no existe devuelve el valor por defecto d)
# setattr(obj, a, v)→ Asigna un valor a un atributo
# delattr(obj, a)   → Elimina un atributo de un objeto

# ----------------------------------------------------------
# 6️⃣ FUNCIONES RELACIONADAS CON ARCHIVOS
# ----------------------------------------------------------
# open(nombre, modo) → Abre un archivo (modo: "r", "w", "a")
# read()             → Lee el contenido completo del archivo
# write()            → Escribe texto en el archivo
# close()            → Cierra el archivo (si no se usa with)

# Ejemplo:
# with open("datos.txt", "w") as f:
#     f.write("Hola Mundo")

# ----------------------------------------------------------
# 7️⃣ FUNCIONES PARA DEPURACIÓN O DESARROLLO
# ----------------------------------------------------------
# vars(obj)          → Devuelve un diccionario con los atributos del objeto
# globals()          → Devuelve las variables globales
# locals()           → Devuelve las variables locales
# callable(obj)      → Indica si algo se puede llamar como función
# eval(expr)         → Ejecuta una expresión en forma de texto (⚠️ usar con cuidado)

# ----------------------------------------------------------
# 8️⃣ FUNCIONES ESPECIALES (AVANZADAS PERO ÚTILES)
# ----------------------------------------------------------
# map(func, iterable)    → Aplica una función a cada elemento
# filter(func, iterable) → Filtra elementos según una condición
# reduce(func, iterable) → Combina elementos acumulativamente (de functools)
# lambda                 → Crea funciones anónimas rápidas (no es función pero muy usada)

# Ejemplo rápido:
# from functools import reduce
# nums = [1, 2, 3, 4]
# dobles = list(map(lambda x: x * 2, nums))  # [2, 4, 6, 8]
# pares = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
# total = reduce(lambda a, b: a + b, nums)  # 10

# ----------------------------------------------------------
# ✅ RESUMEN DE LAS MÁS IMPORTANTES PARA MEMORIZAR
# ----------------------------------------------------------
# print, input, len, type, range, sorted,
# int, float, str, bool,
# sum, max, min, abs, round,
# enumerate, zip, any, all,
# open, dir, isinstance, help
# ==========================================================
