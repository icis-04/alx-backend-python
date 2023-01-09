#!/usr/bin/python3 env
"""
scripts that waits for a particular amount of seconds then returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns the time it took the function to run.
    """
    i : float = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
