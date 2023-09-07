#!/usr/bin/env python3
"""module that return a list of school"""
import pymongo


def schools_by_topic(mongo_collection, topic: str) -> list:
    """function that return a list of schools"""
    schools: list = []
    query = {"topics": topic}
    
    for school in mongo_collection.find(query):
        schools.append(school)

    return schools
