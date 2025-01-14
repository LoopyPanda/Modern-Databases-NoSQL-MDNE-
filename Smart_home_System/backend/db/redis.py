import redis
import os

def get_redis_client():
    return redis.StrictRedis(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT")),
        decode_responses=True
    )
