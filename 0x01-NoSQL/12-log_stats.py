#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_number = nginx_collection.count_documents({})
    print("{} logs".format(log_number))
    print("Methods:")
    stats_check = nginx_collection.count_documents({"path": "/status"})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))
    print("{} status check".format(stats_check))
