#!/usr/bin/env python3
"""
Contains the list_all function
"""


def list_all(mongo_collection):
    """
    List all the documents in a collection
    """
    return [doc for doc in mongo_collection.find()]

