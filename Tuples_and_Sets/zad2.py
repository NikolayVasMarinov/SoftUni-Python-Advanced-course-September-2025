number_of_students: int = int(input())

students: dict[str, tuple[float]] = {}
for student in range(number_of_students):
    student_information: tuple = tuple(input().split(" "))

    student_name: str = student_information[0]
    grade: float = float(student_information[1])

    if student_name not in students:
        students[student_name] = tuple()

    students[student_name] += (grade, )

for student in students:
    average_grade: float = sum(x for x in students[student]) / len(students[student])
    print(f"{student} -> {' '.join('{:.2f}'.format(x) for x in students[student])} (avg: {average_grade:.2f})")