c = int(input())

for test in range(c):
  score_list = list(map(int, input().split()))
  mean = sum(score_list[1:]) / score_list[0]
  count = 0
  for score in score_list[1:]:
    if score > mean:
      count += 1
    true = count / score_list[0] * 100
  print(f'{true:.3f}%')