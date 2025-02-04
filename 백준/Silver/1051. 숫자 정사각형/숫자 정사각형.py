import sys
input = sys.stdin.readline

def find_largest_square(n, m, square):
    max_size = 1

    for i in range(n):
        for j in range(m):
            for k in range(min(n - i, m - j)):
                if square[i][j] == square[i][j + k] == square[i + k][j] == square[i + k][j + k]:
                    max_size = max(k+1, max_size)

    return max_size**2


N, M = map(int, input().split())
square = [list(input().strip()) for _ in range(N)]

print(find_largest_square(N, M, square))