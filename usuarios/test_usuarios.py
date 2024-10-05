# test_usuarios.py

import unittest
import uuid  # Para gerar emails únicos
from usuarios.usuarios import criar_usuario, listar_usuario

class TestUsuarios(unittest.TestCase):

    def setUp(self):
        self.nome = "Fulano da Silva"
        self.email = f"beltranqo_{uuid.uuid4()}@qa.com.br"  # Email único
        self.password = "teste"
        self.administrador = "true"

    def test_criar_usuario(self):
        response = criar_usuario(self.nome, self.email, self.password, self.administrador)
        print("Create User Response:", response.json())  # Print para depuração
        self.assertEqual(response.status_code, 201)  # Supondo que a criação retorne 201

        # Armazenando o ID do usuário criado para uso posterior
        self.usuario_id = response.json().get("_id")  # ID do usuário criado

    def test_listar_usuario(self):
        # Primeiro, crie o usuário
        create_response = criar_usuario(self.nome, self.email, self.password, self.administrador)
        usuario_id = create_response.json().get("_id")  # Supondo que o ID do usuário criado é retornado
        
        # Em seguida, liste o usuário
        response = listar_usuario(usuario_id)
        print("List User Response:", response.json())  # Print para depuração
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("email"), self.email)  # Verificando se o email corresponde

if __name__ == "__main__":
    unittest.main()