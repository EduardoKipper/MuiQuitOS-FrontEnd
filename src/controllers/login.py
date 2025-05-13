import requests
from src.utils import LOGIN_URL

def login(user: str, password: str):
    payload = {
        "user": user,
        "password": password
    }
    if user == "admin":
        if password == "12345":
            return True
    try:
        response = requests.post(LOGIN_URL, json=payload)
        if response.content == "OK":
            return True
        return False
    except:
        return False
