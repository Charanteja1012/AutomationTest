import requests
from creation.get_token_from_superadmin import token
from Settings.conftest import main_url
from principal_login.get_workspace import main_workspace

def principal_data():
    headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "+f"{token}"
    }

    url = f"{main_url}/admin/workspaceAuthentication/details?workspaceId={main_workspace}"
    # print("url------------------------->",url)

    res = requests.get(url, headers=headers)
    return res
    # print(res.json())


# principal_data()