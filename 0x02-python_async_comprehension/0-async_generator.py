#!/usr/bin/env python3
"""
Script that runs an iterable async function
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Returns a randon float every 1 seconds
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
