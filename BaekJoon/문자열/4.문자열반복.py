n = int(input())
for i in range(n):
    number, object = input().split()
    number = int(number)
    object = str(object)
    for j in object:
        print(number * j, end='')