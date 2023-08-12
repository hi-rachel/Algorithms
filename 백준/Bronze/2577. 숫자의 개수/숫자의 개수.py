n = 1
for _ in range(3):
  n *= int(input())

n = str(n)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
cnt = []
for num in numbers:
  cnt.append(n.count(num))

for i in cnt:
  print(int(i))