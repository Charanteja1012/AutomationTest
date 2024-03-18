import requests
from principal_login.get_workspace import main_token, main_workspace
from Settings.conftest import main_url

def add_products_in_principal():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+f"{main_token}"
    }
    payload = {"parentSku":"123456","name":"Tea powder","productVariants":[{"name":"Tea powder","sku":"123456","sortOrder":0,"shortName":"Tea powder","shortDescription":"tea","taxCategoryCode":"GST-12","hsnCode":"1234","baseUom":"KG","packSize":1,"minOrderQty":10,"maxOrderQty":50,"qtyMultiplier":10,"grossWeight":0,"netWeight":0,"volume":0,"warrentyInformation":"","condition":"","facets":[],"MRP":5000,"PTR":3800,"price":3000,"upcCode":"1234","stock":0,"ZINS":False,"listPrice":0,"sales":0,"minRemShelfLife":0,"expiryDate":"2025-09-11","manufacturingDate":"2024-02-14","bestBeforeOrAfter":"Before","bestAfter":"6 Months","ean":"","erpId":"","erpUOM":"","erpPriceUOM":"","quantity":0}],"customFields":{},"productAttributes":[{"baseUom":"KG","packSize":1}]}
    url = f"{main_url}/commerce-v2/products/{main_workspace}"
    res = requests.post(url, json=payload, headers=headers)
    return res


