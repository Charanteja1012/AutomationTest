from Settings.conftest import main_url
from user_login.get_workspace import main_workspace
from Settings.api_requests import postApi



def test_add_customer():
    url = f"{main_url}/customers/create/{main_workspace}"
    payload = {
        "senderWorkspaceId": main_workspace,
        "phone": "0911122334455",
        "customerDetails": {
            "name": "undefined",
            "companyName": "a",
            "telephone": "0911122334455",
            "email": "pankajg@pharmarack.com",
            "CSTNumber": "",
            "gstin": "abcd1234",
            "dlNumber": "12345",
            "dlExpiry": "2024-12-23",
            "distributorCode": "11111",
            "physicalAddress": {
                "address1": "Hyderabad",
                "address2": ""
            },
            "shippingAddress": {
                "shippingAddress1": "",
                "shippingAddress2": "",
                "city": "",
                "state": "",
                "countryCode": "IN",
                "pincode": ""
            },
            "postalCode": "411001",
            "stateCode": "27",
            "countryCode": "IN",
            "cityName": "pune",
            "grossCreditLimit": 0,
            "creditLimitPeriod": 0
        },
        "cfa": []
        }
    res = postApi(url, payload)
    print(res.json())
    print(res.status_code)
