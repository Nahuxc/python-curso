
#algunos de los metodos que aprendimos

# print("hola") # nos muestra en pantalla lo que le pongamos de parametro

# type(24) #nos dice el tipo

cadena = "hola"

#dir es una funcion de python
#print(dir(cadena)) #devuelve la lista de atributos validos del objeto pasado


#METODOS DE CADENA


cadena1 = "esta es la primer cadena"

cadena2 = "esta el asegunda cadena"

#para ejecutar los metodos se pone de la siguiente forma

#metodo es dato.metodo(parametro)

cadena1.upper() #ponemos el texto en mayuscula

cadena1.lower() #ponemos el texto a minuscula

cadena1.capitalize() #primera letra en mayuscula





busqueda_find = cadena1.find("estas") #metodo encuentra la primera aparicion del valor especificado devuelve 0 sino devuelve -1

print(busqueda_find) #es sensible a letras minusculas o mayusculas

#buscamos una cadena en otra cadena

busqueda_cadenas = cadena1.index("a") #la diferencia es que sino encuentra nada tira error una excepcion (hay que aprender a manejar excepciones)

print(busqueda_cadenas)




#replace reemplaza un valor por otro
cadena_nueva = cadena.replace("hola", "hola texto")
cadena_nueva = cadena.replace(",", " ") #reemplazamos las comas por espacios

#split separa por el parametro dado

texto = "hola como estas"

cadena_separada = texto.split(" ") #devuelve una lista

print(cadena_separada) #output: ["hola", "como", "estas"]
print(cadena_separada[0]) #output: ["hola"]








#isnumeric   si es numerico devuelve true

es_numerico = cadena1.isnumeric()

#isalpha si es alfa numerico devuelve true

es_alpha = cadena1.isalpha() #solo toma palabras completas sin espacios o caracters especiales



#count devuelve el numero de ocurrencias de una subcadena en la cadena dada

contar_coincidencias = cadena1.count("a")

#len cuenta los caracteres de una cadena

contar_caracteres = len(cadena1) #no es un metodo es una funcion




#startswith verifica si una cadena termina con

empieza_con = cadena1.startswith("h") #si el teexto arranca con lo indicado da true sino false

#endswith verifica si una cadena comienza con

termina_con = cadena1.endswith("e")











#metodo es una funcion especifica de un objeto o sea tiene funciones propias