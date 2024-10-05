# carrinho.py

import requests
from produtos.produtos import listar_todos_produtos

BASE_URL_CARRINHOS = "https://serverest.dev/carrinhos"

class Carrinho:
    def __init__(self):
        self.produtos = []

    def listar_produtos(self):
        response = listar_todos_produtos()
        if response.status_code == 200:
            return response.json().get("produtos", [])
        return []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_carrinho(self):
        return self.produtos

    def limpar_carrinho(self):
        self.produtos.clear()

    def listar_todos_carrinhos(self):
        headers = {"accept": "application/json"}
        response = requests.get(BASE_URL_CARRINHOS, headers=headers)
        return response