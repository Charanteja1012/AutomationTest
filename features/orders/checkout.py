from Settings.conftest import main_url
from user_login.get_workspace import main_workspace
from Settings.api_requests import postApi
from features.orders.add_to_cart import add_to_cart

add_to_cart_res = add_to_cart().json()

def check_out():
    payload = {
        "sellerWorkspaceId": main_workspace[0]["pId"],
        "customerId": main_workspace[0]["cId"],
        "poFileIds": [add_to_cart_res["orders"][0]["pofileId"]]
    }
    url = f"{main_url}/commerce-v2/orders/checkout/{main_workspace[0]["pId"]}"
    res= postApi(url,payload)
    return res
    # print(res.json())