words = ['мыла', 'мама', 'раму', 'мама',]
list_object = [1, 2, 'c', 'строка', [1, 2, 3], ['я', 'ю', 'у']]
print(words[2])
print(list_object[4][2])
print(len(words))
print(len(list_object))
print(words.index('мама'))
words.append("papa")
words.insert(1, 'окно')
print(words.count('мама'))
a = 'окно'
print(a.count('о'))
print(a[1])
print('papa' in words)
print(words*6)
