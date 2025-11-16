#el modo de apertura w lo que hace es escribir en el archivo pero crea uno nuevo todo el tiempo y lo sobreescribe en el ya creado
with open("archivos\\text_escritura.txt", "w", encoding="UTF-8") as archivo:
    
    #archivo.write("esto le quiero escribir y se va a sobreescribir")
    
    #\n deja un espacio
    
    archivo.writelines(["linea1 a escribir\n", "linea2 a escribir\n"])
    
    archivo.writelines(["linea3 a escribir\n", "linea4 a escribir"])
    
    #si ponemos 2 write se escriben en el mismo y no se sobreescribe