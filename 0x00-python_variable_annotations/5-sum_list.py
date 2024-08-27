#!/usr/bin/env python3
"""Module for float addition
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum a list of float numbers

    Args:
        input_list (list[float]): List of floats passed as argument

    Returns:
        float: The sum of all numbers in list
    """
    return sum(input_list)
