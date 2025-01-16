import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lessons = list(map(int, input().split()))

def is_possible(max_size):
    count, current_sum = 1, 0
    for lesson in lessons:
        if current_sum + lesson > max_size:
            count += 1
            current_sum = lesson
        else:
            current_sum += lesson
    return count <= M

left, right = max(lessons), sum(lessons)
result = right

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)