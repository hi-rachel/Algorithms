a = int(input())
t = int(input())
game = int(input())

cnt = 0
person = 0
game_round = 0

while True:
  game_round += 1
  game_list = [0, 1, 0, 1]
  for i in range(1, game_round+2):
    game_list.append(0)
  for i in range(1, game_round+2):
    game_list.append(1)
  for i in range(len(game_list)):
    if game_list[i] == game:
      cnt += 1
    if cnt == t:
      print(person)
      exit(0)
    person += 1
    person %= a