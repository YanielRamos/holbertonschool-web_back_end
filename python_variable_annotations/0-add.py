#!/usr/bin/python3
"""module that write a type-annotated function add that takes a float a
and a float b as arguments and returns their sum as a float"""

if __name__ == '__main__':
    def add(a: float, b: float) -> float:
        """function that sum two floatsa nd return a float"""
        return a + b
