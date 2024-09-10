#!/usr/bin/env python3
"""Wait task executions
"""
import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[float]:
    """Get and return a coroutine task

    Args:
        max_delay (int): Maximum waiting time

    Returns:
        Awaitable[float]: Coroutine task
    """
    return asyncio.Task(wait_random(max_delay))
