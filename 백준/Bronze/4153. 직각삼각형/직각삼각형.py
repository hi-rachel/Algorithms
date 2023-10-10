import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break
    max_num = max(arr)
    arr.remove(max_num)
    if max_num**2 == arr[0] ** 2 + arr[1] ** 2:
        print("right")
    else:
        print("wrong")