test_case = int(input())

for case in range(test_case):
  case_list = list(input())
  count = 0
  sum_count = 0
  for case in case_list:
    if case == "O":
      count += 1
      sum_count += count
    else:
      count = 0
  print(sum_count)