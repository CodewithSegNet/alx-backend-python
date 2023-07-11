#!/usr/bin/env python3

''' a function that takes an int and return a asyncio.Task
'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

'''function def
'''
def task_wait_random(max_delay: int) -> asyncio.Task:
    '''create an asynchronous task for wait_random
    '''
    return asyncio.create_task(wait_random(max_delay))

