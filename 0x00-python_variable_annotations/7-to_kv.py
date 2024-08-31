#!/usr/bin/env python3
"""Convert params to a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert params to a tuple

    Args:
        k (str): String type param
        v (Union[int, float]): Float or int type param

    Returns:
        Tuple[str, float]: Return a tuple (k, v)
    """
    return (k, v**2)
