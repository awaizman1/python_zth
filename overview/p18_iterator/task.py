# StudentGrade is a simple class holding a sequence of students and an associated
# sequence of grades.
# 1. make StudentGrade iterable. Iteration over StudentGrade should yield tuples of (STUDENT_NAME, STUDENT_GRADE).
# 2. make sure it can iterated multiple times.


class StudentGrade:
    def __init__(self, students, grades):
        self._students = students
        self._grades = grades

    raise NotImplementedError("YOUR IMPLEMENTATION HERE")


student_grades = StudentGrade(["Dave", "Shirley", "Lena", "Jhon"], [78, 95, 92, 56])
for student, grade in student_grades:
    print(student, ": ", grade)

# make sure we can iterate it again
for student, grade in student_grades:
    print(student, ": ", grade)
