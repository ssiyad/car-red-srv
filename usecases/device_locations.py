from datetime import datetime
from typing import Optional
from read_csv import read_csv
from utils.sort_by_date import sort_by_date
from redis_client import redis_cache


@redis_cache('device_locations')
def device_locations(
        device_id: int,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ):
    """
    return list of data points filtered by given criteria

    :param device_id int: id of device
    :param start_date Optional[datetime]: date after which entries start
    :param end_date Optional[datetime]: date before which entries end
    """
    data = sort_by_date(list(read_csv(device_id=device_id, start_date=start_date, end_date=end_date)))
    size = len(data)

    return {
        'data': data,
        'size': size,
    }

