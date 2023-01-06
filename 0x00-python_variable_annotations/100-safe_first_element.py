#!/usr/bin/env python3
""" module for annotation work python"""
from typing import Union, Sequence, Tuple, Any, List


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Augment the following code with the correct duck-typed annotations:
    """
    if lst:
        return lst[0]
    else:
        return None
