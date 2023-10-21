from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
else:
    opinions = deque()
    for _ in range(n):
        opinions.append(int(input()))

    if n <= 3:
        print(round(sum(opinions) / len(opinions) + 0.00000001))

    else:
        del_num = round(n * 0.15 + 0.00000001)

        opinions_sort = deque(sorted(opinions))

        while True:
            opinions_sort.popleft()
            opinions_sort.pop()
            del_num -= 1
            if del_num == 0:
                break

        avg = round(sum(opinions_sort) / len(opinions_sort) + 0.00000001)
        print(avg)