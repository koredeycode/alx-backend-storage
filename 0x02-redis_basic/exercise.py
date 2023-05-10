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


def call_history(method: Callable) -> Callable:
    """
    the call decorator
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        the invoke function
        """
        in_key = "{}:inputs".format(method.__qualname__)
        out_key = "{}:outputs".format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        ret = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, ret)
        return ret
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
    @call_history
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
