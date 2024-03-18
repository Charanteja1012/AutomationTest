from Settings.conftest import main_url
from principal_login.request_apis import postApi
from principal_login.get_workspace import main_workspace
from creation.create_cfa import create_cfa
from creation.create_division import create_division

cfa_res = create_cfa().json()
division_res = create_division().json()


def test_create_product():
    url = f"{main_url}/commerce-v2/products/{main_workspace}"
    payload = {
        "name": "EGG CURRY MASALA",
        "description": "EGG CURRY MASALA",
        "parentSku": "03012401",
        "collections": [
            "NUTR"
        ],
        "productVariants": [
            {
                "name": "EGG CURRY MASALA",
                "sku": "03012401",
                "listPrice": 1000,
                "shortName": "EGG CURRY MASALA",
                "shortDescription": "EGG CURRY MASALA",
                "facets": [],
                "taxCategoryCode": "GST-12",
                "erpId": "000000000001157047",
                "erpUOM": "STR",
                "enabled": True,
                "hsnCode": "21069099",
                "baseUom": "STR",
                "packSize": 1,
                "minOrderQty": 1,
                "netWeight": 14.55,
                "weightUOM": "KG",
                "volumeUOM": "FT3",
                "erpPriceUOM": "STR",
                "MRP": 1000,
                "PTR": 850,
                "isSpecial": False,
                "ZINS": False,
                "minRemShelfLife": 128
            }
        ],
        "customFields": {},
        "divisionCFACodes": [
            {
                "cfaCode": cfa_res["cfa"]["code"],
                "divisionCode": division_res["division"]["code"],
                "isActive": True,
                "packSize": 3,
                "minOrderQty": 3
            }
        ]
    }
    res = postApi(url,payload)
    print(res.json())