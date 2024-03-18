from Settings.conftest import main_url
from Settings.api_requests import postApi
from user_login.get_workspace import main_workspace

def get_products():
    url = f"{main_url}/commerce-v2/products/search/{main_workspace[0]["pId"]}?pageNo=1&pageSize=1&customerId={main_workspace[0]["cId"]}"
    payload = {}
    res = postApi(url,payload)
    return res
    # print(res.json())



