t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1, num+1)]
    
    for k in range(floor):
        for n in range(1, num):
            f0[n] += f0[n-1]
    print(f0[-1])            