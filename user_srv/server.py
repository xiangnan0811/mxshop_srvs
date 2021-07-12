# -*- coding: utf-8 -*-
"""
@Author      : Xiangnan
@Time        : 2021/7/12 14:35
@File        : server.py
@Version     : python 3.8.5
@Description : 
"""
import logging
from concurrent import futures

import grpc
from loguru import logger

from user_srv.proto import user_pb2, user_pb2_grpc
from user_srv.handler.user import UserServicer


def serve():
    logger.add("logs/user_srv_{time}.log", format="{time:YYYY-MM-DD HH:MM:SS} | {level} | {message}", encoding="utf-8")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:8078')
    logger.info(f"启动服务：127.0.0.1:8078")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
