import argparse  # ← Importamos el módulo que nos permite crear un CLI profesional


def main():

    # ================================================================
    # ArgumentParser:
    #
    # Crea el "motor" del CLI, donde configuramos:
    #   - descripción del programa
    #   - ejemplos
    #   - mensajes de ayuda
    #
    # Argumentos principales:
    #   description → texto que aparece al usar --help
    #   epilog      → texto final en la ayuda (opcional)
    #   prog        → nombre del programa (opcional)
    #
    # ================================================================
    parser = argparse.ArgumentParser(
        description="Programa que saluda usando CLI",  # se muestra en --help
        epilog="Ejemplo: python cli.py --nombre Nahuel --edad 21"  # info adicional
    )

    # ================================================================
    # add_argument:
    #
    # Sirve para definir qué argumentos acepta el programa.
    #
    # PARAMETROS MÁS IMPORTANTES:
    #
    # --nombre-del-parametro → nombre del argumento
    #
    # type         → tipo de dato (str, int, float, bool)
    # help         → descripción que se muestra en --help
    # required     → si es obligatorio pasar el argumento
    # default      → valor por defecto si el usuario no pasa nada
    # choices      → lista de valores permitidos
    # action       → para flags booleanas (store_true, store_false)
    #
    # ================================================================

    parser.add_argument(
        "--nombre",        # ← nombre del parámetro que se usará en consola
        type=str,          # ← argparse convertirá el argumento a string
        required=True,     # ← este parámetro es obligatorio
        help="Tu nombre"   # ← aparece cuando el usuario usa --help
    )

    parser.add_argument(
        "--edad",
        type=int,              # ← lo convierte a entero automáticamente
        default=18,            # ← si no lo pasan, usa 18
        help="Tu edad (opcional, por defecto es 18)"
    )

    # ================================================================
    # parser.parse_args():
    #
    # Procesa los argumentos que el usuario pasa por consola.
    #
    # Ejemplo si el usuario escribe:
    # python cli.py --nombre Nahuel --edad 21
    #
    # Entonces:
    # args.nombre → "Nahuel"
    # args.edad   → 21
    #
    # ================================================================
    args = parser.parse_args()

    # ================================================================
    # Uso de los argumentos
    # ================================================================
    print(f"Hola {args.nombre}, tenés {args.edad} años.")


# ================================================================
# Punto de entrada del script.
# Esto permite ejecutar el programa desde la consola:
#   python cli.py --nombre Nahuel --edad 21
# ================================================================
if __name__ == "__main__":
    main()
    
# =====================================================================
# EXPLICACIÓN COMPLETA DE add_argument()  — (ARGPARSE)
#
# La función add_argument() se utiliza para agregar un parámetro o 
# argumento que el usuario podrá pasar desde la consola.
#
# Ejemplo básico de uso:
#   parser.add_argument("--nombre", type=str)
#
# PARAMETROS MÁS IMPORTANTES:
#
# 1) "--nombre"
#    - Nombre del argumento en forma larga.
#    - Se llama así desde consola:
#          python script.py --nombre Nahuel
#
# 2) "-n"
#    - Forma corta del argumento.
#    - Permite:
#          python script.py -n Nahuel
#
# 3) type=str / int / float / bool
#    - Indica a qué tipo debe convertir el argumento.
#    - Si el usuario pone algo incorrecto, argparse muestra error.
#
# 4) required=True
#    - El argumento es obligatorio.
#    - Si no se pasa, argparse muestra un error automáticamente.
#
# 5) default=valor
#    - Valor que toma el argumento cuando el usuario NO lo pasa.
#    - Ejemplo:
#          parser.add_argument("--edad", type=int, default=18)
#
# 6) help="texto"
#    - Describe para qué sirve el argumento.
#    - Se ve cuando el usuario escribe:
#          python script.py --help
#
# 7) choices=[a, b, c]
#    - Restringe los valores aceptados.
#    - Si el usuario pasa otro valor, argparse lanza un error.
#    - Ejemplo:
#          choices=["rapido", "lento"]
#
# 8) action="store_true"
#    - Crea un FLAG booleano.
#    - Si el usuario escribe:
#          python script.py --debug
#      entonces args.debug == True.
#    - Si NO lo escribe:
#      entonces args.debug == False.
#
# 9) nargs="*"
#     - Permite recibir múltiples valores.
#     - Ejemplo:
#          parser.add_argument("--nombres", nargs="*")
#      Usado así:
#          python script.py --nombres Ana Luis Pedro
#      Resultado:
#          args.nombres == ["Ana", "Luis", "Pedro"]
#
# 10) metavar="X"
#     - Cambia el nombre que aparece en la ayuda.
#     - Ejemplo:
#          parser.add_argument("--edad", metavar="AÑOS")
#     - En la ayuda se ve como:
#          --edad AÑOS
#
# =====================================================================