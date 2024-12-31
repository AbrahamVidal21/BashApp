# Cargar las acciones desde el archivo config.json
import json

def cargar_acciones():
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
            return config.get("acciones", {})
    except FileNotFoundError:
        print("El archivo config.json no fue encontrado. Usando acciones predeterminadas.")
        return {
            "registrar": "registrar_usuario_interactivo",
            "listar": "listar_usuarios",
            "obtener_usuarioByEmail": "obtener_usuarioByEmail",
            "salir": "salir_del_programa",
        }
    except json.JSONDecodeError as e:
        print(f"Error al leer config.json: {e}. Usando acciones predeterminadas.")
        return {
            "registrar": "registrar_usuario_interactivo",
            "listar": "listar_usuarios",
            "obtener_usuarioByEmail": "obtener_usuarioByEmail",
            "salir": "salir_del_programa",
        }
