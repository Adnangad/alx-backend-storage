#!/usr/bin/env python3
"""
The module lists all documents ina  collection
"""


def list_all(mongo_collection):
    """
    Args:
    mongo_collection: The collection to be checked
    """
    ls = []
    rez = mongo_collection.find({})
    for i in rez:
        if i is None:
            return []
        ls.append(i)
    return ls
