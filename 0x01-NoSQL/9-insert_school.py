#!/usr/bin/env python3
"""
This module inserts a doc to a collection and returns its id
"""


def insert_school(mongo_collection, **kwargs):
    """
    Args:
    mongo_collection:the collection
    **kwargs: the key value pairs to be added.
    return:
    id of the new doc.
    """
    rez = mongo_collection.insert_one({key: value for key, value in kwargs.items()})
    return rez.inserted_id
