#!/usr/bin/env python3
"""
script designed to wait for a task
"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    asynchronous function that returns list of floats of awaited time of the 
    task_wait_random function.
    """
    i: int = 0
    res: List[float] = []
    while i < n:
        j = await task_wait_random(max_delay)
        res.append(j)
        i += 1
    for i in range(len(res)):
        for j in range(i + 1, len(res)):

            if res[i] > res[j]:
               res[i], res[j] = res[j], res[i]
    return res
