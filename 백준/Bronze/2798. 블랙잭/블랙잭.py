n, m = map(int, input().split())
num_list = list(map(int, input().split()))
sum = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if num_list[i] + num_list[j] + num_list[k] > m:
                continue
            else:
                sum = max(sum, num_list[i] + num_list[j] + num_list[k])
print(sum)