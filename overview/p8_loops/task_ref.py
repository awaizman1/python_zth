# given an odd number, print diamond with this diagonal.
#
# for example, for the number 5 the output would be:
#   *
#  ***
# *****
#  ***
#   *

# the program should keep doing so until the user enters 0


def print_diamond(diagonal):
    astrix = 1

    for row in range(diagonal):
        spaces = ' ' * ((diagonal - astrix) // 2)

        line = spaces + '*' * astrix + spaces

        print(line)

        astrix = (astrix + 2) if row < diagonal // 2 else (astrix - 2)


def read_diagonal_from_user():
    return int(input("Enter diagonal:\n"))


if __name__ == "__main__":

    while True:

        diag = read_diagonal_from_user()

        if diag == 0:
            break

        print_diamond(diag)