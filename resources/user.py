# coding=utf-8
"""
@Author：wang jian wei
@date：2023/3/4 21:06
"""

from flask_restful import Resource, reqparse
from flask import jsonify, request
from model import Edr, Edc
from ext import celery
from tasks import add_task


class PasswordLogin(Resource):
    URL = "/login"

    def __init__(self):
        super().__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("token", required=True, type=str, help="input token", location="json", nullable=False)

    def get(self):
        query = Edr.query.filter()
        a = query.filter_by()
        for n in a:
            print(n)

        # signature("add").apply_async()
        # celery.send_task("add")
        add_task.delay()
        return jsonify({"hello": "sentry"})
