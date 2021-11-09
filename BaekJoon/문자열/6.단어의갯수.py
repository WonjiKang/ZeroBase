# 6. 단어의 개수
s = input("")
words = s.split(" ")
words = [w for w in words if w != ""]
print(len(words))