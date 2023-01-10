#!/usr/bin/env python3
"""
Script to print out the random wait floats in a list
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    asynchronous function that returns list of floats of awaited time of the 
    wait_random function.
    """
    i: int = 0
    res: List[float] = []
    while i < n:
        j = await wait_random(max_delay)
        res.append(j)
        i += 1
    for i in range(len(res)):
        for j in range(i + 1, len(res)):

            if res[i] > res[j]:
               res[i], res[j] = res[j], res[i]
    return res
