n = int(input())
words = []

for i in range(n):
    word = input()
    if word not in words:
        words.append(word)

words.sort(key=lambda x: (len(x), x))
for c in words:
    print(c)