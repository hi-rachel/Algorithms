import sys
input = sys.stdin.readline

def recur(start, path):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return
    
    for i in range(N):
        recur(i+1, path + [numbers[i]])

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

recur(0, [])