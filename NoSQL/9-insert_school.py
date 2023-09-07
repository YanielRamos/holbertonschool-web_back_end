#!/usr/bin/env python3
"""Module that inserts a new doc"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """function that adds the doc"""

    new_school = mongo_collection.insert_one(kwargs)

    return new_school.inserted_id
    