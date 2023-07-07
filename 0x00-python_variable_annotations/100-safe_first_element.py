#!/usr/bin/env python3
""" correct duck-typed annotations"""
from typing import Sequence, Any, Union

"""function def for safe first element"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if len(lst) > 0:
        """ return 1st"""
        return lst[0]
    """ return None"""
    else:
        return None
