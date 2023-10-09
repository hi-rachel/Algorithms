import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for num in m_list:
    if binary_search(n_list, num, 0, n - 1):
        print(1)
    else:
        print(0)