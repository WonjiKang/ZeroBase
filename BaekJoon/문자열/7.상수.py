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
