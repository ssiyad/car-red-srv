from typing import Any, List
from copy import deepcopy


def sort_by_date(l: List[Any]):
    """
    sort a list of data points by `time_stamp`

    :param l List[Any]: list of data points
    """
    return sorted(deepcopy(l), key=lambda i: i.get('time_stamp').timestamp())

