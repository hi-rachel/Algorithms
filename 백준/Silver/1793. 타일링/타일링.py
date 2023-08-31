def dp(n):
  if n == 0 or n == 1:
    return 1
  elif n == 2:
    return 3
  d = [0] * (n + 1)
  d[1] = 1
  d[2] = 3
  for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2] * 2
  return d[n]
  
while True:
  try: n = int(input());
  except: break
    
  print(dp(n))