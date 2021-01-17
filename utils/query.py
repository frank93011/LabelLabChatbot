import requests
from app import APIUrl

def login(user_id):
    query = {"userId": user_id}
    r = requests.post(APIUrl+'user', json=query)
    if(r.ok):
        return r.json()
    else:
        return False