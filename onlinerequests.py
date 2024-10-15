import requests
from pprint import pprint
from config import API_KYE

def convert_currency(from_currency, to_currency):
    url = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KYE}&currencies={from_currency}&base_currency={to_currency}'
    response = requests.get(url)
    data_info = response.json()
    currency = data_info.get('data', None)
    currency_value = currency.get(from_currency, None)
    print(f'Стоимость {to_currency} = {currency_value} {from_currency}')
    return currency_value


def get_all_currencies():
    all_currencies_url = f'https://api.freecurrencyapi.com/v1/currencies?apikey={API_KYE}&currencies='
    response = requests.get(all_currencies_url)
    all_currencies_data = response.json().get('data', None)
    return all_currencies_data

