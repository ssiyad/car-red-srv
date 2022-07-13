import os
from typing import Callable

import redis
from flask.json import dumps
from dotenv import load_dotenv


load_dotenv()


REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379)) 
REDIS_DB = int(os.environ.get('REDIS_DB', 0))
REDIS_USERNAME = os.environ.get('REDIS_USERNAME', 'default')
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '')


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    socket_timeout=5,
    retry_on_timeout=True,
    username=REDIS_USERNAME
)


def redis_cache(prefix: str):
    def ret_fn(fn: Callable):
        def inner(*args, **kwargs):
            q = '_'.join(str(v).replace(' ', '_') for v in kwargs.values())

            match len(args):
                case 0:
                    k = f"{prefix}_{q}"
                case _:
                    k = f"{prefix}_{args[0]}_{q}"

            r = redis_client.get(k)
            if r: return r

            r = fn(*args, **kwargs)
            if r: redis_client.set(k, dumps(r))

            return r

        return inner
    return ret_fn

