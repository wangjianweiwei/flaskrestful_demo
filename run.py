# coding=utf-8
"""
@Author：wang jian wei
@date：2023/3/14 09:38
"""
from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
