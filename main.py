from onlinerequests import get_all_currencies, convert_currency


print('Добро пожаловать, уважаемый клиент!')
print('''
Наша программа поможет Вам конвертировать вашу валюту:
- Выберите валюту, которую хотите перевести.
- Вводите количество этой валюты.
- Выберите валюту для конвертации.
''')

#Вывод списка валют
ALL_CURRENCIES = get_all_currencies()
count = 1
for currency in ALL_CURRENCIES:
    print(f'{count} -> {currency}')
    count += 1

user_currency = input('Введите имеющуюся валюту: ')
current_amount = int(input('Введите имеющуюся сумму: '))
conversion_currency = input('Выберите валюту для конвертации: ')
result = convert_currency(from_currency=conversion_currency, to_currency=user_currency) * current_amount
print(f'Итого: {round(result, 2)}')