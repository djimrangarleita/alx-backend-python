#!/usr/bin/env python3
"""Measure the runtime of the coroutines
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute the coroutines in parallel and measure their runtime

    Returns:
        float: Execution time
    """
    s = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - s
