import string

n, b = map(int, input().split())

def convert(num, base):
  number = string.digits + string.ascii_uppercase
  q, r = divmod(num, base)
  return convert(q, base) + number[r] if q else number[r]

print(convert(n, b))