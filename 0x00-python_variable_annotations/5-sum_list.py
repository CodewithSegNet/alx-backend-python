#!/usr/bin/python3
"""A function that takes a list of floats and return their sum"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of list"""
    sum_float = 0.0
    for lists in input_list:
        sum_float += lists
    return sum_float
