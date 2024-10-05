import requests
from config import BASE_URL

BASE_URL_LOGIN = f"{BASE_URL}/login"

def login(email, password):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "email": email,
        "password": password
    }
    
    response = requests.post(BASE_URL_LOGIN, json=payload, headers=headers)
    return response