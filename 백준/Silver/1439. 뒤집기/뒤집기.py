s = input()
one = s.split('0')
zero = s.split('1')
one_len = 0
zero_len = 0

for i in one:
  if i != '':
    one_len += 1
for i in zero:
  if i != '':
    zero_len += 1
    
print(zero_len) if zero_len < one_len else print(one_len)