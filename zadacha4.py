a = float(input('Введите сумму вклада\n'))
year_of_bank = int(input('Введите сколько лет сумма на вкладе\n'))
print('Сумма вклада = ', round(a*1.1**year_of_bank, 2))