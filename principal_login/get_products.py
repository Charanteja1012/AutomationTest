from Settings.conftest import main_url
from principal_login.request_apis import postApi
from principal_login.get_workspace import main_workspace

def get_products():
    url = f"{main_url}/commerce-v2/products/search/{main_workspace}?pageNo=1&pageSize=20"
    payload = {}
    res = postApi(url,payload)
    return res