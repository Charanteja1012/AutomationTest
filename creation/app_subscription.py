from principal_login.get_workspace import main_workspace
from Settings.conftest import main_url
from principal_login.request_apis import postApi
from creation.get_app_list import get_app_list

apps_data = get_app_list().json()

def app_subscription():
    payload = {
        "workspaceId": main_workspace,
        "appId": apps_data[4]["appId"]
    }
    url = f"{main_url}/apps/subscribe/{main_workspace}"
    res = postApi(url,payload)
    print(res.json())

app_subscription()