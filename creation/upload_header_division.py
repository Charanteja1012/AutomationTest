from Settings.conftest import main_url
from principal_login.get_workspace import main_workspace,code
from principal_login.request_apis import postApi


def test_header_division_masters():
    payload = {
        "entity": "HEADER_DIVISION_MASTER",
        "fileName": "headerDivisions.csv",
        "records": [
            {
                "code": "HD1",
                "name": "Header Division1",
                "companyCode": code,
                "isDefault": False,
                "isActive": True
            },
            {
                "code": "HD2",
                "name": "Header Division2",
                "companyCode": code,
                "isDefault": False,
                "isActive": True
            }
        ],
        "companyCode": code,
        "workspaceId": main_workspace
    }
    url = f"{main_url}/mdm-integration/uploadbatch"
    res = postApi(url,payload)
    print(res.json())

