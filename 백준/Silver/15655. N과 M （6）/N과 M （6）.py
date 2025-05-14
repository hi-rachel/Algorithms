def recur(start, path):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return

    for i in range(start, N):
        recur(i + 1, path + [arr[i]])
        # recur(depth + 1, output+str(i)+" ")

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

recur(0, [])
