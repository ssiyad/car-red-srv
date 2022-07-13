from flask import json

from redis_client import redis_client
from read_csv import read_csv
from utils.get_latest import get_latest


def device_latest(device_id: int):
    """
    try to fetch device information from redis.
    if not present, fetch from csv and save to
    redis

    :param device_id str: id of device to be checked
    """
    res = redis_client.get(str(device_id))

    if (res): return res

    raw = read_csv(device_id=device_id)
    res = get_latest(list(raw))

    if not res: return 

    redis_client.set(str(device_id), json.dumps(res))
    redis_client.expire(str(device_id), 1800)
    return res

