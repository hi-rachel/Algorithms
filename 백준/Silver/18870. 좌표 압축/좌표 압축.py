import sys
input = sys.stdin.readline

n = int(input())
X_cor = list(map(int, input().split()))
sorted_unique_X = sorted(set(X_cor))

sorted_dict_X = {value: idx for idx, value in enumerate(sorted_unique_X)}

for x in X_cor:
    print(sorted_dict_X[x], end=' ')