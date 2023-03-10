#!/usr/bin/env python3
"""
script that calculates the time it takes for an async function to run
"""
from typing import List
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the time it takes for an async function to run
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - start
    return end / n
