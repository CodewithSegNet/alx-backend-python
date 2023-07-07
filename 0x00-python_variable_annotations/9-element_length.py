#!/usr/bin/env python3
"""Annotate function’s parameters and /
return values with the appropriate types"""
from typing import Iterable, Sequence, List, Tuple

"""function’s parameters and return values with the appropriate types"""
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    result = []
    """loop seq in 1st"""
    for seq in lst:
        """store seq in a variable length"""
        length = len(seq)
        """ append seq"""
        result.append((seq, length))
        """return seq"""
    return result
