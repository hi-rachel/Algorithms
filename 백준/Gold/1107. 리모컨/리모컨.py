import sys
input = sys.stdin.readline

current_channel = 100

N = int(input())

if (N == current_channel):
    print(0)
    sys.exit()

M = int(input())

if M > 0:
    broken_btn_list = list(map(int, input().split()))
else:
    broken_btn_list = []

btn_list = [str(i) for i in range(10) if i not in broken_btn_list]

def can_move(channel):
    for ch in str(channel):
        if ch not in btn_list:
            return False
    return True

min_press = abs(N - current_channel)

for i in range(1000000):
    if can_move(i):
        min_press = min(min_press, len(str(i)) + abs(i - N))

print(min_press)