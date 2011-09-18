def diffs_of_lists(a, b):
    """Returns the diffs of two lists:

    >>> diffs_of_lists([1, 3, 2], [3, 4])
    ([1, 2], [4])
    """
    not_in_b = filter(lambda x: x not in b, a)
    not_in_a = filter(lambda x: x not in a, b)
    return (not_in_b, not_in_a)

def split_with_condition(iter, condition):
    """Splits the iterable to two.

    First list contains all those elements which match the condition.
    Second list contains the ones that dont. Returns a tuble containing
    matches and misses.

    >>> split_with_condition([1, 2, 3, 1, 4, 9], lambda x: x == 1)
    ([1, 1], [2, 3, 4, 9])
    """
    matches, misses = [], []
    for i in iter:
        if condition(i):
            matches.append(i)
        else:
            misses.append(i)
    return matches, misses


import re

emailregex = "[a-zA-Z0-9\._\-+=]+@[a-zA-Z0-9\._\-]+\.[a-zA-Z]+"

def is_valid_email(s):
    r"""Checks if s is a valid email address.

    >>> is_valid_email("foo")
    False
    >>> is_valid_email("foo@foo")
    True
    
    Whitespace, newlines and so forth are not allowed.

    >>> is_valid_email(" foo@foo.com")
    False
    >>> is_valid_email("foo@foo.com ")
    False
    >>> is_valid_email("foo@foo.com\n")
    False
    >>> is_valid_email("foo @bar.com")
    False
    """
    return re.match(emailregex + "\Z", s) != None
