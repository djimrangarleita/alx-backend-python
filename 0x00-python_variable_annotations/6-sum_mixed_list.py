#!/usr/bin/env python3
"""Annotated function with mixed type
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Make the sum of an array of integers and floats

    Args:
        mxd_lst (List[Union[int, float]]): Function param, numbers to sum up

    Returns:
        float: The sum of the array of numbers
    """
    return sum(mxd_lst)
