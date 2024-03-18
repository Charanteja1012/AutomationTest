from Settings.conftest import main_url,mobile_number
from user_login.single_login import send_otp,verify_otp,get_workspace
from user_login.mfa_login import verify_mobile_otp,verify_email_otp,get_workspacess

main_workspace = []
main_token = ""
code = ""
send_otp_response = send_otp(main_url, mobile_number)

# print(send_otp_response.json())
# print(send_otp_response)
# print(1)


if send_otp_response.json()["mfaStatus"]:
    # print(otp_res)
    verify_mobile_res = verify_mobile_otp(send_otp_response.json(),mobile_number, main_url)
    # print(verify_mobile_res.json())
    # print(verify_mobile_res)
    verify_email_res = verify_email_otp(send_otp_response.json(), verify_mobile_res.json(), main_url)
    # print(verify_email_res.json())
    main_token = verify_email_res.json()["token"]
    get_workspaces = get_workspacess(verify_email_res.json(), main_url)
    # print(get_workspaces.json())
    for i in get_workspaces.json():
        for j in i["principal"]:
            each_principal = {"pId": j["principalWorkspaceId"], "cId": j["inviteId"],"cwId": j["clientWorkspaceId"]}
            main_workspace.append(each_principal)
    code = get_workspaces.json()[0]["code"]
else:
    token = verify_otp(send_otp_response.json(),main_url,mobile_number)
    main_token = token.json()["token"]
    workspace = get_workspace(token.json()["token"],main_url)
    # print(workspace.json())
    for i in workspace.json():
        for j in i["principal"]:
            each_principal = {"pId": j["principalWorkspaceId"], "cId": j["inviteId"],"cwId": j["clientWorkspaceId"]}
            main_workspace.append(each_principal)
    code = workspace.json()[0]["code"]

# print(main_workspace)
# print(main_token)


