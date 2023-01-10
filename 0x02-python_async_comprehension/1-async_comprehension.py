#!/usr/bin/env python3
"""Async comprehension"""

from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers using an
    async comprehensing over async_generator
    """
    numbers = [i async for i in async_generator()]
    return numbers
