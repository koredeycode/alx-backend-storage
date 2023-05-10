#!/usr/bin/env python3
"""
Module documentation
"""

from functools import wraps
import redis
from typing import Union, Callable, Any
import uuid


def count_calls(method: Callable) -> Callable:
    """
    the count decorator
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        do something cool
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    The cache class
    """
    def __init__(self):
        """
        The initializing instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generate an random kee and store input data in redis
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        the get methon that take a key string argument
        return the converted data
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """
        return a string value from redis
        """
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        return an integer from redis data
        """
        return self.get(key, int)
