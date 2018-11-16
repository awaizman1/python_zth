# given a dict 'd', return a new dict with all duplicated values removed. keep the smallest key of duplications.
# for example, for the dict {1: 'a', 2: 'a', 3: 'b'} return {1: 'a', 3: 'b'}
from pprint import pprint


def remove_duplicates(d):
    reversed_dict = {}
    for key, value in d.items():
        if value not in reversed_dict or reversed_dict[value] > key:
            reversed_dict[value] = key

    return {value: key for key, value in reversed_dict.items()}


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
    with open(file, 'r') as f:
        text = f.read()

        # Cleaning text and lower casing all words
        for char in '-.,\n':
            text = text.replace(char, ' ')
        text = text.lower()

        words = text.split()

        ret = {}
        for word in words:
            ret[word] = ret.get(word, 0) + 1

        return ret


pprint(word_count('input.txt'))
