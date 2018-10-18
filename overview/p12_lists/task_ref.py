# find the list in a list of lists whose sum of elements is the highest
# hint:
# - https://docs.python.org/3/library/functions.html#max
# - https://docs.python.org/3/library/functions.html#sum

def find_max_list(list_of_lists):
    return max(list_of_lists, key=sum)


print(find_max_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]))


# flatten list of lists using comprehension
def flatten_list(list_of_lists):
    return [item for l in list_of_lists for item in l]


print(flatten_list([[1, 2], [3, 4], [5, 6]]))


# convert a flat list of students grades into a list of tuples where each tuple is (student, grade)
def normalize_grades(grades):
    return [(name, grade) for name, grade in zip(grades[::2], grades[1::2])]


print(normalize_grades(["Max", 76, "Tal", 96, "Jhon", 100, "Bob", 88]))


# given a matrix, calculate a sum_matrix where sum_matrix[row_index, col_index] = sum of the row and col in matrix
# for example:
# [[1, 2],
#  [3, 4]]
#
# will return:
# [[7, 9],
#  [11, 13]]

def sum_of_index(row, col):
    row_sum = sum(matrix[row])
    col_sum = sum([row[col] for row in matrix])

    return row_sum + col_sum


def calc_matrix(input_matrix):
    return [[sum_of_index(row, col) for col in range(len(input_matrix[0]))] for row in range(len(input_matrix))]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(calc_matrix(matrix))
