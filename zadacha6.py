y = int(input('Введите год'))
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    print('Високосный год')
else:
    print('Обычный год')