import requests
from principal_login.get_workspace import main_token

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "+f"{main_token}"
}


def getApi(url):
    response = requests.get(url,headers = headers)
    return response

def postApi(url,payload):
    response = requests.post(url, json=payload, headers = headers)
    return response

def putApi(url,payload):
    response = requests.put(url, json=payload, headers = headers)
    return response.json()

def deleteApi(url, payload):
    response = requests.delete(url, json= payload, headers = headers)
    return response