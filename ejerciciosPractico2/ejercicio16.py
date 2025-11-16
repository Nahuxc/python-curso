#ejercicio 2 nivel medio Creá una lista con nombres y eliminá uno que el usuario ingrese.

nombre_borrar = input("ingresa el nombre a borrar: ").lower()

lista_nombres = ["jorge","maria","martin","natalia"]

for i, nombre in enumerate(lista_nombres, start= 0):
    if(nombre_borrar == nombre):
        lista_nombres.pop(i)
        print(f"se borro en la posicion: {i} | el nombre: {nombre_borrar}")
        break
else:
    print("el nombre a querer borrar no existe")


print("====== LISTA =====")
for nombre in lista_nombres:
    print(nombre)
