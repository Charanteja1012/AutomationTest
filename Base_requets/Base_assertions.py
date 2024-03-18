def checking_the_status_code_201(response):
    if response.status_code == 201:
        return True

def checking_the_status_code_200(response):
    if response.status_code == 200:
        return True

def checking_the_status_code_422(response):
    if response.status_code == 422:
        return True    