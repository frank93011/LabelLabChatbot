import requests
from app import APIUrl
from linebot.models import QuickReplyButton, PostbackAction

### 查詢使用者資料回傳
def login(user_id):
    query = {"userId": user_id}
    r = requests.post(APIUrl+'user', json=query)
    if(r.ok):
        if(r.json()['success']):
            return r.json()['data']
        else:
            print(r.json())
            return False
    else:
        return False

def get_all_tasks():
    r = requests.get(APIUrl+'tasks')
    if(r.ok):
        if(r.json()['success']):
            return r.json()['data']
        else:
            print(r.json())
            return False
    else:
        return False

def get_all_options(taskId):
    query = {"taskId": taskId}
    r = requests.post(APIUrl+'task/getQuestion', json=query)
    if(r.ok):
        if(r.json()['success']):
            return r.json()['data']
        else:
            print(r.json())
            return False
    else:
        return False

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
        if(r.json()['success']):
            response = r.json()['data']
            result['url'] = response['labelList'][0]['imagePath'].replace("http", "https")
            result['labelId'] = response['labelList'][0]['labelId']
            result['taskId'] = taskId
            return result
        else:
            print(r.json())
            return False
    else:
        return False

def startTask(userId, taskId, transactionId=None):
    options = get_all_options(taskId)
    labelObject = get_question(userId, taskId)
    if(not labelObject):
        return False, False
    url = labelObject['url']
    replyItems = []
    for option in options:
        if(not transactionId):
            replyItems.append(
                QuickReplyButton(
                        action=PostbackAction(label=option, data="action=answerTask&taskId={}&labelId={}&answer={}".format(taskId, labelObject['labelId'],option))
                )
            )
        else:
            replyItems.append(
                QuickReplyButton(
                        action=PostbackAction(label=option, data="action=answerTask&taskId={}&labelId={}&answer={}&transactionId={}".format(taskId, labelObject['labelId'], option, transactionId))
                )
            )
    replyItems.append(
        QuickReplyButton(
                action=PostbackAction(label="結束作答", data="action=endTask&taskId={}&labelId={}&answer={}&transactionId={}".format(taskId, labelObject['labelId'], "結束作答", transactionId))
        ))
    return url, replyItems

def answerTask(userId, taskId, labelId, answer, transactionId=None):
    query = {
        "taskType": "classification",
        "userId": userId,
        "taskId": taskId,
        "classification": answer,
        "labelIdList": [labelId]
    }
    if(transactionId):
        query.update({'transactionId': transactionId})
    r = requests.post(APIUrl+'saveAnswer', json=query)
    if(r.ok):
        if(r.json()['success']):
            return r.json()['data']
        else:
            print(r.json())
            return False
    else:
        return False

def endTask(userId, taskId, transactionId):
    query = {
        "taskType": "classification",
        "userId": userId,
        "taskId": taskId,
        "transactionId": transactionId
    }
    r = requests.post(APIUrl+'accuracy', json=query)
    if(r.ok):
        if(r.json()['success']):
            return r.json()['data']
        else:
            print(r.json())
            return False
    else:
        return False
