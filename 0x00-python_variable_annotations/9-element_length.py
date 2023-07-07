#!/usr/bin/env python3
"""Annotate function’s parameters and return values with the appropriate types"""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    result = []
    for seq in lst:
        length = len(seq)
        result.append((seq, length))
    return result
