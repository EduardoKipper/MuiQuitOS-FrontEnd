import requests
from src.utils import DATA_URL

def get_data():
    try:
        response = requests.get(DATA_URL)
        if response.status_code == 200:
            return response.json()
        return False
    except:
        return False
