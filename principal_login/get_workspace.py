
from Settings.conftest import main_url, principal_mobile_num
from user_login.single_login import send_otp,verify_otp,get_workspace
from user_login.mfa_login import verify_mobile_otp,verify_email_otp,get_workspacess

mobile_number = principal_mobile_num
main_workspace = ""
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
    main_workspace = get_workspaces.json()[0]["id"]
    code = get_workspaces.json()[0]["code"]
else:
    token = verify_otp(send_otp_response.json(),main_url,mobile_number)
    main_token = token.json()["token"]
    workspace = get_workspace(token.json()["token"],main_url)
    # print(workspace.json())
    main_workspace = workspace.json()[0]["id"]
    code = workspace.json()[0]["code"]

# print(main_workspace)
# print(main_token)
# print(code)