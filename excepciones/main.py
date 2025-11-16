############# excepciones ##############

#que es un evento? es cualquier cosa que suceda en nuestro programa acciones que se vayan producciendo

def Suma():
    # el try y except : Intentá ejecutar este código, pero si ocurre un error, no te detengas: manejalo acá.

    #Si el usuario escribe algo que no es número, el programa no se rompe, sino que entra al except
    while True:
        a = input("ingresa a: ")
        b = input("ingresa b: ")
        try:#nos ayuda al manejo de errores/excepciones
            resultado = int(a) + int(b)
        except: #si try manda un error entonces entra al except
            print("te pedi un numero")
        else:
            break
    return resultado

Suma()