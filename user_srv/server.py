# -*- coding: utf-8 -*-
"""
@Author      : Xiangnan
@Time        : 2021/7/12 14:35
@File        : server.py
@Version     : python 3.8.5
@Description : 
"""
import os
import sys
import signal
import logging
import argparse
from concurrent import futures

import grpc
from loguru import logger

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASE_DIR)

from user_srv.proto import user_pb2, user_pb2_grpc
from user_srv.handler.user import UserServicer


def on_exit(signal, frame):
    logger.error(f"进程中断！")
    sys.exit(0)


def serve():
    # 参数解析
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host",
        nargs="?",
        type=str,
        default="127.0.0.1",
        help="binding host"
    )
    parser.add_argument(
        "--port",
        nargs="?",
        type=int,
        default=8078,
        help="the listening port"
    )
    args = parser.parse_args()
    # 日志文件
    logger.add(
        "logs/user_srv.log",
        format="{time:YYYY-MM-DD HH:MM:SS} | {level} | {message}",
        encoding="utf-8",
        rotation="00:00",
        retention="30 days",
        enqueue=True,
        diagnose=True,
        backtrace=True,
        compression="zip",
    )
    # grpc服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port(f'{args.host}:{args.port}')

    # 主进程退出信号监听 并优雅退出
    signal.signal(signal.SIGINT, on_exit)               # Control + C
    signal.signal(signal.SIGTERM, on_exit)              # kill
    logger.info(f"启动服务：{args.host}:{args.port}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
