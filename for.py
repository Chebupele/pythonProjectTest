x = 4
i = 1
while i <= 6:
    i+=1
    if x+i == 8:
        continue
    print(x+i)

while True:
    print(x:=x**2)
    if x > 10000:
        break

words = ['мыла', 'мама', 'раму', 'мама',]
for word in words:
    print(word.count('м'))