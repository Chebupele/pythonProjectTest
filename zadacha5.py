y = int(input('Введите номер месяца'))
if 12 < y or y <= 0:
    print('Такого месяца нет')
elif 3 <= y <= 5:
    print('Весна')
elif 6 <= y <= 8:
    print('Лето')
elif 9 <= y <= 11:
    print('Осень')
else:
    print('Зима')