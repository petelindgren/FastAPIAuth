# https://fastapi-users.github.io/fastapi-users/10.0/configuration/authentication/strategies/redis/
import aioredis
from src.settings import REDIS_URL

redis = aioredis.from_url(REDIS_URL, decode_responses=True)
