#!/usr/bin/env python3
"""
This module manipulates the redis db
"""
import redis
import uuid


class Cache:
    def __init__(self):
        """
        Initializes vars
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """
        generates a key and inserts data to redis db
        """
        key = int(uuid.uuid4())
        self._redis.set(key, data)
        return key
