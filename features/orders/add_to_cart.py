from Settings.conftest import main_url
from user_login.get_workspace import main_workspace
from Settings.api_requests import postApi
from features.products.get_products import get_products

products_res = get_products().json()

def add_to_cart():
    payload = {
        "customerId": main_workspace[0]["cId"],
        "sellerWorkspaceId": main_workspace[0]["pId"],
        "source": "manual",
        "lines": [
            {"productVariantId": variant["productVariantId"], "quantity": variant["minOrderQty"], "operator": "add"}
            for product in products_res["products"]
            for variant in product["productVariants"]
        ]

    }
    url = f"{main_url}/commerce-v2/orders/additemtoactiveorder/{main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    return res