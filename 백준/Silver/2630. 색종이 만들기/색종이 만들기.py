import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def count_paper(paper):
    n = len(paper)
    white_cnt = 0
    blue_cnt = 0

    def divide_and_conquer(x, y, size):
        nonlocal white_cnt, blue_cnt
        current_color = paper[x][y]
        is_same_color = True

        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] != current_color:
                    is_same_color = False
                    break
            if not is_same_color:
                break
        
        if is_same_color:
            if current_color == 0:
                white_cnt += 1
            else:
                blue_cnt += 1
        else:
            half_size = size // 2
            divide_and_conquer(x, y, half_size)
            divide_and_conquer(x, y + half_size, half_size)
            divide_and_conquer(x + half_size, y, half_size)
            divide_and_conquer(x + half_size, y + half_size, half_size)

    divide_and_conquer(0, 0, n)
    return white_cnt, blue_cnt

white_cnt, blue_cnt = count_paper(paper)
print(white_cnt)
print(blue_cnt)