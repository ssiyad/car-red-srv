from read_csv import read_csv
from utils.sort_by_date import sort_by_date
from redis_client import redis_cache 


@redis_cache('device_movement')
def device_movement(device_id: int):
    l = sort_by_date(list(read_csv(device_id=device_id)))

    match len(l):
        case 0:
            return
        case 1:
            start = end = l.pop()
        case _:
            start = l.pop(0)
            end = l.pop()

    return {
        'start': {
            'time_stamp': start.get('time_stamp'),
            'sts': start.get('sts'),
            'location': f"({start.get('latitude')}, {start.get('longitude')})"
        },
        'end': {
            'time_stamp': end.get('time_stamp'),
            'sts': end.get('sts'),
            'location': f"({end.get('latitude')}, {end.get('longitude')})"
        },
    }

