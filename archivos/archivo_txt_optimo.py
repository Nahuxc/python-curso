#para no abrir y cerrar el archivo tantas veces, vamos a enteder como abrirlo y cerrarlo optimamente

#podemos usar modos de apertura de archivo r o w

with open("archivos\\text.txt","r", encoding="UTF-8") as archivo: #aca adelante le ponemos el nombre como habiamos hecho antes
    #leemos el archivo
    contenido = archivo.read()
    
    #no hace falta cerrar el archivo
    print(contenido)