from collections import deque

def bfs(x, y, visited, grid, L, R, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    union = [(x, y)]
    visited[x][y] = True
    population_sum = grid[x][y]

    while queue:
        _x, _y = queue.popleft()
        for dx, dy in directions:
            nx, ny = _x + dx, _y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(grid[_x][_y] - grid[nx][ny]) <= R:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    union.append((nx, ny))
                    population_sum += grid[nx][ny]

    if len(union) > 1:
        new_population = population_sum // len(union)
        for ux, uy in union:
            grid[ux][uy] = new_population
        return True
    return False

def population_movement(N, L, R, grid):
    days = 0
    while True:
        visited = [[False] * N for _ in range(N)]
        moved = False
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    if bfs(i, j, visited, grid, L, R, N):
                        moved = True
        if not moved:
            break
        days += 1
    return days

N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(population_movement(N, L, R, grid))