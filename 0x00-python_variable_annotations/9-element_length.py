#!/usr/bin/env python3
"""Type annotate a function
"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Get the length of an iterable containing sequences

    Args:
        lst (Iterable[Sequence]): Iterable with sequences

    Returns:
        List[Tuple[Sequence, int]]: List of tuples with a squence and its len
    """
    return [(i, len(i)) for i in lst]
