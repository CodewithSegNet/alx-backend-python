#!/usr/bin/env python3
"""A function that takes float as arg and /
returns a function that multiplies float by/
multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """def function for float multiplication"""
    def multiply(num: float) -> float:
        """return multiply float"""
        return num * multiplier
    return multiply
