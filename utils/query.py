import requests
from app import APIUrl

def login(user_id):
    query = {"userId": user_id}
    r = requests.post(APIUrl+'user', json=query)
    if(r.ok):
        return r.json()
    else:
        return False

def get_all_tasks():
    r = requests.get(APIUrl+'tasks')
    if(r.ok):
        return r.json()
    else:
        return False

def get_all_options(taskId):
    query = {"taskId": taskId}
    r = requests.post(APIUrl+'task/getQuestion', json=query)
    if(r.ok):
        return r.json()

def get_question(userId, taskId):
    query = {
        "taskId":taskId,
        "taskType": "classification",
        "userId": userId,
        "labelCount": 1,
    }
    r = requests.post(APIUrl+'task/getLabel', json=query)
    result = {}
    if(r.ok):
        response = r.json()
        result['url'] = response['labelList'][0]['imagePath']
        result['labelId'] = response['labelList'][0]['labelId']
        result['taskId'] = taskId
        return result