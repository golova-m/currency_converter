from onlinerequests import get_all_currencies, convert_currency
from validation import validation_currencies, validation_amount

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

while not validation_currencies(user_currency := input('Введите имеющуюся валюту: '), ALL_CURRENCIES):
    print('Проверьте написание валюты. Введенной валюты нет в списке.')
while not validation_amount(current_amount := input('Введите имеющуюся сумму: ')):
    print('Введите положительное число.')
while not validation_currencies(conversion_currency := input('Выберите валюту для конвертации: '), ALL_CURRENCIES):
    print('Проверьте написание валюты. Введенной валюты нет в списке.')
result = convert_currency(from_currency=conversion_currency, to_currency=user_currency) * int(current_amount)
if type(result) == 'int':
    print(f'Итого: {round(result, 2)}')
else:
    print("Ошибка")