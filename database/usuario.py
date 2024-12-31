# database/createUser.py
# Solo admite operaciones con la base de datos

import sqlite3
from database.conexion import Conexion

def registrar_usuario(usuario):
    try:
        conexion = Conexion.conexionDataBase()
        if conexion is not None:
            with conexion:
                cursor = conexion.cursor()
                cursor.execute("""
                    INSERT INTO usuarios (name, lastname, email, birthday, banned)
                    VALUES (?, ?, ?, ?, ?)
                """, (usuario.name, usuario.lastname, usuario.email, usuario.birthday, usuario.banned))
            print("Usuario registrado correctamente.")
    except sqlite3.Error as e:
        print(f"Error al registrar el usuario: {e}")

def getOne_User(email):
    try:
        conexion = Conexion.conexionDataBase()
        if not conexion:
            print("Error al conectar con la base de datos.")
            return None
        with conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
            usuario = cursor.fetchone()
        return usuario
    except sqlite3.Error as e:
        print(f"Error al buscar el usuario: {e}")
        return None
