#!/usr/bin/env python3
"""Compute average exec time
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure execution time of the wait_n corountines

    Args:
        n (int): Number of coroutines to spawn
        max_delay (int): Maximum exec delay of coroutines

    Returns:
        float: Average execution time
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed / n
