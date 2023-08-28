#!/usr/bin/env python3
"""script that have the elements of a function"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Get the first element of a sequence safely"""
    if lst:
        return lst[0]
    else:
        return None
