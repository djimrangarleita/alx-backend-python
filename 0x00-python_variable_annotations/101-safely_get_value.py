#!/usr/bin/env python3
"""Safely get value
"""
from typing import Mapping, Union, Any, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Use variable types

    Args:
        dct (Mapping): Dictionary
        key (Any): Any type key va
        default (Union[T, None], optional): Optional param. Defaults to None.

    Returns:
        Union[Any, T]: Return type any or T
    """
    if key in dct:
        return dct[key]
    else:
        return default
