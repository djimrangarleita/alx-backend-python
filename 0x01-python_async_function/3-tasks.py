#!/usr/bin/env python3
"""Wait task executions
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[float]:
    """Get and return a coroutine task

    Args:
        max_delay (int): Maximum waiting time

    Returns:
        Callable: Coroutine task
    """
    return asyncio.Task(wait_random(max_delay))
