#!/usr/bin/env python3
"""Script that have a async generator"""
import asyncio
import random


async def async_generator() -> float:
    """async coroutine generator"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

                   