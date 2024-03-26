


# from Settings.conftest import main_url
# from creation.get_principal_data_from_admin import principal_data
# from creation.get_token_from_superadmin import token
# from principal_login.get_workspace import main_token
# import requests

# # data = principal_data().json()["workspaceDetails"]


# def token_for_upload():
#     headers = {
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "clientSecret": data["clientSecret"],
#         "clientId": data["clientId"],
#         "workspaceId": main_token
#     }
#     url = f"{main_url}/mdm-integration/workspace-auth/login"
#     res = requests.post(url,json=payload, headers= headers)
#     print(res.json())

# token_for_upload()