
# Remove 3 or more consecutive characters from a string, repeat until there are no more.
# example:
# ABCCCCBBD --> ABBBD --> AD
#
# hints:
# - help(str)
# - sequence protocol

def remove_dups(some_string):

    res = remove_dups_fwd(some_string)
    while len(res) != len(remove_dups_fwd(res)):
        res = remove_dups_fwd(res)

    return res


def remove_dups_fwd(some_string):

    if not some_string:
        return some_string

    curr_char_index = 1
    res = some_string[0]
    char_index_in_res = 0
    curr_char_count = 1

    while curr_char_index < len(some_string):  # iterate all some_string chars

        curr_char = some_string[curr_char_index]
        res += curr_char
        curr_char_index += 1

        if curr_char == res[char_index_in_res]:
            curr_char_count += 1
            if curr_char_count == 3:

                while curr_char_index < len(some_string) and some_string[curr_char_index] == curr_char:
                    curr_char_index += 1

                res = res.rstrip(curr_char)
                continue
        else:
            curr_char_count = 1
            char_index_in_res = len(res) - 1

    return res


print(remove_dups("ABCDEFGHIJK"))
print(remove_dups(""))
print(remove_dups("AABBCCCAB"))
print(remove_dups("ABCCCCBBD"))
print(remove_dups("ABBCCCCDDEEEEEEEDBCAA"))