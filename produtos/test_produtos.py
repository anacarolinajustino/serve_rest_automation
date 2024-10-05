import unittest
import uuid
from config import EMAIL, PASSWORD
from login.login import login
from produtos.produtos import cadastrar_produto, listar_todos_produtos, listar_produto_por_id, excluir_produto

class TestProdutos(unittest.TestCase):

    def setUp(self):
        response = login(EMAIL, PASSWORD)
        self.token = response.json().get("authorization")
        print("Token:", self.token)
        
        if not self.token:
            self.skipTest("Token de autenticação não obtido, testando o login.")

        self.nome = f"Produto-{uuid.uuid4()}"
        self.preco = 470
        self.descricao = "Mouse"
        self.quantidade = 381
        
        self.create_response = cadastrar_produto(self.nome, self.preco, self.descricao, self.quantidade, self.token)
        self.produto_id = self.create_response.json().get("_id")

    def test_cadastrar_produto(self):
        print("Create Product Response:", self.create_response.json())
        self.assertEqual(self.create_response.status_code, 201)

    def test_criar_buscar_deletar_listar(self):
        response = listar_produto_por_id(self.produto_id)
        print("Get Product Response:", response.json())
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("nome"), self.nome)

        response_delete = excluir_produto(self.produto_id, self.token)
        print("Delete Product Response:", response_delete.json())
        self.assertEqual(response_delete.status_code, 200)

        response_check = listar_produto_por_id(self.produto_id)
        print("Check Deleted Product Response:", response_check.json())
        self.assertEqual(response_check.status_code, 404)  

    def test_listar_todos_produtos(self):
        response = listar_todos_produtos()
        print("List All Products Response:", response.json())
        
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(self.nome, [produto['nome'] for produto in response.json().get("produtos", [])])

if __name__ == "__main__":
    unittest.main()