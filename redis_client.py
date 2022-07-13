import os

import redis
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

