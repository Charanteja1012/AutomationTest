from Settings.conftest import main_url
from principal_login.request_apis import postApi
from principal_login.get_workspace import main_workspace,code
from creation.create_cfa import create_cfa
from creation.create_division import create_division

cfa_res = create_cfa().json()
division_res = create_division().json()

mobile_number = 1111112222

def test_create_customer():
    url = url = f"{main_url}/customers/create/{main_workspace}"
    payload = {
            "phone": f"091{mobile_number}",
            "phone2": "",
            "companyCode": code,
            "isActive": True,
            "customerDetails": {
                "telephone": "+911212312123",
                "email": "ss12345@yopmail.com",
                "CSTNumber": 0,
                "gstin": "19AIIPS2130H1Z3",
                "dlNumber": "DL-CB--1183-SW",
                "dlExpiry": "2026-12-31",
                "distributorChannel": "",
                "grossCreditLimit": 0,
                "creditLimitPeriod": 0,
                "shippingAddress": {
                    "shippingAddress1": "",
                    "shippingAddress2": ""
                },
                "distributorCode": "123412",
                "name": "amar",
                "companyName": "VSRR",
                "physicalAddress": {
                    "address1": "Malakpet",
                    "address2": "LB nagar"
                },
                "postalCode": "500060",
                "stateId": "24b724f9-0579-4c40-b84a-5f75639ca1dc",
                "countryId": "e4d36d67-aa3d-4343-a865-fedd78544e11",
                "cityName": "Hyderabad"
            },
            "cfa": [
                {
                    "divisionCodes": [
                        {
                            "code": division_res["division"]["code"],
                            "isActive": True
                        }
                    ],
                    "cfaCode": cfa_res["cfa"]["code"],
                    "salesOrg": ""
                }
            ]
        }
    res = postApi(url,payload)
    print(res.json())