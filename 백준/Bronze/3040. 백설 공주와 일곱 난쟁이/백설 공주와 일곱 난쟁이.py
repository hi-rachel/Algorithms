small = []
for i in range(9):
    small.append(int(input()))
for i in range(9):
    for j in range(i+1, 9):
        if sum(small)-small[i]-small[j] == 100:
            x,y=i,j
            break
small.pop(x)
small.pop(y-1)
for c in small:
    print(c)