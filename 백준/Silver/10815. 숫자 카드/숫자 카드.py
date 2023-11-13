import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

_dict = {}

for n in n_list:
    _dict[n] = 0

for x in m_list:
    if x in _dict:
        print(1, end=' ')
    else:
        print(0, end=' ')