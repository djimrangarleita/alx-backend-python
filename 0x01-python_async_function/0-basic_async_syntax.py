#!/usr/bin/env python3
"""Manipulation of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Coroutine that returns a random number

    Args:
        max_delay (int, optional): Maximum wait time. Defaults to 10.

    Returns:
        float: Return the duration of the pause
    """
    pause_for: float = random.uniform(0, max_delay)
    await asyncio.sleep(pause_for)
    return pause_for
