# find the list in a list of lists whose sum of elements is the highest
# hint:
# - https://docs.python.org/3/library/functions.html#max
# - https://docs.python.org/3/library/functions.html#sum

def find_max_list(list_of_lists):
    [--> your implementation here <--]


print(find_max_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]))


# flatten list of lists using comprehension
def flatten_list(list_of_lists):
    [--> your implementation here <--]


print(flatten_list([[1, 2], [3, 4], [5, 6]]))


# convert a flat list of students grades into a list of tuples where each tuple is (student, grade)
def normalize_grades(grades):
    [--> your implementation here <--]


print(normalize_grades(["Max", 76, "Tal", 96, "Jhon", 100, "Bob", 88]))


# given a matrix, calculate a sum_matrix where sum_matrix[row_index, col_index] = sum of the row and col in matrix
# for example:
# [[1, 2],
#  [3, 4]]
#
# will return:
# [[7, 9],
#  [11, 13]]


def calc_matrix(input_matrix):
    [--> your implementation here <--]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(calc_matrix(matrix))
