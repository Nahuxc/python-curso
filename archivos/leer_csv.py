#importamos csv para poder leer el archivo
import csv

#en un csv se separa con comas y espacios en linea

#lo interpreta como si fuera un excel nombre de columna y datos debajo

with open("archivos\\datos.csv") as archivo:
        reader = csv.reader(archivo)
        
        #leer con pandas es mucho mas recomendado
        for row in reader:
            print(row)