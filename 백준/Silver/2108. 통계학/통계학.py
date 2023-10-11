import sys, math
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

avg = round(sum(arr) / len(arr))
median = arr[len(arr) // 2]

print(avg)
print(median)

cnt = Counter(arr).most_common()

if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

diff = max(arr) - min(arr)
print(diff)