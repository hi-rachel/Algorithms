n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
new_score_list = []
for x in score:
  new_score = x / max_score * 100
  new_score_list.append(new_score)
print(sum(new_score_list) / n)