from features.orders.checkout import check_out
from Base_requets.Base_assertions import checking_the_status_code_201

check_out_res = check_out()
print(check_out_res.json())
def test_check_out():
    assert checking_the_status_code_201(check_out_res)