def eliminar(inventario, producto_eliminar):
    
    for i, producto in enumerate(inventario):
        if producto["nombre"] == producto_eliminar.lower():
            inventario.pop(i)
            print("\n####### producto eliminado #######")
            return
    else:
        print("\n######## no se pudo eliminar el producto no existe ########")
