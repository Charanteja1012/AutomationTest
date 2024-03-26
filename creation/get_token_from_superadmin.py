from Settings.conftest import main_url
from user_login.single_login import send_otp,verify_otp

token = ""
mobile_number = "9999999987"

send_otp_response = send_otp(main_url, mobile_number)
main_token = verify_otp(send_otp_response.json(),main_url,mobile_number)
token = main_token.json()["token"]



