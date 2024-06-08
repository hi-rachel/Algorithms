import sys
input = sys.stdin.readline

N = int(input())
max_weight_list = []

for _ in range(N):
    max_weight_list.append(int(input()))

max_weight_list.sort()

max_weight = 0
rope_cnt = N

for i in range(N):
    if max_weight_list[i] * rope_cnt > max_weight:
        max_weight = max_weight_list[i] * rope_cnt
    rope_cnt -= 1
    
print(max_weight)