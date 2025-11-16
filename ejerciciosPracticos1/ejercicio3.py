# Pedí al usuario que escriba una frase
# Si tiene más de 20 caracteres → “Texto largo”
# Si tiene entre 10 y 20 → “Texto medio”
# Si tiene menos de 10 → “Texto corto”
# Mostrá también cuántas veces aparece la letra "a"

frase = input("escribi una frase: ")


if len(frase) > 20:
    print("texto largo")
elif len(frase) < 20 and len(frase) > 10:
    print("texto medio")
else:
    print("texto corto")

print(f"la letra a se repite:{frase.count("a")} ")