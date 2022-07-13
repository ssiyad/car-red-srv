from typing import Any, List
from copy import deepcopy

from .to_timestamp import to_timestamp


def sort_by_date(l: List[Any]):
    """
    sort a list of data points by date

    :param l List[Any]: list of data points
    """
    _l = deepcopy(l)
    _l.sort(key=to_timestamp)
    return _l

