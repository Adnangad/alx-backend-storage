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


def call_history(method: Callable) -> Callable:
    """
    A decorator that create input and output list keys
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        wrapper function
        """
        input_key = f"{method.__qualname__}:inputs"
        out_key =   f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwds)
        self._redis.rpush(out_key, str(result))
        return result
    return wrapper


class Cache:
    def __init__(self):
        """
        Initializes vars
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get_input_history(self, method):
        return self._redis.lrange(f"{method.__qualname__}:inputs", 0, -1)

    def get_output_history(self, method):
        return self._redis.lrange(f"{method.__qualname__}:outputs", 0, -1)


def replay(method):
    """
    display the history of calls of a particular function
    """
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")

    for inp, outp in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{inp.decode('utf-8')}) -> {outp.decode('utf-8')}")
