import sys
input = sys.stdin.readline

n, k = map(int, input().split()) 
a = list(map(int, input().split()))

def bubble_sort(a):
    cnt = 0
    for i in range(n-1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                cnt += 1
                
                if cnt == k:
                    print(a[j], a[j + 1])
                    return
    print(-1)
    
bubble_sort(a)