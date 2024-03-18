from Settings.conftest import main_url
from principal_login.request_apis import postApi
from principal_login.get_workspace import main_workspace


def create_cfa():
    url = f"{main_url}/fulfillment-locations/{main_workspace}"
    payload = {
        "workspaceId": main_workspace,
        "fulfillmentLocationCode": "24012",
        "supplierName": "user",
        "isActive": True,
        "stateId": "24b724f9-0579-4c40-b84a-5f75639ca1dc",
        "cityId": "018fe890-e3c2-4cce-a74b-2a5d7780a1a7",
        "email": "nava_az4@yop.com",
        "fulfillmentAddress": "amerpeta hyd",
        "GSTNumber": "FTVRYDE352",
        "businessPan": "TTYYR2YPP47",
        "postalCode": "500061",
        "country": "India",
        "phone": "091111122222"
    }
    res = postApi(url,payload)
    # print(res.json())
    return res

# create_cfa()