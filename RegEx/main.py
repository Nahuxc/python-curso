#EXPRESIONES REGULARES   RegEX

#01- expresiones regulares

#se utilizan para buscar y manipular cadenas de texto con una forma especifica

""" las expresiones regulares son una secuencia de caracteres que forman un patron
de busqueda. se utilizan para la busqueda de cadenas de texto, validaciones de datos etc"""

""" ¿porque aprender regex? 

- busqueda avanzada: encontrar patrones especificos en textos grandes de forma rapida y precisa

- validacion de datos: asegurarte que los datos que ingresa un usuario como el mail, telefono, etc. son correctos

- manipulacion del texto: extraer, reemplazar y modficiar de la cadena de texto facilmente


"""

#1. para trabajar regex
import re



#2. crear un patron, que es una cadena de texto que describe lo que queremos buscar

def main():
    
    #2 crear un patron, que es una cadena de texto que decribe lo que queremos buscar
    patron_a_buscar = "hola"
    #3 el texto donde vamos a buscar
    text = "hola mundo"
    # usar la funcion de busqueda de re
    resultado_busqueda = re.search(patron_a_buscar, text)

    print(resultado_busqueda)


if __name__ == "__main__":
    main()