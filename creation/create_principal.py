from creation.get_token_from_superadmin import token
from Settings.conftest import main_url
import requests


def test_create_principal():
    headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "+f"{token}"
    }

    payload = {
  "firstName": "Automation Digital",
  "lastName": "",
  "mobile": "0911012101210",
  "email": "allpharma012@gmail.com",
  "workspaceDetails": {
    "companyName": "Automation Digital",
    "spaceName": "Digital",
    "companyEmail": "allpharma012@gmail",
    "code": "Automation",
    "isSeller": True,
    "gstin": "27DFRTY39003E4CC"
  }
}
    url = f"{main_url}/admin/principal/workspace"
    res = requests.post(url,json=payload,headers = headers)
    print(res.json())

    