from database.db_setup import inicializar_base_de_datos
from utils import cargar_acciones, animacion_proceso, obtener_funcion


def main():
    print("Inicializando base de datos...")
    inicializar_base_de_datos()
    print("Base de datos inicializada correctamente.\n")

    acciones = cargar_acciones()

    while True:
        # Mostrar las acciones disponibles en cada iteración
        print("\nAcciones disponibles:")
        for i, accion in enumerate(acciones.keys(), start=1):
            print(f"{i}. {accion.capitalize()}")

        opcion = input("\nSelecciona una opción: ").strip()
        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(acciones):
            print("Opción inválida. Por favor, elige una opción válida.")
            animacion_proceso(3)
            continue

        accion_seleccionada = list(acciones.keys())[int(opcion) - 1]
        nombre_funcion = acciones[accion_seleccionada]
        funcion = obtener_funcion(nombre_funcion)

        if funcion:
            funcion()
            animacion_proceso(3)
            if accion_seleccionada == "salir":
                break
        else:
            print(f"Acción '{accion_seleccionada}' no tiene una función asociada.")

if __name__ == "__main__":
    main()
