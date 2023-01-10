#!/usr/bin/env python3
"""Async comprehension"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """runs async_comprehension() four times in parallel"""
    start = time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    return (time() - start)
