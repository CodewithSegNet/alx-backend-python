#!/usr/bin/env python3
'''an async routine that takes in arg and \
        return the list of all delays'''
from typing import List
import asyncio
import random

wait = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delay = await asyncio.gather(*[wait(max_delay) for _ in range(n)])
    return sorted(delay)
