n, k = map(int, input().split())
cnt = 0

for h in range(n + 1):
  if h < 10:
    fh = '0'+str(h)
  else:
    fh = str(h)
  for m in range(60):
    if m < 10:
      fm = '0'+str(m)
    else:
      fm = str(m)
    for s in range(60):
      if s < 10:
        fs = '0'+str(s)
      else:
        fs = str(s)
      if str(k) in fh + fm + fs:
        cnt += 1

print(cnt)