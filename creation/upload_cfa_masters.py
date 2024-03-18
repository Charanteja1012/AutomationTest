from Settings.conftest import main_url
from principal_login.request_apis import postApi
from principal_login.get_workspace import main_workspace,code


def test_create_cfa_master():
    payload = {
        "entity": "CFA_MASTER",
        "fileName": "Cfa_masters.csv",
        "records": [
            {
                "companyCode": code,
                "fulfillmentLocationCode": "4590",
                "isActive": True,
                "GSTNumber": "ASDFTY5634",
                "supplierName": "Kothaguda",
                "stateCode": "36",
                "cityName": "Hyd",
                "email": "testhyd44@yopmail.com",
                "fulfillmentAddress": "hyd",
                "businessPan": "TES56RESW",
                "postalCode": "500084",
                "country": "India",
                "phone": "0915646542345"
            },
            {
                "companyCode": code,
                "fulfillmentLocationCode": "0932",
                "isActive": True,
                "GSTNumber": "FCDERT453",
                "supplierName": "amerpeta",
                "stateCode": "36",
                "cityName": "Hyd",
                "email": "testhyd234@yopmail.com",
                "fulfillmentAddress": "hyd",
                "businessPan": "TSR43LKJH",
                "postalCode": "500084",
                "country": "India",
                "phone": "0918761123098"
            }
        ],
        "companyCode": code,
        "workspaceId": main_workspace
    }
    url = f"{main_url}/mdm-integration/uploadbatch"
    res = postApi(url,payload)
    print(res.json())