#el modo a es el de editar o sea no sobre escribe y crea denuevo
#sino que lee el archivo y te permite agregarle cosas

#solo para los txt se usa r, w, a

with open("archivos\\text_escritura.txt", "a", encoding="UTF-8") as archivo:
    
        lineas = [f"\nesta linea viene de un for pythonico {i}" for i in range(1,11)]
        archivo.writelines(lineas)