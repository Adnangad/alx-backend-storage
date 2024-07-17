#!/usr/bin/env python3
"""
This module manipulates the redis db
"""
import redis
import uuid
from typing import Union, Callable
from functools import wrapper


def count_calls(method: Callable) -> Callable:
    """
    A decorator
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        The wrapper function
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        """
        Initializes vars
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generates a key and inserts data to redis db
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None):
        """
        converts data back to desired format.
        """
        if self._redis.exists(key) == 1:
            rez = self._redis.get(key)
            if fn:
                return fn(rez)
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """
        Returns a str
        """
        return self._redis.get(key, fn=lambda x: x.decode('utf-8'))
    
    def get_int(self, key: str) -> int:
        """
        Returns an int
        """
        return self.get(key, fn=int)
