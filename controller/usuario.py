# controller/usuario.py
# Solo efectua interacciones con el usuario

from models.usuario import Usuario
from controller.auth import verificar_correo_existente
from database.conexion import Conexion
from database.usuario import getOne_User, registrar_usuario
import sqlite3

def registrar_usuario_interactivo():
    print('Para registrar un usuario, ingrese los siguientes datos: Nombre, Apellido, email, cumpleaños(dd/mm/yyyy)')

    name = input('Nombre: ').lower()
    lastname = input('Apellido: ').lower()

    while True:
        email = input('Email: ').lower().strip()
        if not verificar_correo_existente(email):
            print("El correo electrónico ya está registrado en nuestra base de datos. Por favor, ingresa uno diferente.")
            continuar = input("¿Deseas intentar con otro correo? (si/no): ").strip().lower()
            if continuar == 'no':
                print("Saliendo del registro.")
                return
        break  # Validación exitosa del correo

    birthday = input('Cumpleaños (dd/mm/yy): ').lower()
    banned = False

    usuario = Usuario(name, lastname, email, birthday, banned)
    registrar_usuario(usuario)
    print('Usuario registrado correctamente. Gracias, Vuelva Pronto.')

def listar_usuarios():
    try:
        conexion = Conexion.conexionDataBase()
        if conexion:
            with conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM usuarios")
                usuarios = cursor.fetchall()
                if usuarios:
                    print("Usuarios registrados:")
                    for usuario in usuarios:
                        print(f"ID: {usuario[0]}, Nombre: {usuario[2]}, Apellido: {usuario[3]}, Email: {usuario[4]}, Cumpleaños: {usuario[5]}, Baneado: {usuario[6]}")
                else:
                    print("No hay usuarios registrados.")
    except sqlite3.Error as e:
        print(f"Error al listar usuarios: {e}")

def listar_usuario_por_email():
    email = input("Ingresa el correo electrónico a buscar: ").strip()
    usuario = getOne_User(email)
    if usuario:
        print(f"\nUsuario encontrado: {str(usuario[2]).capitalize()} {str(usuario[3]).capitalize()}")
        print(f"ID: {usuario[0]}")
        print(f"Nombre: {usuario[2]}")
        print(f"Apellido: {usuario[3]}")
        print(f"Email: {usuario[4]}")
        print(f"Cumpleaños: {usuario[5]}")
        print(f"Baneado: {'Sí' if usuario[6] else 'No'}\n")
    else:
        print(f"No se encontró ningún usuario con el correo: {email}\n")