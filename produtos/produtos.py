import requests
from config import BASE_URL

BASE_URL_PRODUTOS = f"{BASE_URL}/produtos"

def cadastrar_produto(nome, preco, descricao, quantidade, token):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": token
    }
    payload = {
        "nome": nome,
        "preco": preco,
        "descricao": descricao,
        "quantidade": quantidade
    }
    
    response = requests.post(BASE_URL_PRODUTOS, json=payload, headers=headers)
    return response

def listar_produto_por_id(produto_id):
    headers = {
        "accept": "application/json"
    }
    
    response = requests.get(f"{BASE_URL_PRODUTOS}/{produto_id}", headers=headers)
    return response

def listar_todos_produtos():
    headers = {
        "accept": "application/json"
    }
    
    response = requests.get(BASE_URL_PRODUTOS, headers=headers)
    return response

def excluir_produto(produto_id, token):
    headers = {
        "Authorization": token
    }
    
    response = requests.delete(f"{BASE_URL_PRODUTOS}/{produto_id}", headers=headers)
    return response