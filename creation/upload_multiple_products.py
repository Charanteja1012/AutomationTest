from creation.create_cfa import create_cfa
from creation.create_division import create_division
from principal_login.get_workspace import main_workspace,code
from Settings.conftest import main_url
from principal_login.request_apis import postApi

cfa_res = create_cfa().json()
division_res = create_division().json()

def test_multiple_products_upload():
    payload = {
        "entity": "PRODUCT_MASTER",
        "fileName": "products.csv",
        "records": [
            {
                "name": "Chacolate",
                "parentSku": "098765",
                "description": "blend ",
                "productVariants": [
                    {
                        "name": "Chacolate",
                        "sku": "098765",
                        "listPrice": 250.50,
                        "shortName": "Dairy milk",
                        "shortDescription": "We blend",
                        "facets": [
                            {
                                "name": "Sweet",
                                "facetCode": "CH",
                                "facetValues": [
                                    {
                                        "facetValue": "Netcafe",
                                        "facetValueCode": "Net"
                                    }
                                ]
                            }
                        ],
                        "sortOrder": 0,
                        "taxCategoryCode": "GST-12",
                        "enabled": True,
                        "ean": "abc",
                        "erpId": "234",
                        "erpUOM": "CHA",
                        "vairantCode": "Var111",
                        "upcCode": "4321",
                        "hsnCode": "9876",
                        "baseUom": "PCK",
                        "packSize": 2,
                        "minOrderQty": 1,
                        "maxOrderQty": 20,
                        "qtyMultiplier": 1,
                        "grossWeight": 50,
                        "netWeight": 45,
                        "weightUOM": "KG",
                        "volume": 60,
                        "volumeUOM": "L",
                        "erpPriceUOM": "DZ",
                        "warrentyInformation": "No warranty",
                        "condition": "condition information",
                        "MRP": 250,
                        "PTR": 200,
                        "caseSize": 12,
                        "isSpecial": True,
                        "packingInfo": "1*10",
                        "ZINS": True,
                        "mfgName": "NETCAFE",
                        "mfgCode": "NET11"
                    }
                ],
                "customFields": {},
                "divisionCFACodes": [
                    {
                        "cfaCode": cfa_res["cfa"]["code"],
                        "divisionCode": division_res["division"]["code"],
                        "isActive": True
                    }
                ]
            },
            {
                "name": "chicken masala",
                "parentSku": "45678",
                "description": "blend ",
                "productVariants": [
                    {
                        "name": "chicken masla",
                        "sku": "45678",
                        "listPrice": 300,
                        "shortName": "masala",
                        "shortDescription": "We blend",
                        "facets": [
                            {
                                "name": "Masala",
                                "facetCode": "CM",
                                "facetValues": [
                                    {
                                        "facetValue": "Netcafe",
                                        "facetValueCode": "Nct"
                                    }
                                ]
                            }
                        ],
                        "sortOrder": 0,
                        "taxCategoryCode": "GST-12",
                        "enabled": True,
                        "ean": "abc",
                        "erpId": "54",
                        "erpUOM": "PCK",
                        "vairantCode": "Var111",
                        "upcCode": "4321",
                        "hsnCode": "9876",
                        "baseUom": "PCK",
                        "packSize": 2,
                        "minOrderQty": 1,
                        "maxOrderQty": 20,
                        "qtyMultiplier": 1,
                        "grossWeight": 50,
                        "netWeight": 45,
                        "weightUOM": "KG",
                        "volume": 60,
                        "volumeUOM": "L",
                        "erpPriceUOM": "CM",
                        "warrentyInformation": "No warranty",
                        "condition": "condition information",
                        "MRP": 300,
                        "PTR": 250,
                        "caseSize": 12,
                        "isSpecial": True,
                        "packingInfo": "1*11",
                        "ZINS": True,
                        "mfgName": "NETCAFE",
                        "mfgCode": "NET11"
                    }
                ],
                "customFields": {},
                "divisionCFACodes": [
                        {
                            "cfaCode": cfa_res["cfa"]["code"],
                            "divisionCode": division_res["division"]["code"],
                            "isActive": True
                        }
                ]
            }
        ],
        "companyCode": code,
        "workspaceId": main_workspace
    }
    url = f"{main_url}/mdm-integration/uploadbatch"
    res = postApi(url, payload)
    print(res.json())

