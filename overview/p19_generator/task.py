import itertools


# assume there is a huge text file which can't be read into memory at once.
# 1. implement a function 'words' to iterate over file words.
# 2. now, using itertools implement another function 'filtered_words_until' that iterate
#    all words but to filtered ones and stops when reaching a specific word.
def words(filename):
    raise NotImplementedError("YOUR IMPLEMENTATION HERE")


for word in words("huge_file.txt"):
    print(word)
print("--------------------------------")


def filtered_words_until(filename, filter, until_word):
    raise NotImplementedError("YOUR IMPLEMENTATION HERE")


for word in filtered_words_until("huge_file.txt", ["of, the, is, was"], "software"):
    print(word)
