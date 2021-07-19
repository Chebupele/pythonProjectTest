text = input('Введите предложение\n')
bykva = input('Введите искомую букву\n')
print("Количество встретившихся букв=", text.lower().count(bykva.lower()))
list_word = text.split()
for word in list_word:
    print(word, "-", word.lower().count(bykva.lower()))

