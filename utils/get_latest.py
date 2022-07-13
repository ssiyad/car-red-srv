from typing import Any, List
from copy import deepcopy

from .sort_by_date import sort_by_date


def get_latest(l: List[Any]):
    """
    get latest item from a list of data points

    :param list List[Any]: list of data points
    """
    _l = sort_by_date(deepcopy(l))

    if len(_l) < 1: return

    return _l.pop(0)

