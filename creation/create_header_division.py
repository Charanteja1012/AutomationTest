from Settings.conftest import main_url
from principal_login.get_workspace import main_workspace,code
from principal_login.request_apis import postApi

def createe_header_division():
    url = f"{main_url}/headDivision/{main_workspace}"
    payload = {
        "name": "Popular Spices",
        "isActive": True,
        "companyCode": code,
        "code": "PS11"
    }
    res = postApi(url,payload)
    return res
    # print(res.json())


# createe_header_division()

