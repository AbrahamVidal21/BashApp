# Asociar los nombres de las funciones con las funciones reales
from controller.usuario import listar_usuario_por_email, registrar_usuario_interactivo, listar_usuarios
from .salir import salir_del_programa

def obtener_funcion(nombre_funcion):
    funciones_disponibles = {
        "registrar_usuario_interactivo": registrar_usuario_interactivo,
        "listar_usuarios": listar_usuarios,
        "obtener_usuarioByEmail": listar_usuario_por_email,
        "salir_del_programa": salir_del_programa
    }
    return funciones_disponibles.get(nombre_funcion, None)