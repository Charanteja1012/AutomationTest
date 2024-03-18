from Settings.conftest import main_url
from principal_login.request_apis import postApi
from principal_login.get_workspace import main_workspace,code
from creation.create_header_division import createe_header_division

header_division_res = createe_header_division().json()

def create_division():
    url = f"{main_url}/division/{main_workspace}"
    payload = {
        "name": "Popular Spices",
        "isActive": True,
        "companyCode": code,
        "code": "PS1",
        "stateCode": "String",
        "headDivisionCode": header_division_res["division"]["code"],
        "isDefault": False
    }
    res = postApi(url,payload)
    # print(res.json())
    return res

# create_division()