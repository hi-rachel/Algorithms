n = int(input())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = list(str(factorial(n)))

def count_zero(arr):
    cnt = 0
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] == "0":
            cnt += 1
        else:
            break
    return cnt

print(count_zero(result))