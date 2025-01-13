import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    diary_1 = list(map(int, input().split()))
    M = int(input())
    diary_2 = list(map(int, input().split()))

    diary_1_dict = dict(zip(diary_1, diary_1))

    for i in range(M):
        if diary_2[i] in diary_1_dict:
            print(1)
        else:
            print(0)