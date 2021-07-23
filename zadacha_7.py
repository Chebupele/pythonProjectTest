srtroka = input('Введите предложение\n')
itog = ''
for s in srtroka:
    if s == 'о':
        itog += "а"
    else:
        itog += s
print(itog)

