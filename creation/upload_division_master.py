from Settings.conftest import main_url
from principal_login.request_apis import postApi
from principal_login.get_workspace import main_workspace,code
from creation.create_header_division import createe_header_division

header_division_res = createe_header_division().json()

def test_create_division_masters():
    payload = {
        "entity": "DIVISION_MASTER",
        "fileName": "Division_masters.py",
        "records": [
            {
                "name": "grams",
                "isActive": True,
                "companyCode": code,
                "code": "GR",
                "stateCode": "27",
                "headDivisionCode": header_division_res["division"]["code"],
                "isDefault": False
            },
            {
                "name": "Rice",
                "isActive": True,
                "companyCode": code,
                "code": "RS",
                "stateCode": "27",
                "headDivisionCode": header_division_res["division"]["code"],
                "isDefault": False
            }
        ],
        "companyCode": code,
        "workspaceId": main_workspace
    }
    url = f"{main_url}/mdm-integration/uploadbatch"
    res = postApi(url,payload)
    print(res.json())
    print(res)