n, m = map(int, input().split())

woods = []
need = 0

for _ in range(n):
    woods.append(list(input()))

for i in range(n):
    a = ""
    for j in range(m):
        if woods[i][j] != a and woods[i][j] == "-":
            need += 1
        a = woods[i][j]

for j in range(m):
    a = ""
    for i in range(n):
        if woods[i][j] != a and woods[i][j] == "|":
            need += 1
        a = woods[i][j]

print(need)