n = int(input())
work = {}

for _ in range(n):
    name, log = map(str, input().split())
    work[name] = log

sorted_work = dict(sorted(work.items(), key=lambda x: x[0], reverse=True))

for name in sorted_work:
    if sorted_work[name] == "enter":
        print(name)