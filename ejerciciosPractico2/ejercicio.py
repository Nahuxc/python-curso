""" 
hoy falto el profesor de clases y los chicos
se organizaron para armar la clase propia

- 1 alumno es el profesor
- 1 alumno es el asistente

A) pedir el nombre y la edad de los compañeros que vinieron
a la clase y ordenar los datos de menor a mayor

B) el mayor es el profesor y el menor es el asistente:
quien es quien?

"""

#crear funcion cargar alumnos
def cargarAlumno(compañeros, cantidadAlumnos):
    i = 1
    while(i <= cantidadAlumnos):
        nombre = input("ingresa tu nombre: ")
        edad = input("ingresa tu edad: ")
        alumno_struct = {
            "id": i,
            "nombre": nombre,
            "edad" : edad
        }
        compañeros.append(alumno_struct)
        i += 1




#declaracion de variables
id = 1
lista_de_alumnos = []

#llamado de funcion cargar alumnos
cargarAlumno(lista_de_alumnos, 2)

#ordenar lista
lista_de_alumnos.sort(key=x : x[1] > x[2])


#mostrar alumnos
for alumnos in lista_de_alumnos:
    print(f"===== ALUMNO {alumnos['id']} =====")
    print(f"nombre: {alumnos['nombre']}")
    print(f"edad: {alumnos['edad']}")
    print("=====================")




