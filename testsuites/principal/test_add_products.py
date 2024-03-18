from principal_login.principal_products.add_products import add_products_in_principal
from Base_requets.Base_assertions import checking_the_status_code_422

res = add_products_in_principal()


def test_add_products_fields():
    assert checking_the_status_code_422(res)
    print(res.json()["message"])