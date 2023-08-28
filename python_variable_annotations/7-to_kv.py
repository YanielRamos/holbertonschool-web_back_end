#!/usr/bin/env python3
"""Script that returns a tuple[str, float]"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function that return the tuple"""
    return tuple([k, v * v])
