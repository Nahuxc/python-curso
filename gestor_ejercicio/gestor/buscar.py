def buscar(inventario, busqueda_producto):
    for i, producto in enumerate(inventario):
        if (producto["nombre"] == busqueda_producto.lower()):
            print("\n####### PRODUCTO ENCONTRADO ########")
            print(f""" 
========== PRODUCTO N°{i + 1} =============
nombre: {producto['nombre']}
precio: {producto['precio']}
stock: {producto['stock']}
categoria: {producto['categoria']}
======================================
                  """)
            return
    else:
        print("\n###### no se encontro el producto ######")