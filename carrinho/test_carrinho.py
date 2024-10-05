# test_carrinho.py

import unittest
from carrinho.carrinho import Carrinho

class TestCarrinho(unittest.TestCase):

    def setUp(self):
        self.carrinho = Carrinho()

    def test_listar_todos_carrinhos(self):
        response = self.carrinho.listar_todos_carrinhos()
        print("List All Carts Response:", response.json())  # Print para depuração
        self.assertEqual(response.status_code, 200)  # Verifica se o GET foi bem-sucedido

if __name__ == "__main__":
    unittest.main()