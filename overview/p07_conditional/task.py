
# Write a function which checks if a password is valid.
# A valid password must follow:
# - At least 1 letter between [a-z] and 1 letter between [A-Z]
# - At least 1 number between [0-9]
# - At least 1 character from [$#@]
# Minimum length of 6 characters
# Maximum length of 16 characters

import string


def is_password_valid(password):

    # hints:
    # - https://docs.python.org/3/reference/compound_stmts.html
    # - you can iterate chars in string using for-loop:
    #   for c in "hello world"...
    # - use string.ascii_lowercase, etc. and the 'membership test operation':
    #   x in s evaluates to True if x is a member of s, and False otherwise

    raise NotImplementedError("YOUR IMPLEMENTATION HERE")


p = input("Enter password:\n")
print(f"'{p}' is valid" if is_password_valid(p) else f"'{p}' is invalid")
