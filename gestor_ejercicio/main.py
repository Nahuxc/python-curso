from gestor import agregar, buscar, eliminar, mostrar, guardar_archivo

#SOLO DECLARAR ACA USO DE VARIABLES GLOBALES

def menu():
    print("""
================== MENU PRINCIPAL ===================
1) agregar item al inventario
2) mostrar items del inventario
3) buscar items del inventario
4) eliminar items del inventario
5) guardar Archivo de inventario
0) Salir
          """)


def main():
    #inicializacion de mi opcion en -1
    opcion = -1

    #lista del inventario vacia
    inventario = []

    while opcion != 0:
        #carga del menu
        menu()
        #tocar opcion
        opcion = input("opcion a seleccionar: ")
        #verificando que el valor que ingresa sea el correcto
        try:
            opcion = int(opcion)
        except ValueError as e:
            print(f"ERROR: {e}")
            print("\nPor favor ingrese un número válido para el menú.")
            continue

        #match de opcciones para manejar el menu
        match opcion:
            case 1:
                    while True:
                        print(f"\n========== PRODUCTO =========")
                        nombre = input("ingresa el nombre del producto: ")
                        precio = input("ingresa el precio: ")
                        stock = input("ingrese la cantidad de stock: ")
                        categoria = input("ingrese la categoria: ")
                        try:
                            agregar(inventario, nombre, int(precio), int(stock), categoria)
                        except ValueError as e:
                            print(f"ERROR: {e}")
                            print("\n###### no ingresaste bien los valores ######")
                        else:
                            break


            case 2:
                mostrar(inventario)
            case 3:
                busqueda = input("ingresa el nombre del producto a consultar: ")
                buscar(inventario, busqueda)
            case 4:
                producto_eliminar = input("ingresa el nombre del producto a eliminar: ")
                eliminar(inventario, producto_eliminar)
            case 5:
                guardar_archivo()
            case 0:
                print("\n###### SALIENDO DEL PROGRAMA #######")
                break
            case _:  # Caso por defecto si la opción no existe
                print("\n ###### Opción no válida, intente nuevamente. #####")



if (__name__ == "__main__"):
    main()