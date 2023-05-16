# coding=utf-8
"""
@Author：wang jian wei
@date：2023/3/13 10:32
"""
from ext import db
from sqlalchemy import Column, Integer, String, UniqueConstraint, Text


class Edr(db.Model):
    __bind_key__ = 'edr'
    id = Column(Integer(), autoincrement=True, primary_key=True)
    table1 = Column(String(16), comment="table1")


class Edc(db.Model):
    __bind_key__ = 'edc'
    id = Column(Integer(), autoincrement=True, primary_key=True)
    table2 = Column(String(16), comment="table2")
