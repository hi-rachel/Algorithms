from collections import deque

queue = deque()
josephus = []

n, k = map(int, input().split())

for i in range(1, n + 1):
    queue.append(i)

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
    josephus.append(queue.popleft())

print("<", end="")
print(", ".join(map(str, josephus)), end="")
print(">")