import sys
from collections import deque
input = sys.stdin.readline

queuestack = deque()

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

for i in range(N):
    if A[i] == 0:
        queuestack.appendleft(B[i])
    else:
        if queuestack == []:
            print(*C)
            sys.exit()

for i in range(M):
    queuestack.append(C[i])
    print(queuestack.popleft(), end=' ')