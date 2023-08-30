#!/usr/bin/env python3
"""Script that have a coroutine that
returns 10 random numbers"""
import random
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async function that collects 10 random numbers"""
    lst = []

    async for i in async_generator():
        lst.append(i)

    return lst