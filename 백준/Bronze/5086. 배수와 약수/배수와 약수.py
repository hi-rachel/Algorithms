while True:
  n, k  = map(int, input().split())
  if n == 0 & k == 0:
    break
  if k % n == 0:
    print("factor")
  elif n % k == 0:
    print("multiple")
  else:
    print("neither")