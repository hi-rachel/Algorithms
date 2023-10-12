from itertools import product

n, k = map(int, input().split())
k_arr = list(input().split())
len_max = len(str(n))

while True:
    tmp = list(product(k_arr, repeat=len_max))
    result = []
    for i in tmp:
        guess = int("".join(i))
        if guess <= n:
            result.append(guess)
    if len(result) >= 1:
        print(max(result))
        break
    else:
        len_max -= 1