#!/usr/bin/env python3
"""Async generator module
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine generator

    Yields:
        float: yield a random num between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yielded_number = random.uniform(0, 10)
        yield yielded_number
