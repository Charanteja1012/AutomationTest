from creation.create_cfa import create_cfa
from creation.create_division import create_division
from principal_login.get_workspace import main_workspace,code
from Settings.conftest import main_url
from principal_login.request_apis import postApi
cfa_res = create_cfa().json()
division_res = create_division().json()

def test_customers_upload():
    payload = {
        "entity": "CUSTOMER_MASTER",
        "fileName": "customers.csv",
        "records": [
            {
                "phone": "0918787878778",
                "phone2": "",
                "companyCode": code,
                "isActive": True,
                "customerDetails": {
                    "telephone": "",
                    "email": "c2112@cupmail.com",
                    "CSTNumber": 11,
                    "gstin": "19AIIAS2240Y2S8",
                    "dlNumber": "15876",
                    "dlExpiry": "2024-05-21",
                    "distributorChannel": "",
                    "shippingAddress": {
                        "shippingAddress1": "Sector-11",
                        "shippingAddress2": "Bhilai"
                    },
                    "distributorCode": "90987",
                    "name": "sharma",
                    "companyName": "b21",
                    "physicalAddress": {
                        "address1": "pune",
                        "address2": "nanded"
                    },
                    "postalCode": "500094",
                    "stateCode": "36",
                    "countryCode": "IN",
                    "cityName": "Hyd"
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
            },
            {
                "phone": "0915675675675",
                "phone2": "",
                "companyCode": code,
                "isActive": True,
                "customerDetails": {
                    "telephone": "",
                    "email": "a29@copmail.com",
                    "CSTNumber": 10,
                    "gstin": "19SDFGS2230T2R8",
                    "dlNumber": "15834",
                    "dlExpiry": "2024-03-21",
                    "distributorChannel": "",
                    "shippingAddress": {
                        "shippingAddress1": "Sector-9",
                        "shippingAddress2": "Bhilai"
                    },
                    "distributorCode": "90967",
                    "name": "aswin",
                    "companyName": "a57",
                    "physicalAddress": {
                        "address1": "pune",
                        "address2": "nanded"
                    },
                    "postalCode": "500094",
                    "stateCode": "36",
                    "countryCode": "IN",
                    "cityName": "Hyd"
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
        ],
        "companyCode": code,
        "workspaceId": main_workspace
    }
    url = f"{main_url}/mdm-integration/uploadbatch"
    res = postApi(url,payload)
    print(res.json())

    