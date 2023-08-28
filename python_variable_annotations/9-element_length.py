#!/usr/bin/env python3
"""script that that return a the type of
everything in the function"""
from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function that return a lsit with a tuple"""
    return [(i, len(i)) for i in lst]
