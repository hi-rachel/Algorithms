import sys
input = sys.stdin.readline

N = int(input())
p_arr = list(map(int, input().split()))
sorted_p_arr = sorted(p_arr)

time = 0
acc = 0

for num in sorted_p_arr:
    acc += num
    time += acc

print(time)