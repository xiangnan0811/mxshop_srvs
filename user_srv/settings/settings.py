# -*- coding: utf-8 -*-
"""
@Author      : Xiangnan
@Time        : 2021/7/1 12:48
@File        : settings.py
@Version     : python 3.8.5
@Description : 配置中心
"""
import os

from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin


class ReconnectMySQLDatabase(ReconnectMixin, PooledMySQLDatabase):
    def sequence_exists(self, seq):
        pass


# mysql配置
MYSQL_DB = "mxshop_user_srv"
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = int(os.getenv('MYSQL_PORT'))
MYSQL_USER = "mxshop"
MYSQL_PASSWORD = os.getenv('MYSQL_MXSHOP_PASS')

DB = ReconnectMySQLDatabase(
    database=MYSQL_DB,
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
)

# consul配置
CONSUL_HOST = os.getenv('CONSUL_HOST')
CONSUL_PORT = int(os.getenv('CONSUL_PORT'))

# 服务相关配置
USER_SRV_NAME = "user-srv"
USER_SRV_TAGS = ["user", "srv", "Python"]
