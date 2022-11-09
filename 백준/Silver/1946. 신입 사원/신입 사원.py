import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
  applicants_n = int(input())
  ranking = [list(map(int, input().split())) for _ in range(applicants_n)]
  ranking_sort = sorted(ranking)
  top = 0
  hire = 1

  for x in range(1, len(ranking_sort)):
    if ranking_sort[x][1] < ranking_sort[top][1]:
      top = x
      hire += 1
  print(hire)