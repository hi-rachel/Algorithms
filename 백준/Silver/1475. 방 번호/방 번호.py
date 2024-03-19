import sys
input = sys.stdin.readline

room_num = map(int, str(input().rstrip()))

og_set_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
set_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
set_num = 1

for need in room_num:
    if need not in set_list:
        if need == 6:
            if 9 not in set_list:
                set_list += og_set_list
                set_num += 1
                set_list.remove(6)
            else:
                set_list.remove(9)
        elif need == 9:
            if 6 not in set_list:
                set_list += og_set_list
                set_num += 1
                set_list.remove(9)
            else:
                set_list.remove(6)
        else:
            set_list += og_set_list
            set_num += 1
            set_list.remove(need)
        continue
    set_list.remove(need)

print(set_num)