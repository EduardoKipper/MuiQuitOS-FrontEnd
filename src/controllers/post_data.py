import requests
from datetime import datetime
from src.utils import DATA_URL

def post_data(user: str, cep: int, intensity: int):
    payload = {
        "user": user,
        "cep": cep,
        "intensity": intensity,
        "date": datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    }
    try:
        # response = requests.post(DATA_URL, json=payload)
        # if response.content == "OK":
            # return True
        # return False
        return True
    except:
        return False
