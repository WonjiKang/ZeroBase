# 백준 문제
# 백준 문제
# 1. 아스키코드

n = input()
n = ord(n)
print(n)

# 2. 숫자의합
n = input()
number = input()
array = []
for i in number:
    array.append(int(i))

print(sum(array))

# 3. 알파벳 문자열
n = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in n:
        print(n.index(i), end = ' ')
    else:
        print("-1", end= ' ')

# 4. 문자열 반복

n = int(input())
for i in range(n):
    number, object = input().split()
    number = int(number)
    object = str(object)
    for j in object:
        print(number * j, end='')
# ## 답이 계속 틀린다.

# 5. 단어 공부

# 6. 단어의 개수
s = input("")
words = s.split(" ")
words = [w for w in words if w != ""]
print(len(words))

# 7. 상수
n, s = input().split()

n = ''.join(reversed(n))
s = ''.join(reversed(s))
s = int(s)
n = int(n)
if n > s:
    print(n)
else:
    print(s)
