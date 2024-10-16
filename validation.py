def validation_response(response):
    if response.status_code  == 200:
        return response
    return False


def validation_currencies(input_currency, all_currencies):
    if input_currency in all_currencies:
        return True
    return False


def validation_amount(input_amount):
    if input_amount.isdigit() and int(input_amount) > 0:
        return True
    return False