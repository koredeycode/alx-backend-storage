#!/usr/bin/env python3
"""
Module documentation
"""

from functools import wraps
import requests
import redis
from typing import Callable

r = redis.Redis()


def cache_url(fn: Callable) -> Callable:
    """cache a url to 10 seconds"""
    @wraps(method)
    def wrapper(url) -> str:
        """the invoking function"""
        r.incr("count:{}".format(url))
        res = r.get("result:{}".format(url))
        if res:
            return result.decode('utf-8')
        res = method(url)
        r.set("count:{}".format(url), 0)
        r.setex("result:{}".format(url), 10, res)
        return res

    return wrapper


@cache_url
def get_page(url: str) -> str:
    """
    obtain the html content of a particular url and return it.
    """
    res = requests.get(url)
    return res.text
