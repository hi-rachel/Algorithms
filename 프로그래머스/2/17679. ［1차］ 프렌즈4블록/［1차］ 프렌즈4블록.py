def solution(m, n, board):
    grid = [list(row) for row in board]
    removed_total = 0
    
    while True:
        to_remove = set()
    
        for i in range(m - 1):
            for j in range(n - 1):
                a = grid[i][j]
                if a is None:
                    continue
                if (
                    grid[i][j + 1] == a and
                    grid[i + 1][j] == a and
                    grid[i + 1][j + 1] == a
                ):
                    to_remove.update({
                        (i, j), (i, j + 1),
                        (i + 1, j), (i + 1, j + 1)
                    })
                    
        if not to_remove:
            break

        removed_total += len(to_remove)
        for (i, j) in to_remove:
            grid[i][j] = None

        for j in range(n):
            stack = [grid[i][j] for i in range(m) if grid[i][j] is not None]
            for i in range(m - 1, -1, -1):
                grid[i][j] = stack.pop() if stack else None

    return removed_total