# -*- coding:utf-8 -*-
"""
@Author：wang jian wei
@date：2023/3/4 20:57
"""

from flask import Flask

import config
from ext import extend, api


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    extend(app)

    return app
