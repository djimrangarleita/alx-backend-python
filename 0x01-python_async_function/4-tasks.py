#!/usr/bin/env python3
"""Module used for multiple coroutines
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run a coroutine n times

    Args:
        n (int): Number of time wait_random should be called
        max_delay (int): Maximum duration of wait time

    Returns:
        List[float]: List of all wait times
    """
    result = list()
    futures = [task_wait_random(max_delay) for _ in range(n)]
    for future in asyncio.as_completed(futures):
        result.append(await future)
    return result
