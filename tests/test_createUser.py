import unittest
#from database.createUser import registrar_usuario
from database.usuario import registrar_usuario
from models.usuario import Usuario
from unittest.mock import patch, MagicMock


class TestCreateUser(unittest.TestCase):
    
    @patch('database.createUser.Conexion.conexionDataBase')
    def test_registrar_usuario(self, mock_conexion):
        # Simula la conexión a la base de datos
        mock_conexion.return_value = True  # Simula que la conexión fue exitosa
        
        # Crea un usuario para registrar
        usuario = Usuario("John", "Doe", "john.doe@example.com", "01/01/1990", False)
        
        # Llama a la función de registro
        registrar_usuario(usuario)
        
        # Verifica si la función de conexión fue llamada
        mock_conexion.assert_called_once()

if __name__ == '__main__':
    unittest.main()
