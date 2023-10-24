def solution(n, lost, reserve):
    students = [i for i in range(1, n + 1)]

    students = list(set(students) - set(lost))

    for cloth in reserve:
        if cloth not in students:
            students.append(cloth)

    reserve = list(set(reserve) - set(lost))

    for cloth in reserve:
        if (cloth - 1) >= 1 and (cloth - 1) not in students:
            students.append(cloth - 1)
        elif (cloth + 1) <= n and (cloth + 1) not in students:
            students.append(cloth + 1)

    return len(students)