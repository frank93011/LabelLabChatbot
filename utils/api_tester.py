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

query = {"taskId": 'taskId1f54c47a361b40f9'}
r = requests.post(APIUrl+'task/getQuestion', json=query)
response = r.json()
# %%
query = {
    "taskId":'taskId1f54c47a361b40f9',
    "taskType": "classification",
    "userId": "U4b95521900347bfce99dda2206a20c74",
    "labelCount": 1,
}
r = requests.post(APIUrl+'task/getLabel', json=query)
response = r.json()
response
# %%
