def agregar(inventario, nombre, precio, stock, categoria):
    try:
        producto = {
            "nombre": nombre.lower(),
            "precio": precio,
            "stock": stock,
            "categoria": categoria.lower()
        }
        inventario.append(producto)
        print("\n########## se agrego exitosamente #########")
    except ValueError:
        print("\n########## hubo un error al agregar el producto #############")