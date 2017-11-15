

import random
from itertools import permutations
from more_itertools import unique_everseen, powerset
import textwrap


DICTPATH = 'dictionary.txt'


# load dictionary into memory
with open(DICTPATH) as f:
    DICT_WORDS = set(f.read().splitlines())


def word_in_dict(word):
    """
    Is given word (or tileset) in the dictionary?
    """
    if not isinstance(word, str):
        word = ''.join(word)
    return word in DICT_WORDS


def possible_words(letters):
    """
    Return list of all legal words made of the given letters.
    """
    wordset = set()
    # for all possible lengths of letters
    for chosen_letters in powerset(letters):
        if not chosen_letters:
            continue
        # test all permutations of letters of given length not before seen
        for tiles in unique_everseen(permutations(chosen_letters)):
            if word_in_dict(tiles):
                wordset.add(''.join(tiles))
    return sorted(wordset)


if __name__ == '__main__':
    print()
    letters = list('andytrd'.upper())
    random.shuffle(letters)
    print(f'letters: {letters}')
    words = possible_words(letters)
    print(f'{len(words)} words found:')
    print(textwrap.fill(' '.join(words),
                        initial_indent='    ',
                        subsequent_indent='    '))
