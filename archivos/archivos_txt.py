########## ARCHIVOS ##########
#alt + 92 = \\

#usando open para abrir un archivo con una codificacion universal
archivo = open("archivos\\text.txt", encoding="UTF-8")

#LEER UN ARCHIVO CON read()
print(archivo.read())

#una vez leido el archivo luego hay que cerrarlo
archivo.close()




archivo = open("archivos\\text.txt", encoding="UTF-8")

#como leer una linea especifica (usarla con archivos chicos de texto)
linea_1 = archivo.readline() #por dentro le pasamos 1, 2 o .. n para ver las distintas lineas, sino lee la linea lee la cantidad de caracteres  ej:  readline(2) o readline(1)
print(linea_1)

archivo.close()

