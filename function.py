def print_three_words():
    print("1")
    print("2")
    print("3")
def print_word(slovo):
    print(slovo*2)
def search_in_str(stroka, searcher_object):
    print(stroka.lower().count(searcher_object.lower()))
def max(x,y):
    if x >= y:
        return x
    else:
        return y
oper = print_three_words
oper()
max_number = max(max(10,20),40)
print(max_number)
print_three_words()
print_word('компьютер')
stroka_word = input("Введите строку\n")
search = input("введите искомую букву\n")
search_in_str(stroka_word, search)
