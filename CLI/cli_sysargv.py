## Leé los parámetros exactos pasados en la consola.

# posicionarse en la carpeta cd "C:\Users\Nahuel\Desktop\CODE 2025\python-curso\CLI"

# ejecutar: python cli_sysargv.py  estos son los parametros que le paso por consola Nahuel 21

# cli_sysargv.py
import sys

def main():
    args = sys.argv

    nombre = args[1]
    edad   = args[2]

    print(f"Hola {nombre}, tenés {edad} años.")

if __name__ == "__main__":
    main()