from flask import json

from redis_client import redis_cache, redis_client
from read_csv import read_csv
from utils.get_latest import get_latest


@redis_cache('device_latest')
def device_latest(device_id: int):
    """
    try to fetch device information from redis.
    if not present, fetch from csv and save to
    redis

    :param device_id str: id of device to be checked
    """
    return get_latest(list(read_csv(device_id=device_id)))

