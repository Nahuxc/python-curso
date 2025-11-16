def mostrar(inventario):
    if len(inventario) == 0:
        print("no hay productos en el inventario")
    else:
        for i, producto in enumerate(inventario, start=1):
            print("\n############ LISTA DE INVENTARIO ###############")
            print(f""" 
========== PRODUCTO N°{i} =============
nombre: {producto['nombre']}
precio: {producto['precio']}
stock: {producto['stock']}
categoria: {producto['categoria']}
======================================
                """)