import itertools


# assume there is a huge text file which can't be read into memory at once.
# 1. implement a function 'words' to iterate over file words.
# 2. now, using itertools implement another function 'filtered_words_until' that iterate
#    all words but to filtered ones and stops when reaching a specific word.
def words(filename):

    with open(filename, 'r') as f:
        for line in f:
            line_words = line.split()
            for word in line_words:
                yield word


for word in words("huge_file.txt"):
    print(word)
print("--------------------------------")


def filtered_words_until(filename, filter, until_word):
    return itertools.takewhile(lambda word: word != until_word,
                               itertools.filterfalse(lambda word: word in filter,
                                                     words(filename)))


for word in filtered_words_until("huge_file.txt", ["of", "the", "is", "was"], "software"):
    print(word)
