#!/usr/bin/env python3

def return_evens(num_list):
    """Return a list of even integers from num_list."""
    return [num for num in num_list if num % 2 == 0]


def make_exclamation(sentence_list):
    """Return a list of sentences with exclamation marks at the end."""
    return [sentence + "!" for sentence in sentence_list]
