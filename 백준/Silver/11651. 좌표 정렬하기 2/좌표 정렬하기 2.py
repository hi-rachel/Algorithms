n = int(input())

arr = []

for _ in range(n):
    dot = list(map(int, input().split()))
    arr.append(dot)

arr.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(*arr[i])