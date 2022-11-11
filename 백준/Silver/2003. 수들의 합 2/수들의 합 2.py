n, m = map(int, input().split())
a_list = list(map(int, input().split()))

left, right = 0, 1
cnt = 0

while right <= n and left <= right:
  sum_sub_list = a_list[left:right]
  sum_list = sum(sum_sub_list)

  if sum_list == m:
    cnt += 1
    right += 1

  elif sum_list < m:
    right += 1
    
  else:
    left += 1
  
print(cnt)