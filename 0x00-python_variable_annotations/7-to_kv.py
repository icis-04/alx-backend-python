#!/usr/bin/env python3
"""
List that prints Tuple of sy=ting and floats
"""
from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of string int/float
    """
    return (k, v ** 2)
