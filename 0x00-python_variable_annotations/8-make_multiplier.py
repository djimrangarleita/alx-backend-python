#!/usr/bin/env python3
"""Type annotated function to make multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Make a multiplier function

    Args:
        multiplier (float): A float to be mulitplied by callable's param

    Returns:
        Callable[[float], float]: Callable that multiplies two floats
    """
    def multiply(anotherParam: float) -> float:
        return anotherParam * multiplier
    return multiply
