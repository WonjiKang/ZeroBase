# 3. 알파벳 문자열
n = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in n:
        print(n.index(i), end = ' ')
    else:
        print("-1", end= ' ')
