n, k = map(int, input().split())
students = sorted(list(map(int, input().split())), reverse=True)

print(students[k - 1])