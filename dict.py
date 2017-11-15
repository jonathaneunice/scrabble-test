

import random
import string
from itertools import permutations
from more_itertools import unique_everseen, powerset


from show.pretty import *

DICTPATH = 'dictionary.txt'


with open(DICTPATH) as f:
    words = f.read().splitlines()
words = set(words)


def word_in_dict(word):
    return word in words


def tiles_in_dict(tiles):
    word = ''.join(tiles).upper()
    value =  word in words
    return value


def possible_words(tiles):
    wordset = set()
    pset = list(powerset(tiles))
    for tileoption in pset:
        if not tileoption:
            continue
        for perm in list(permutations(tileoption)):
            if not unique_everseen(perm):
                continue
            is_word = tiles_in_dict(perm)
            if is_word:
                wordset.add(perm)

    return sorted(wordset)


if __name__ == '__main__':
    tiles = list('andytrd')
    print(f'words in tiles: {tiles}')
    for w in possible_words(tiles):
        print(''.join(w))
