import sys
input = sys.stdin.readline

N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

left, right = 0, N - 1
best_sum = float('inf')
result = (0, 0) 

while left < right:
    current_sum = solutions[left] + solutions[right]

    if abs(current_sum) < abs(best_sum):
        best_sum = current_sum
        result = (solutions[left], solutions[right])

    if current_sum < 0:
        left += 1
    elif current_sum > 0:
        right -= 1
    else:
        break

print(result[0], result[1])