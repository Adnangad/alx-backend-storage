#!/usr/bin/env python3
"""
This module retreives info from  a db
"""
from pymongo import MongoClient


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
