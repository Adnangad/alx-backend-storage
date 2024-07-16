#!/usr/bin/env python3
"""
This module retreives info from  a db
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    Implements the main code
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_col = client.logs.nginx
    num = nginx_col.count_documents({})
    print(f"{num} logs")
    print("Methods:")
    get = nginx_col.count_documents({"method": "GET"})
    post = nginx_col.count_documents({"method": "POST"})
    put = nginx_col.count_documents({"method": "PUT"})
    patch = nginx_col.count_documents({"method": "PATCH"})
    delete = nginx_col.count_documents({"method": "DELETE"})
    stat = nginx_col.count_documents({"path": "/status"})
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{stat} status check")
    print("IPs:")
    params = [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
            ]
    rez = nginx_col.aggregate(params)
    for req_log in rez:
        ip = req_log['_id']
        req_count = req_log['totalRequests']
        print(f"\t{ip}: {req_count}")
