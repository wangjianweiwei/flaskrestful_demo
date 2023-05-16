# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/5/11 14:37
"""

from ext import celery, cache
from model import Edr


@celery.task(name="add")
def add_task():
    query = Edr.query.filter()
    for n in query:
        print(n)
    cache.incr("my_account")
