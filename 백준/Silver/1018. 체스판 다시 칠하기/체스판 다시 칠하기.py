n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(input())
    
for i in range(n-7):
    for j in range(m-7):
        paint1 = 0
        paint2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != "B":
                        paint1 += 1
                    if board[a][b] != "W":
                        paint2 += 1
                else:
                    if board[a][b] != "W":
                        paint1 += 1
                    if board[a][b] != "B":
                        paint2 += 1
        result.append(paint1)
        result.append(paint2)
print(min(result))