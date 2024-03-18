from features.products.get_products import get_products
from Base_requets.Base_assertions import checking_the_status_code_201

products_res = get_products()
print(products_res.json())

def test_get_products():
    assert checking_the_status_code_201(products_res)
    
    

