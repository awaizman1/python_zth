
# Remove 3 or more consecutive characters from a string, repeat until there are no more.
# example:
# ABCCCCBBD --> ABBBD --> AD
#
# hints:
# - help(str)
# - sequence protocol


def remove_dups(some_string, dups=3):
    
    n = dups - 1
    i = 0
    while i < len(some_string) - n:
        # keep fwd until different char
        j = i + 1
        while j < len(some_string) and some_string[i] == some_string[j]:
            j += 1
        
        # remove duplication
        if j - i > n:
            some_string = some_string[:i] + some_string[j:]
            i -= n
        else:
            i = j
    
    return some_string


print(remove_dups("ABCDEFGHIJK"))
print(remove_dups(""))
print(remove_dups("AABBCCCAB"))
print(remove_dups("ABCCCCBBD"))
print(remove_dups("ABBCCCCDDEEEEEEEDBCAA"))
