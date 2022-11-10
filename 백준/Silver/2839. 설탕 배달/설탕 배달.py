kgram = int(input())
min_bag = 0

while kgram >= 0:
  if kgram % 5 == 0:
    min_bag += int(kgram // 5)
    print(min_bag)
    break

  else:
    kgram -= 3
    min_bag += 1

else:
  print(-1)