#!/usr/bin/env python3
"""
script that calculates the time it takes for an async function to run
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Returns the time it takes for an async function to run
    """
    start = time.perf_counter()
    j = asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    await j
    end = time.perf_counter() - start
    return end
