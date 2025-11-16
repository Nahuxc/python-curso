#nivel dificil ejercicio

#Mini inventario: manejá un diccionario de productos con nombre, precio y stock; permití modificar stock.

#Buscador de palabras: pedí una palabra y verificá si existe dentro de un texto dado.

#Diccionario de estudiantes: pedí nombre, edad y nota; guardá varios y mostrálos en tabla.

#Simulador de carrito: permití agregar productos a un carrito y mostrale el total a pagar.

#Promedio general: cargá notas de alumnos en un diccionario y calculá el promedio general.

#Analizador de lista: creá una función que reciba una lista y devuelva suma, promedio, máximo y mínimo.

#Conversor de moneda: función que convierta un monto entre pesos, dólares y euros con tasas fijas.

#Frecuencia de letras: pedí un texto y mostrá las tres letras más frecuentes.


#Simulador de agenda diaria: permití agregar eventos con fecha y hora, y listálos ordenados por fecha.


#Gestor de contactos: permití agregar, buscar y eliminar contactos guardados en un diccionario.

#funciones
def agregarContacto(lista, nombre, apellido, numero):
    contacto = {
        "nombre": nombre.lower(),
        "apellido": apellido.lower(),
        "numero": numero
    }
    lista.append(contacto)
    print("se agrego existosamente el contacto")


def mostrarLista(lista):
    if not lista:
        print("📭 No hay contactos guardados.")
        return

    print("\n📒 Lista de contactos:")
    print("---------------------------")
    for i, contacto in enumerate(lista, start=1):
        print(f"{i}. {contacto['nombre']} {contacto['apellido']} | 📞 {contacto['numero']}")
    print("---------------------------")


def buscarContacto(lista, contacto_buscado):
    for contacto in lista:
        if(contacto["nombre"] == contacto_buscado):
            print(f"se encontro el contacto {contacto_buscado}")
            return
    else:
        print(f"no se encontro el contacto {contacto_buscado}")


def eliminarContacto(lista, contacto_eliminar):
    for i, contacto in enumerate(lista, start=0):
        if contacto["nombre"] == contacto_eliminar:
            lista.pop(i)
            return
    else:
        print("no se encontro el contacto a eliminar")


#variables
lista_de_contactos = []

#invocaciones
agregarContacto(lista_de_contactos, "jorge", "martinez", 11522689)
agregarContacto(lista_de_contactos, "nati", "mar", 11522689)

buscarContacto(lista_de_contactos, "jorge")

eliminarContacto(lista_de_contactos, "jorge")

mostrarLista(lista_de_contactos)