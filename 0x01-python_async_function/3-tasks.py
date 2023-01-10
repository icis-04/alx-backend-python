#!/usr/bin/env python3
"""
script that returns the async task of a function
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    converts function to a task
    """
    return asyncio.create_task(wait_random(max_delay))
