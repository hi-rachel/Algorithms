import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    max_day = 0
    profit = 0
    for day in reversed(days):
        if day > max_day:
            max_day = day
        else:
            profit += max_day - day
    print(profit)