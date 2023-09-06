#!/usr/bin/env python3
"""Modula tha list all documents in a collection"""
import pymongo


def list_all(mongo_collection) -> list:
    """function that list all docs"""

    docs: list = []

    for documents in mongo_collection.find():
        docs.append(documents)

    return docs
