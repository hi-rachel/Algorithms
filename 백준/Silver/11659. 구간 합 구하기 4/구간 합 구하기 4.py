import sys
input = sys.stdin.readline

N, M = map(int, input().split())

N_list = list(map(int, input().split()))

new_list = [0] * (N)

for i in range(N):
    new_list[i] = new_list[i - 1] + N_list[i]

for k in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(new_list[j - 1])
    else:
        print(new_list[j - 1] - new_list[i - 2])