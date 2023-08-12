play = list(map(int, input().split()))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]

if play == ascending:
  print('ascending')
elif play == ascending[::-1]:
  print('descending')
else:
  print('mixed')