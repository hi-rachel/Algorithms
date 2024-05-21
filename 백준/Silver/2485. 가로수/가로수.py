import sys
from math import gcd
input = sys.stdin.readline

N = int(input())

compare_tree = int(input())

arr = []

for _ in range(N-1):
    tree = int(input())
    arr.append(tree - compare_tree)
    compare_tree = tree
    
g = arr[0]
for i in range(len(arr)):
    g = gcd(g, arr[i])
    
result = 0
for x in arr:
    result += x // g - 1
print(result)