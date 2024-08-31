#!/usr/bin/env python3
"""Fix typing with mypy
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Type annotated function

    Args:
        lst (Tuple): Param of type Tuple
        factor (int, optional): Optional int. Defaults to 2.

    Returns:
        Tuple: _description_
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


tupleArg = (12, 72, 91)

zoom_2x = zoom_array(tupleArg)

zoom_3x = zoom_array(tupleArg, 3)
