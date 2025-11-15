def count_row(board, n, row):
    """특정 행에서 최대 연속 길이를 반환"""
    max_count = 1
    count = 1
    for j in range(1, n):
        if board[row][j] == board[row][j-1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    return max(max_count, count)


def count_col(board, n, col):
    """특정 열에서 최대 연속 길이를 반환"""
    max_count = 1
    count = 1
    for i in range(1, n):
        if board[i][col] == board[i-1][col]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    return max(max_count, count)


def solve():
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    
    # 초기 최댓값 계산
    max_result = 1
    for i in range(n):
        max_result = max(max_result, count_row(board, n, i))
    for j in range(n):
        max_result = max(max_result, count_col(board, n, j))
    
    # 가로 방향 교환 (i행의 j열과 j+1열 교환)
    for i in range(n):
        for j in range(n - 1):
            # 교환
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            
            # 영향받는 행(i)과 열(j, j+1)만 확인
            max_result = max(max_result, count_row(board, n, i))
            max_result = max(max_result, count_col(board, n, j))
            max_result = max(max_result, count_col(board, n, j+1))
            
            # 원복
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
    
    # 세로 방향 교환 (i행과 i+1행의 j열 교환)
    for i in range(n - 1):
        for j in range(n):
            # 교환
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            
            # 영향받는 행(i, i+1)과 열(j)만 확인
            max_result = max(max_result, count_row(board, n, i))
            max_result = max(max_result, count_row(board, n, i+1))
            max_result = max(max_result, count_col(board, n, j))
            
            # 원복
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
    
    print(max_result)
    
if __name__ == "__main__":
    solve()