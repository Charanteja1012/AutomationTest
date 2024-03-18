from creation.create_cfa import create_cfa
from creation.create_division import create_division
from principal_login.get_workspace import main_workspace,code
from Settings.conftest import main_url
from principal_login.request_apis import postApi
from principal_login.get_products import get_products

products_res = get_products().json()
cfa_res = create_cfa().json()
division_res = create_division().json()


def test_create_scheme_with_discount():
    payload = {
        "name": "Jan-Disc-offer",
        "enabled": True,
        "startsAt": "2024-03-11T00:00:00.000Z",
        "endsAt": "2024-07-13T00:00:00.000Z",
        "skus": [
            products_res["products"][0]["parentSku"]
        ],
        "stateCodes": [],
        "customerCodes": [],
        "promotionCode": "765489",
        "cfaDivisionCodes": [
            {
                "cfaCode": cfa_res["cfa"]["code"],
                "divisionCode": division_res["division"]["code"]
            }
        ],
        "slabs": [
            {
                "minimumQty": 10,
                "maximumQty": 500,
                "discountPercentage": 20.0,
                "entity": "product"
            }
        ]
    }
    url = f"{main_url}/commerce-v2/scheme/v2/productdiscount/{main_workspace}"
    res = postApi(url,payload)
    print(res.json())
    print(res.status_code)