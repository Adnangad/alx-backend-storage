#!/usr/bin/env python3
"""
This module returns a list of topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    Args:
    mongo_collection: the collection
    topic: the topic to be searched
    """
    rez = mongo_collection.find({'topic': {"$elemMatch": {"$eq": topic}}})
    return rez
