import unittest
import uuid
from usuarios.usuarios import criar_usuario, listar_usuario

class TestUsuarios(unittest.TestCase):

    def setUp(self):
        self.nome = "Fulano da Silva"
        self.email = f"beltranqo_{uuid.uuid4()}@qa.com.br" 
        self.password = "teste"
        self.administrador = "true"

    def test_criar_usuario(self):
        response = criar_usuario(self.nome, self.email, self.password, self.administrador)
        print("Create User Response:", response.json())  
        self.assertEqual(response.status_code, 201)  

        self.usuario_id = response.json().get("_id") 
        
    def test_listar_usuario(self):
        create_response = criar_usuario(self.nome, self.email, self.password, self.administrador)
        usuario_id = create_response.json().get("_id")
        response = listar_usuario(usuario_id)
        print("List User Response:", response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("email"), self.email)

if __name__ == "__main__":
    unittest.main()