import sys
input = sys.stdin.readline

N = int(input())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()

answer = 0

for i in range(N):
    answer += A_list[-1] * min(B_list)

    A_list.pop()
    B_list.remove(min(B_list))

print(answer)