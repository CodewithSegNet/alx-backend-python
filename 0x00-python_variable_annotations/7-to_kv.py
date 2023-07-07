#!/usr/bin/env python3
"""A function that takes str and int or float as arg/
return tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple of str and int or float"""
    return k, v ** 2
