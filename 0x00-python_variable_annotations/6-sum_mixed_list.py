#!/usr/bin/env python3
"""
file that prints for multiple list types
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the list with integers and floats
    """
    return sum(mxd_lst)
