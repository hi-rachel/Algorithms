import sys
input = sys.stdin.readline

N = int(input().rstrip())

answer = 0
hint = [list(map(int, input().split())) for _ in range(N)]

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or c == a:
                continue
            cnt = 0
            
            for arr in hint:
                num, strike, ball = arr
                num_test = list(str(num))

                num1 = num // 100
                num2 = num % 100 // 10
                num3 = num % 10

                ball_cnt = 0
                strike_cnt = 0

                if a == num1:
                    strike_cnt += 1
                elif a == num2 or a == num3:
                    ball_cnt += 1

                if b == num2:
                    strike_cnt += 1
                elif b == num1 or b == num3:
                    ball_cnt += 1

                if c == num3:
                    strike_cnt += 1
                elif c == num1 or c == num2:
                    ball_cnt += 1

                if ball == ball_cnt and strike == strike_cnt:
                    cnt += 1
            if cnt == N:
                answer += 1

print(answer)