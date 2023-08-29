n = int(input())

k = [0] + [int(input()) for _ in range(n)] + [0]

d = [0] * (n+2)

d[1] = k[1]
d[2] = d[1] + k[2]

for i in range(3, n+1):
  d[i] = max(d[i - 3] + k[i - 1] + k[i], d[i - 2] + k[i])
  d[i] = max(d[i - 1], d[i])

print(d[n])