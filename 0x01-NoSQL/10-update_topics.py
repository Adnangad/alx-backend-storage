#!/usr/bin/env python3
"""
The module changes topics of a school based on name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Args:
    mongo_collection: the collection
    name: name of school
    topics: list of strings
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
