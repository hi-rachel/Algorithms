import sys

input = sys.stdin.readline

N, M = map(int, input().split())
memo = {}
for i in range(N):
    site, password = input().split()
    memo[site] = password

for i in range(M):
    print(memo[input().rstrip()])