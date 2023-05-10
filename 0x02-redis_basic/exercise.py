#!/usr/bin/env python3
"""
Module documentation
"""

import redis
import typing
import uuid


class Cache:
    """
    The cache class
    """
    def __init__(self):
        """
        The initializing instance
        """
        self._redis = redis.Redis()

    def store(self, data: typing.Any) -> str:
        """
        generate an random kee and store input data in redis
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key