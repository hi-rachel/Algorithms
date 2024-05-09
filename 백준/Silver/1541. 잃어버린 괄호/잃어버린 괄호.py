import sys
input = sys.stdin.readline

calc_list = input().rstrip().split('-')
minus_calc_list = []

for calc in calc_list:
    plus_calc_list = list(map(int, calc.split('+')))
    minus_calc_list.append(sum(plus_calc_list))

answer = minus_calc_list[0]

for i in range(1, len(minus_calc_list)):
    answer -= minus_calc_list[i]

print(answer)