########## DECORADORES ###############

#es una funcion que decora a otra
#agrega un codigo extra a la funcion que ya existia

#uso del decorador
def decorador(funcion): #pasamos una funcion por parametro

    def funcion_modificada():

        # función interna que envuelve a la original
        print("antes de llamar a la funcion")
        funcion()
        print("despues de llamar a la funcion")


    # ❌ ERROR ANTES: return funcion_modificada()
    # ✔️ SOLUCIÓN: devolvemos la función SIN ejecutar
    return funcion_modificada

###### FORMA NO OPTIMA #####

#def saludo():
#    print("hola como estas")

##################################

###### FORMA OPTIMA DE USAR DECORADOR CREAR LA FUNCION Y LLAMARLA ARRIBA DE LA QUE QUEREMOS DECORAR CON UN @

@decorador ## pone el codigo del decorador de funcion que hicimos y es como que automaticamente ya se lo pasa por el parametro y se ejecuta todo normal y nos ahorramos eso de la asignacion de variable y demas
def saludo():
    print("hola como estas")

def main():

    #FORMA NO OPTIMA
    # usamos el decorador dentro le pasamos nuestra funcion
    # saludo_modificado_por_decorador = decorador(saludo)

    # aca llamamos a la variable como viene y se ejecuta
    # saludo_modificado_por_decorador

    # FORMA OPTIMA
    saludo()


if __name__ == "__main__":
    main()