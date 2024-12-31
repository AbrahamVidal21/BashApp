import sqlite3
from database.conexion import Conexion
import os

def verificar_base_de_datos(db_path="SqliteDB.db"):
    """
    Verifica si el archivo de la base de datos existe.
    """
    return os.path.exists(db_path)

def inicializar_base_de_datos():
    """
    Verifica la existencia de la base de datos y crea las tablas necesarias.
    """
    if not verificar_base_de_datos():
        print("Base de datos no encontrada. Creando base de datos y tablas necesarias...")
        crear_tabla_usuarios()
    else:
        print("Base de datos existente. Verificando tablas necesarias...")
        crear_tabla_usuarios()

def crear_tabla_usuarios():
    conexion = Conexion.conexionDataBase()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    name TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    birthday DATE NOT NULL,
                    banned BOOLEAN DEFAULT FALSE
                )
            ''')
            conexion.commit()
            print('Tabla "usuarios" creada correctamente.')
        except sqlite3.Error as error:
            print(f'Error al crear la tabla: {error}')
        finally:
            conexion.close()


# Inicializar la base de datos si ejecutas este archivo directamente
if __name__ == "__main__":
    crear_tabla_usuarios()