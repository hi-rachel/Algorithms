import sys
input = sys.stdin.readline

def dfs(depth, nums):
    global min_ans, max_ans

    if depth == k + 1:
        if not min_ans or nums < min_ans:
            min_ans = nums
        if not max_ans or nums > max_ans:
            max_ans = nums
        return

    for i in range(10): # 0 ~ 9
        if not visited[i]:
            if depth == 0 or signs[depth-1] == "<" and nums[-1] < str(i) or signs[depth-1] == ">" and nums[-1] > str(i):
                visited[i] = True
                dfs(depth + 1, nums + str(i))
                visited[i] = False

k = int(input())
signs = input().split()

visited = [False] * 10
min_ans, max_ans = "", ""

dfs(0, "")

print(max_ans)
print(min_ans)