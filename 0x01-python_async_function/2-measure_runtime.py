#!/usr/bin/env python3
'''a function with ints as arg that measures\
        the total execution time'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' computes the average runtimes of wait_n
    '''
    start = time.time()
    delay = asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
