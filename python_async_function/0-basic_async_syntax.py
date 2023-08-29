#!/usr/bin/env python3
"""Script that select a random number with async"""
import asyncio
import random


@asyncio.coroutine
async def wait_random(max_delay: int = 10) -> float:
    """function that takes a random float using async"""

    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
