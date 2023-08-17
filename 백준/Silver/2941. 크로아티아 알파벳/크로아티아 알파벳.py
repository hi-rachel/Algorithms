words = str(input())

c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

result = 0

for i in c_alpha:
  words = words.replace(i, '*')

print(len(words))