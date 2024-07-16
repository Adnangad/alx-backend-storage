#!/usr/bin/env python3
"""
Module groups a nd sorts stdents by avg value
"""


def top_students(mongo_collection):
    """
    Args:
    mongo_collection: the collection
    """
    param = {
            '$unwind': '$topics',
            '$group': {
                '_id': '$name',
                'average_score': {'$avg': '$topics.score'}
                },
            '$sort': { 'average_score' : 1}
            }
    students = mongo_collection.aggregate(param)
    result = []
    for idx, student in enumerate(students, start=1):
        result.append({
            '_id': f"[{idx}] {student['_id']}",
            'name': student['_id'],
            'averageScore': student['average_score']
        })

    return result
