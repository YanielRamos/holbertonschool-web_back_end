#!/usr/bin/env python3
"""script that sum a list of floats and int"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """function that sums all int and float of the list"""
    result = float(sum(mxd_list))
    return result
