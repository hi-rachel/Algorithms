import sys
input = sys.stdin.readline

n = int(input())

square_map = []

for i in range(n):
    square_map.append(list(map(int, input().rstrip())))

cnt = 0
result = 0

def dfs(x, y):
    global result
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    
    if square_map[x][y] == 1:
        square_map[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        result += 1
        return True 
    return False

house_list = []

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt += 1
            house_list.append(result)
            result = 0

house_list.sort()

print(cnt)
for i in range(len(house_list)):
    print(house_list[i])