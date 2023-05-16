# coding=utf-8
"""
@Author：wang jian wei
@date：2023/3/4 21:04
"""

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:123456@127.0.0.1:3306/flaskrestful_demo?charset=utf8mb4'
SQLALCHEMY_BINDS = {
    'edc': f'mysql+pymysql://root:123456@127.0.0.1:3306/edc?charset=utf8mb4',
    'edr': f'mysql+pymysql://root:123456@127.0.0.1:3306/edr?charset=utf8mb4',
}
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

REDIS_URL = 'redis://:@localhost:9736/8'

INSTALL_APPS = ["resources", ]
