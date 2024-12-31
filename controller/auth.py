# controller/auth.py

from database.conexion import Conexion

def verificar_correo_existente(email):
    conexion = Conexion.conexionDataBase()
    if conexion is not None:
        cursor = conexion.cursor()
        cursor.execute("SELECT email FROM usuarios WHERE LOWER(email) = LOWER(?)", (email,))
        result = cursor.fetchone()
        conexion.close()
        return result is None
    return False
