# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/5/11 15:51
"""
from celery import Task

from app import create_app
from ext import celery

app = create_app()


class ContextTask(Task):

    def __call__(self, *args, **kwargs):
        with app.app_context():
            super().__call__(*args, **kwargs)


setattr(celery, "Task", ContextTask)
