from typing import Any, List
from datetime import datetime

from flask import json

from redis_client import redis_client
from read_csv import read_csv


def device_latest(device_id: str):
    """
    try to fetch device information from redis.
    if not present, fetch from csv and save to
    redis

    :param device_id str: id of device to be checked
    """
    res = redis_client.get(device_id)

    if (res): return res

    raw = read_csv(device_id=device_id)
    res = get_latest(list(raw))

    if not res: return 

    redis_client.set(device_id, json.dumps(res))
    redis_client.expire(device_id, 1800)
    return res


def to_timestamp(d: Any):
    """
    convert iso string to timestamp and return unix timestamp (seconds)

    :param d Any: iso string
    """
    return datetime.strptime(d.get('time_stamp'), "%Y-%m-%dT%H:%M:%S%z").timestamp()


def get_latest(l: List[Any]):
    """
    get latest item from a list of data points

    :param list List[Any]: list of data points
    """
    if len(l) < 1: return 

    l.sort(key=to_timestamp)
    return l.pop(0)

