
# Write a function which checks if a password is valid.
# A valid password must follow:
# - At least 1 letter between [a-z] and 1 letter between [A-Z]
# - At least 1 number between [0-9]
# - At least 1 character from [$#@]
# Minimum length of 6 characters
# Maximum length of 16 characters

import string


def is_password_valid(password):

    if len(password) < 6 or len(password) > 16:
        return False

    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch in string.ascii_lowercase:
            has_lowercase = True
        elif ch in string.ascii_uppercase:
            has_uppercase = True
        elif ch in "$#@":
            has_special = True
        elif ch in string.digits:
            has_digit = True

        if has_lowercase and has_uppercase and has_special and has_digit:
            return True

    return False


p = input("Enter password:\n")
print(f"'{p}' is valid" if is_password_valid(p) else f"'{p}' is invalid")
