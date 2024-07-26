from itertools import combinations

while True:
    input_list = list(map(int, input().split()))
    if input_list == [0]:
        break
    
    k = input_list[0]
    n_list = input_list[1:]
    combi = list(combinations(n_list, 6))
    for i in combi:
        print(*i)
    print()