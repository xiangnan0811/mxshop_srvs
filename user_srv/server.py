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

from user_srv.proto import user_pb2, user_pb2_grpc
from user_srv.handler.user import UserServicer


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:8078')
    print(f"启动服务：127.0.0.1:8078")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
