import unittest
#from database.createUser import registrar_usuario
from database.usuario import registrar_usuario
from models.usuario import Usuario
from unittest.mock import patch, MagicMock

class TestDatabase(unittest.TestCase):

    @patch('database.createUser.Conexion.conexionDataBase')  # Aquí reemplazamos la conexión real a la base de datos
    def test_registrar_usuario(self, mock_conexion):
        # Crear un objeto mock para la base de datos
        mock_db = MagicMock()
        mock_conexion.return_value = mock_db

        # Crear un usuario de prueba
        usuario = Usuario("Juan", "Pérez", "juan@example.com", "01/01/1990", False)

        # Ejecutar la función que registra al usuario
        registrar_usuario(usuario)

        # Verificar que la instrucción SQL fue ejecutada correctamente con los valores esperados
        mock_db.cursor.return_value.execute.assert_called_with(
            """INSERT INTO usuarios (name, lastname, email, birthday, banned) VALUES (?, ?, ?, ?, ?)""",
            ("Juan", "Pérez", "juan@example.com", "01/01/1990", False)
        )

        # Verificar que la conexión fue cerrada al final
        mock_db.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
