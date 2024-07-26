from itertools import combinations

N, S = map(int, input().split())
n_list = list(map(int, input().split()))

cnt = 0

for i in range(1, N+1):
    for j in list(combinations(n_list, i)):
        if sum(list(j)) == S:
            cnt += 1

print(cnt)