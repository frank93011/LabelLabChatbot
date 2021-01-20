#%%
import requests
import json
APIUrl = "https://labellab-backend.herokuapp.com/"
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
    "userId": "U5757018f29d8fa358d147c40eab3391f",
    "labelCount": 1,
}
r = requests.post(APIUrl+'task/getLabel', json=query)
response = r.json()
response
# %%
query = {
    "taskType": "classification",
    "userId": "U4b95521900347bfce99dda2206a20c74",
    "taskId": "taskId1f54c47a361b40f9",
    "classification": "airplane",
    "labelIdList": ['labelId249dbd179b5f4dce']
}
r = requests.post(APIUrl+'saveAnswer', json=query)
response = r.json()
response
# %%
query = {
    "taskType": "classification",
    "userId": "U4b95521900347bfce99dda2206a20c74",
    "taskId": "taskId1f54c47a361b40f9",
    "transactionId": "transId46bd8da6c7a34893"
}
r = requests.post(APIUrl+'accuracy', json=query)
response = r.json()
response
# %%
query = {"taskId": 'taskId1f54c47a361b40f9'}
r = requests.post(APIUrl+'task', json=query)
response = r.json()

# %%
accuracy = """
{
  "type": "bubble",
  "size": "micro",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "準確程度",
        "color": "#ffffff",
        "align": "start",
        "size": "lg",
        "gravity": "center",
        "weight": "bold"
      },
      {
        "type": "text",
        "text": "{}%",
        "color": "#ffffff",
        "align": "start",
        "size": "xs",
        "gravity": "center",
        "margin": "lg"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "filler"
              }
            ],
            "width": "{}%",
            "backgroundColor": "#0D8186",
            "height": "6px"
          }
        ],
        "backgroundColor": "#9FD8E36E",
        "height": "6px",
        "margin": "sm"
      }
    ],
    "backgroundColor": "#27ACB2",
    "paddingTop": "19px",
    "paddingAll": "12px",
    "paddingBottom": "16px"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Title"
      }
    ],
    "spacing": "md",
    "paddingAll": "12px"
  },
  "styles": {
    "footer": {
      "separator": false
    }
  }
}
"""
new = accuracy.replace("{}", "70").replace("Title", "物品圖片分類")
a = json.loads(new)

# %%
a['header']
# %%
