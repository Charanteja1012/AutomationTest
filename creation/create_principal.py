from creation.get_token_from_superadmin import token
from Settings.conftest import main_url
import requests


def test_create_principal():
    headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer "+f"{token}"
      }

    payload = {
      "firstName": "Automation Testing",
      "lastName": "",
      "mobile": "0919090909090",
      "email": "allpharma900@gmail.com",
      "workspaceDetails": {
        "companyName": "Automation Testing",
        "spaceName": "Testing",
        "companyEmail": "allpharma900@gmail.com",
        "code": "Testing",
        "isSeller": True,
        "gstin": "27AZXCH98765E4ZZ"
      }
    }
    url = f"{main_url}/admin/principal/workspace"
    res = requests.post(url,json=payload,headers = headers)
    print(res.json())

    