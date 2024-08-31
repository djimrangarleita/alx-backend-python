#!/usr/bin/env python3
"""Duck-typing module
"""
from typing import Any, Union, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safe first element, type annotated

    Args:
        lst (Sequence[Any]): Argument of any type

    Returns:
        Union[Any, None]: _description_
    """
    if lst:
        return lst[0]
    else:
        return None