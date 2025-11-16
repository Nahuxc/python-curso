#EJERCICIO NIVEL MEDIO , EJERCICIO 1

lista_notas = [8.5,2,9,6,3,1,1,7]

for i, notas in enumerate(lista_notas, start=1):
    if (notas >= 6):
        print(f"el alumno {i} aprobo")
    else:
        print(f"el alumno {i} no aprobo")

promedio = sum(lista_notas) / len(lista_notas)

print(f"este es el promedio de notas totales: {promedio}")