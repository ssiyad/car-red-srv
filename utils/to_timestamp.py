from typing import Any
from datetime import datetime


def to_timestamp(d: Any):
    """
    convert iso string to timestamp and return unix timestamp (seconds)

    :param d Any: iso string
    """
    return datetime.strptime(d.get('time_stamp'), "%Y-%m-%dT%H:%M:%S%z").timestamp()

