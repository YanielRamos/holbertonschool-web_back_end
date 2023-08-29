#!/usr/bin/env python3
"""Script that return a asyncio task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """function"""
    return asyncio.Task(wait_random(max_delay))
