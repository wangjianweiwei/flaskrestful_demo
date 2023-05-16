# coding=utf-8
"""
@Author：wang jian wei
@date：2023/3/4 21:26
"""
from celery import Celery
from flask_restful import Api
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()
cache = FlaskRedis()
celery = Celery(__name__, broker="redis://localhost:9736/8", include=["tasks"])


def extend(app):
    db.init_app(app)
    cache.init_app(app)
    api.init_app(app)
