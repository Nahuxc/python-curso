"""
=======================================
📘 GUÍA COMPLETA: ACCESO A DATOS EN LISTAS, DICCIONARIOS Y TUPLAS
=======================================

Autor: Nahuel Coronel
Descripción:
Archivo guía con todas las formas de acceder e iterar estructuras
complejas en Python (listas, diccionarios, tuplas, listas anidadas, etc.)
Cada bloque está explicado con ejemplos y buenas prácticas.
"""

# ---------------------------------------------------------------------
# 🧩 1️⃣ LISTA DE DICCIONARIOS
# ---------------------------------------------------------------------
contactos = [
    {"nombre": "Jorge", "apellido": "Martinez", "numero": 11522689},
    {"nombre": "Nati", "apellido": "Mar", "numero": 11852347}
]

# ✅ Forma 1: recorrer con for y acceder por clave
for contacto in contactos:
    print(contacto["nombre"], contacto["numero"])

# ✅ Forma 2: usar enumerate() para índice + valor
for i, contacto in enumerate(contactos):
    print(f"{i+1}. {contacto['nombre']} {contacto['apellido']}")

# ⚙️ Forma 3: acceso por índice de lista y luego por clave
print(contactos[0]["nombre"])  # 'Jorge'

# ⚙️ Forma 4: usar .get() para evitar errores si falta la clave
print(contactos[1].get("apellido", "No especificado"))


# ---------------------------------------------------------------------
# 🧱 2️⃣ LISTA DE TUPLAS
# ---------------------------------------------------------------------
usuarios = [
    ("jorge", "martinez", 11522689),
    ("nati", "mar", 11852347)
]

# ✅ Forma 1: desempaquetar en el for
for nombre, apellido, numero in usuarios:
    print(nombre, numero)

# ⚙️ Forma 2: acceder por índices
print(usuarios[0][1])  # 'martinez'

# ✅ Forma 3: usar enumerate() con tuplas
for i, (nombre, apellido, numero) in enumerate(usuarios, start=1):
    print(f"{i}. {nombre} ({numero})")


# ---------------------------------------------------------------------
# 📦 3️⃣ LISTA DE LISTAS
# ---------------------------------------------------------------------
datos = [
    ["jorge", "martinez", 11522689],
    ["nati", "mar", 11852347]
]

# ✅ Forma 1: desempaquetar
for nombre, apellido, numero in datos:
    print(nombre, numero)

# ⚙️ Forma 2: acceso por índices
print(datos[1][0])  # 'nati'


# ---------------------------------------------------------------------
# 🧠 4️⃣ COMBINACIONES (listas con tuplas/diccionarios anidados)
# ---------------------------------------------------------------------
usuarios_complejos = [
    {
        "nombre": "jorge",
        "telefonos": (11522689, 11555555),
        "direcciones": ["Av. Siempre Viva 123", "Calle 9 #456"]
    },
    {
        "nombre": "nati",
        "telefonos": (11852347,),
        "direcciones": ["Calle Azul 77"]
    }
]

# ✅ Acceso a valores anidados
for u in usuarios_complejos:
    print(u["nombre"])
    print("Teléfono principal:", u["telefonos"][0])
    print("Dirección principal:", u["direcciones"][0])
    print("----------------------")

# ✅ Acceso directo puntual
print(usuarios_complejos[1]["direcciones"][0])  # 'Calle Azul 77'


# ---------------------------------------------------------------------
# 🚀 5️⃣ BÚSQUEDAS Y FILTROS EN LISTAS COMPLEJAS
# ---------------------------------------------------------------------
# ✅ Forma 1 (óptima y pythonica): next() + generador
resultado = next((c for c in contactos if c["nombre"] == "Nati"), None)
print(resultado)

# ✅ Forma 2: list comprehension
coincidencias = [c for c in contactos if c["apellido"] == "Martinez"]
print(coincidencias)

# ⚙️ Forma 3: bucle clásico con break
for c in contactos:
    if c["nombre"] == "Jorge":
        print("Encontrado:", c)
        break


# ---------------------------------------------------------------------
# 🧮 6️⃣ USO DE enumerate() EN DIFERENTES ESTRUCTURAS
# ---------------------------------------------------------------------
colores = ["rojo", "verde", "azul"]

# 📘 Con lista simple
for i, color in enumerate(colores, start=1):
    print(f"{i}: {color}")

# 📙 Con lista de tuplas
for i, (nombre, apellido, numero) in enumerate(usuarios, start=1):
    print(f"{i}. {nombre} ({numero})")

# 📒 Con lista de diccionarios
for i, c in enumerate(contactos, start=1):
    print(f"{i}. {c['nombre']} - {c['numero']}")


# ---------------------------------------------------------------------
# 🧭 7️⃣ DICCIONARIOS: FORMAS DE ACCEDER Y RECORRER
# ---------------------------------------------------------------------
datos = {
    "nombre": "Jorge",
    "edad": 25,
    "ciudad": "Buenos Aires"
}

# ✅ Forma 1: acceder directamente por clave
print(datos["nombre"])

# ⚙️ Forma 2: usar .get() → evita error si la clave no existe
print(datos.get("profesion", "Desconocido"))

# ✅ Forma 3: recorrer solo las claves (por defecto)
for key in datos:
    print(f"clave: {key}")

# ✅ Forma 4: recorrer claves con .keys()
for key in datos.keys():
    print(f"clave (usando keys): {key}")

# ✅ Forma 5: recorrer solo los valores con .values()
for value in datos.values():
    print(f"valor: {value}")

# ✅ Forma 6 (💎 la más útil): recorrer con .items() → devuelve (clave, valor)
for key, value in datos.items():
    print(f"Esta es la key: {key}  y este es su valor: {value}")

# ⚙️ Forma 7 (como la que mencionaste): desempaquetando manualmente el par
for par in datos.items():
    key = par[0]
    value = par[1]
    print(f"Manual → key: {key}, value: {value}")

"""
🔍 MÉTODOS DISPONIBLES EN DICCIONARIOS
--------------------------------------
.keys()      → devuelve todas las claves
.values()    → devuelve todos los valores
.items()     → devuelve tuplas (clave, valor)
.get(key)    → devuelve valor sin error si no existe la clave
.pop(key)    → elimina un par clave-valor específico
.popitem()   → elimina y devuelve el último par agregado
.update({...}) → actualiza o agrega claves nuevas
.clear()     → borra todo el diccionario
.copy()      → copia el diccionario
"""

# ---------------------------------------------------------------------
# 📊 8️⃣ RESUMEN DE EFICIENCIA
# ---------------------------------------------------------------------
"""
🔹 MÁS ÓPTIMAS (claras y rápidas):
    ✅ for + acceso directo (dic["clave"])
    ✅ for + enumerate() en listas
    ✅ for key, value in dic.items()
    ✅ next() o list comprehension para búsquedas

🔸 INTERMEDIAS:
    ⚙️ acceso por índices múltiples [0][1]
    ⚙️ uso de .get() para evitar errores
    ⚙️ bucles for con break

🔻 MENOS ÓPTIMAS:
    ❌ while con contadores manuales
    ❌ recorrer listas completas cuando se busca un solo dato
    ❌ estructuras mal anidadas o sin etiquetas (pérdida de legibilidad)
"""

# ---------------------------------------------------------------------
# 🧾 FIN DEL ARCHIVO
# ---------------------------------------------------------------------
