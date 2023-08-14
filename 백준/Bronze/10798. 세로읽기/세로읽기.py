save = []
length = 0
result = ""

for _ in range(5):
    letters = str(input())
    save.append(letters)
    if length < len(letters):
      length = len(letters)

for i in range(length):
  for j in range(5):
    try:
      result += save[j][i]
    except IndexError:
      result += ''

print(result)