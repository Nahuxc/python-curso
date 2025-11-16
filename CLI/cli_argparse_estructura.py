"""
main.py
Plantilla base de CLI usando argparse.
- Contiene: build_parser(), handlers por subcomando, main()
- Comentarios en español para que entiendas cada paso.
"""

import argparse
import sys

# -------------------------
# Handlers: funciones que ejecutan la lógica de cada subcomando
# -------------------------
def handle_scrape(args):
    """
    Handler para el subcomando 'scrape'.
    Aquí debés poner la lógica que arme la URL, llame al scraper y guarde resultados.
    args.city -> nombre de la ciudad
    args.day  -> 0|1|2
    """
    # placeholder: aquí iría weather_service.scrape_city_day(args.city, args.day)
    print(f"[SCRAPE] Ejecutando scraping para ciudad='{args.city}', día={args.day}")
    # ejemplo de output que podés tener:
    # print("HTML descargado y parseado. Guardados X documentos en MongoDB.")

def handle_seed(args):
    """
    Handler para 'seed' (cargar ubicaciones desde JSON a la DB).
    args.path -> ruta al JSON con las ubicaciones
    """
    print(f"[SEED] Cargando ubicaciones desde: {args.path}")
    # placeholder: db.seed_locations(args.path)

def handle_list(args):
    """
    Handler para 'list' (listar ubicaciones guardadas en la DB).
    """
    print("[LIST] Listando ubicaciones en la base de datos...")
    # placeholder: print(db.list_locations())

def handle_runloop(args):
    """
    Handler para 'run-loop' (ejecutar el scraper indefinidamente cada N minutos).
    args.interval -> intervalo en minutos
    """
    print(f"[RUN-LOOP] Ejecutando en ciclo cada {args.interval} minutos (simulado).")
    # placeholder: iniciar bucle real con time.sleep(args.interval * 60)

# -------------------------
# Construcción del parser: centralizamos la configuración
# -------------------------
def build_parser() -> argparse.ArgumentParser:
    """
    Crea y devuelve el ArgumentParser configurado con subcomandos.
    Usá esta función como base y agregá argumentos según necesites.
    """

    parser = argparse.ArgumentParser(
        prog="proyecto_clima",
        description="Herramienta de scraping y guardado de pronósticos (proyecto clima).",
        epilog="Ejemplos: proyecto_clima scrape --city london --day 0"
    )

    # subparsers para agrupar subcomandos (scrape, seed, list, run-loop, ...)
    subparsers = parser.add_subparsers(dest="command", required=True)

    # -------------------------
    # subcomando: scrape
    # -------------------------
    p_scrape = subparsers.add_parser(
        "scrape",
        help="Ejecutar scraping para una ciudad y día específicos"
    )
    p_scrape.add_argument(
        "--city",
        type=str,
        required=True,
        help="Identificador de la ciudad (ej: london, new-york, rio-de-janeiro)"
    )
    p_scrape.add_argument(
        "--day",
        type=int,
        choices=[0, 1, 2],
        default=0,
        help="Día del pronóstico: 0=hoy, 1=mañana, 2=pasado (por defecto 0)"
    )
    # asociamos el handler a este subcomando
    p_scrape.set_defaults(func=handle_scrape)

    # -------------------------
    # subcomando: seed
    # -------------------------
    p_seed = subparsers.add_parser(
        "seed",
        help="Cargar ubicaciones desde un archivo JSON a la base de datos"
    )
    p_seed.add_argument(
        "--path",
        type=str,
        default="locations.json",
        help="Ruta al JSON con ubicaciones (por defecto: locations.json)"
    )
    p_seed.set_defaults(func=handle_seed)

    # -------------------------
    # subcomando: list
    # -------------------------
    p_list = subparsers.add_parser(
        "list",
        help="Listar ubicaciones guardadas en la base de datos"
    )
    p_list.set_defaults(func=handle_list)

    # -------------------------
    # subcomando: run-loop
    # -------------------------
    p_loop = subparsers.add_parser(
        "run-loop",
        help="Ejecutar el scraper en bucle indefinidamente (modo producción/test)"
    )
    p_loop.add_argument(
        "--interval",
        type=int,
        default=180,
        help="Intervalo en minutos entre ejecuciones (por defecto: 180)"
    )
    p_loop.set_defaults(func=handle_runloop)

    # Opcional: añadir un flag global, p.ej. debug o verbose
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Activar modo debug (imprime información adicional)"
    )

    return parser

# -------------------------
# Función main: parsea y despacha a handlers
# -------------------------
def main(argv=None):
    """
    main(): inicializa el parser, parsea args y llama al handler asociado.
    - argv: lista de argumentos (útil para testing); si es None usa sys.argv[1:].
    """
    parser = build_parser()

    # Si se pasa argv (lista), la usamos; si no, argparse lee sys.argv automáticamente
    args = parser.parse_args(argv)

    # Podemos chequear flags globales antes de ejecutar
    if getattr(args, "debug", False):
        print("[DEBUG] Argumentos parseados:", args)

    # args.func fue seteado por set_defaults en cada subparser; lo llamamos
    # (manejo defensivo: en caso de que no exista func)
    handler = getattr(args, "func", None)
    if handler is None:
        parser.print_help()
        return 1

    # Ejecutamos el handler con los argumentos parseados
    handler(args)
    return 0

# -------------------------
# Entry point
# -------------------------
if __name__ == "__main__":
    # Llamamos main() sin parámetros para usar sys.argv
    sys.exit(main())