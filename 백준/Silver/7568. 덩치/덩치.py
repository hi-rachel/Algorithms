n = int(input())

persons = []
rank = []

for _ in range(n):
    person = list(map(int, input().split()))
    persons.append(person)

for i in range(n):
    now = persons[i]
    cnt = 1
    for j in range(n):
        if i == j:
            continue
        next = persons[j]
        if now[0] < persons[j][0] and now[1] < persons[j][1]:
            cnt += 1
        else:
            j += 1
    rank.append(cnt)
    
print(*rank)