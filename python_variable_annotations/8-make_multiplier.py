#!/usr/bin/env python3
"""script that hat takes a float multiplier as argument and
returns a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create and return a function that multiplies
    a float by the given multiplier"""
    def multiplier_function(d: float) -> float:
        return d * multiplier

    return multiplier_function
