#%%
import requests
import json
APIUrl = "http://127.0.0.1:8000/"
# %%
query = {"userId": 'U4b95521900347bfce99dda2206a20c74'}
r = requests.post(APIUrl+'user', json=query)
r.content

# %%
