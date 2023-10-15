import sys
input = sys.stdin.readline

n = int(input().rstrip())

reset = [0] * 10001

for i in range(n):
    num = int(input().rstrip())
    reset[num] += 1

for i in range(10001):
    if reset[i] > 0:
        for j in range(reset[i]):
            print(i)