a = int(input('первое число\n'))
b = int(input('второе число\n'))
operation = input('Введите операцию (+,-,*,/)\n')
if operation == '+':
    print(operation)
    print(a+b)
elif operation == '-':
    print(operation)
    print(a-b)
elif operation == '*':
    print(operation)
    print(a*b)
elif operation == '/':
    print(operation)
    print(a/b)
else:
    print('Неизвестная операция')

