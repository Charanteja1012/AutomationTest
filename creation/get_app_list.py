from principal_login.get_workspace import main_workspace
from Settings.conftest import main_url
from principal_login.request_apis import getApi


def get_app_list():
    url = f"{main_url}/app/list/{main_workspace}"
    res = getApi(url)
    return res