"""
갑옷을 만드는 재료들은 각각 고유한 번호를 가지고 있음
갑옷은 두 개의 재료로 만드는데 두 재료의 고유한 번호를 합쳐 M이 되면 갑옷이 만들어지게 된다

N, M개의 재료를 가지고 갑옷을 몇 개나 만들 수 있는지 구하라
N = 재료의 개수
M = 갑옷을 만드는데 필요한 수
재료들이 가진 고유한 번호
"""

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

materials = list(map(int, input().split()))
materials.sort()

count = 0

start = 0
end = len(materials) - 1

while start < end:
    total = materials[start] + materials[end]
    if total == M:
        count += 1
        start += 1
        end -=  1
    elif total < M:
        start += 1
    else:
        end -= 1

print(count)