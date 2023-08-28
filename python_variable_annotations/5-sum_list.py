#!/usr/bin/env python3
"""script that have function with a list of float as argument"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function that sum all float in the list"""
    result = sum(input_list)

    return result
