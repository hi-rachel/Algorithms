n = int(input())

members = []

for i in range(n):
    member = input().split()
    members.append(member)

result = sorted(members, key=lambda x: int(x[0]))

for m in result:
    print(" ".join(m))
