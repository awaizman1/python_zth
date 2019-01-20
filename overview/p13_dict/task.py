# given a dict 'd', return a new dict with all duplicated values removed. keep the smallest key of duplications.
# for example, for the dict {1: 'a', 2: 'a', 3: 'b'} return {1: 'a', 3: 'b'}
from pprint import pprint


def remove_duplicates(d):
    raise NotImplementedError("YOUR IMPLEMENTATION HERE")


pprint(remove_duplicates({'one': 1,
                          'two': 2,
                          'three': 3,
                          'first': 1,
                          'second': 2,
                          'third': 3,
                          'ONE': 1,
                          'TWO': 2,
                          'THREE': 3}))


# given a text file - 'file', load it and return its words count (in dict form)
# make sure to handle special characters and ignore words case
def word_count(file):
    raise NotImplementedError("YOUR IMPLEMENTATION HERE")


pprint(word_count('input.txt'))
