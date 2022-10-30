A, B = map(int, input().split())
C = int(input())
if B + C < 60:
  print(A, B + C)
elif B + C >= 60:
  D = (B + C) // 60
  E = (B + C) % 60
  if A + D >= 24:
    print(A + D -24, E)
  else:
    print(A + D, E)