#!/usr/bin/env python3
"""Function that takes in a list of floats/ints and returns float sum"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """function takes in list of floats and integers"""

    sum_int_float = 0.0
    for lists in mxd_lst:
        sum_int_float += lists

    return sum_int_float
