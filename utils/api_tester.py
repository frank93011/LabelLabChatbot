#%%
import requests
import json
APIUrl = "http://140.112.251.124:8000/"
# %%
query = {"userId": 'U4b95521900347bfce99dda2206a20c74'}
r = requests.post(APIUrl+'user', json=query)
response = r.json()

# %%
sum(list(response.values()))
# %%
r = requests.get(APIUrl+'tasks')
response = r.json()
response
# %%
