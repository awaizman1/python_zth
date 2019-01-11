# StudentGrade is a simple class holding a sequence of students and an associated
# sequence of grades.
# 1. make StudentGrade iterable.
# 2. make sure it can iterated multiple times.


class StudentGrade:
    def __init__(self, students, grades):
        self._students = students
        self._grades = grades

    def __iter__(self):
        class StudentGradeIterator:
            def __init__(self, student_grade):
                self._student_grade = student_grade
                self._index = 0

            def __iter__(self):
                return self

            def __next__(self):
                if self._index >= len(self._student_grade._students):
                    raise StopIteration

                ret = self._student_grade._students[self._index], \
                      self._student_grade._grades[self._index]

                self._index += 1

                return ret

        return StudentGradeIterator(self)


student_grades = StudentGrade(["Dave", "Shirley", "Lena", "Jhon"], [78, 95, 92, 56])
for student, grade in student_grades:
    print(student, ": ", grade)

# make sure we can iterate it again
for student, grade in student_grades:
    print(student, ": ", grade)
