#!/usr/bin/env python3
"""Documentation for the module
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async comprehension

    Returns:
        List[float]: List comprehension of the yielded numbers
    """
    return [i async for i in async_generator()]
