N = int(input())

answer = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        for c in range(1, N + 1):
            if a + b + c == N:
                if c >= b + 2:
                    if a != 0 and b != 0 and c != 0:
                        if a % 2 != 1:
                            answer += 1

print(answer)