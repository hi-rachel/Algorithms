import sys
input = sys.stdin.readline

n = int(input())
reservation = []

for i in range(n):
    room = list(map(int, input().split()))
    reservation.append(room)

reservation.sort(key=lambda x: (x[1], x[0]))
current = -1
available = 0

for reserv in reservation:
    s, e = reserv
    if s < current:
        continue
    current = e
    available += 1

print(available)