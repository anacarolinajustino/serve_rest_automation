import requests
from config import BASE_URL

BASE_URL_USUARIOS = f"{BASE_URL}/usuarios"

def criar_usuario(nome, email, password, administrador):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "nome": nome,
        "email": email,
        "password": password,
        "administrador": administrador
    }
    
    response = requests.post(BASE_URL_USUARIOS, json=payload, headers=headers)
    return response

def listar_usuario(usuario_id):
    headers = {
        "accept": "application/json"
    }
    
    response = requests.get(f"{BASE_URL_USUARIOS}/{usuario_id}", headers=headers)
    return response