# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

x: int = 5
y = 3
z = 1
print(x+y+z)
print('x'+'y'+'z')
print(x, y, z)
x = 2.001*5
print(round(x, 3))
x = 2 ** 2 ** 3
print(x)
x = -12 % -5
print(x)
# z = int(input())
# i = 5
# print(z + i)
# print(int(input("Введите число")))
print('В сто \"сорок\n солнц\" закат\t пылал')
print("""Отправляя эту форму, я разрешаю JetBrains использовать мой электронный адрес 
для отправки мне учебных материалов и коммерческих предложений об используемом мной продукте, 
а также обрабатывать мои персональные данные с указанной целью. Я соглашаюсь с тем, что такая обработка может 
выполняться с использованием сторонних сервисов в соответствии с Политикой конфиденциальности JetBrains. 
Я могу в любой момент отозвать согласие в своем профиле. Кроме того, ссылка для отмены подписки 
содержится в каждом электронном письме""")
print('спам\n '*3)
x = 5
x += 2
print(type(x))
print(x)

age = int(input("введите возраст"))
if age > 60:
    print("пенсионер")
elif age > 18:
    print("совершеннолетний")
else:
    print("юноша")

