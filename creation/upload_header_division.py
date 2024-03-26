from Settings.conftest import main_url
from principal_login.get_workspace import main_workspace,code
from creation.get_token_for_mdm import token_for_upload
import requests

workspace_Auth = token_for_upload().json()["token"]


def test_header_division_masters():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+f"{workspace_Auth}"
    }
    payload = {
        "entity": "HEADER_DIVISION_MASTER",
        "fileName": "headerDivisions.csv",
        "records": [
            {
                "code": "HD01",
                "name": "Header Division01",
                "companyCode": code,
                "isDefault": False,
                "isActive": True
            },
            {
                "code": "HD02",
                "name": "Header Division02",
                "companyCode": code,
                "isDefault": False,
                "isActive": True
            }
        ],
        "companyCode": code,
        "workspaceId": main_workspace
    }
    url = f"{main_url}/mdm-integration/uploadbatch"
    res = requests.post(url,json = payload, headers = headers)
    print(res.json())

