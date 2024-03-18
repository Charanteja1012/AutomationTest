from creation.create_cfa import create_cfa
from creation.create_division import create_division
from principal_login.get_workspace import main_workspace
from Settings.conftest import main_url
from principal_login.request_apis import postApi
from principal_login.get_products import get_products
products_res = get_products().json()

cfa_res = create_cfa().json()
division_res = create_division().json()

def test_create_scheme_with_buyXandgetY():
    payload = {
        "name": "Buy X-Get Y",
        "enabled": True,
        "startsAt": "2024-03-11T00:00:00.000Z",
        "endsAt": "2024-05-20T00:00:00.000Z",
        "promotionCode": "09876",
        "cfaDivisionCodes": [
            {
                "cfaCode": cfa_res["cfa"]["code"],
                "divisionCode": division_res["division"]["code"]
            }
        ],
        "slabs": [
            {
                "qtyXFrom": "10",
                "qtyXTo": "200",
                "qtyY": "2",
                "type": "inclusive",
                "SkusX": [
                    products_res["products"][1]["parentSku"]
                ],
                "SkusY": [
                    products_res["products"][3]["parentSku"]
                ]
            }
        ]
    }
    url = f"{main_url}/commerce-v2/scheme/v2/buyXgetYfree/{main_workspace}"
    res = postApi(url,payload)
    print(res.json())
    print(res.status_code)

