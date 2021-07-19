months = [['Зима', '1', '2', '12', ], ['Весна', '3', '4', '5', ], ['Лето', '6', '7', '8', ],
         ['Осень', '9', '10', '11', ], ]
m = input('Введите месяц\n')
result = 'Неверный введённый месяц'
for month in months:
    if m in month:
        result = month[0]
        break
print(result)

