# Diccionario con productos:
# stock = {"pan": 10, "leche": 5, "huevos": 0, "queso": 2}
# Pedí al usuario un producto
# - Si no existe → decí “No se vende ese producto”
# - Si existe y hay stock > 0 → “Disponible”
# - Si existe pero stock == 0 → “Sin stock”

dic_stock = {
    "pan" : 10,
    "leche" : 5,
    "huevos" : 0,
    "queso" : 2

}

producto = input("ingresa un producto: ").lower()

if dic_stock.get(producto) != None and dic_stock.get(producto) > 0:
    print("disponible")
elif dic_stock.get(producto) != None and dic_stock.get(producto) == 0:
    print("no hay stock")
else:
    print("no existe")
