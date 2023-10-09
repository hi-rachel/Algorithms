n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if array[mid] == target:
        return cnt.get(target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


cnt = {}
for i in n_list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for num in m_list:
    print(binary_search(n_list, num, 0, n - 1))