from itertools import combinations

N = int(input())
num_list = list(map(int, input().split()))

sum_set = set()

for i in range(1, N+1):
    for comb in combinations(num_list, i):
        sum_set.add(sum(comb))

smallest_missing = 1
while smallest_missing in sum_set:
    smallest_missing += 1

print(smallest_missing)