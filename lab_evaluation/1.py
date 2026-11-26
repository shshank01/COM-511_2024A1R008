
n, f = map(int, input().split())

attendance = {}

for i in range(n):
    student, day = input().split()

    if student not in attendance:
        attendance[student] = set()

    attendance[student].add(day)

feedback = set()

for i in range(f):
    student = input()
    feedback.add(student)

eligible = []
missing = []

for student in attendance:

    if len(attendance[student]) >= 2:

        if student in feedback:
            eligible.append(student)
        else:
            missing.append(student)

eligible.sort()
missing.sort()
print("OUTPUT:")
print(" ".join(eligible) if eligible else "NONE")
print(" ".join(missing) if missing else "NONE")
