#!/usr/bin/env python3
"""
Scripts returns list of floats from the async_generator module using
asyn list comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns a list of floats gotten from the async_generator module
    """
    result: List[float] = [i async for i in async_generator()]
    return result 
