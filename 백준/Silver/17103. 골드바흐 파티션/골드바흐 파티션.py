t = int(input())
p = [True] * 1000001
p[0] = False
p[1] = False

for i in range(2, 1000001):
    if p[i]:
        for j in range(i+i, 1000001, i):
            p[j] = False
            
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(n//2+1):
        if p[i] and p[n-i]:
            cnt += 1
    print(cnt)