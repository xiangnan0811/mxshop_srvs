# -*- coding: utf-8 -*-
"""
@Author      : Xiangnan
@Time        : 2021/7/12 14:35
@File        : server.py
@Version     : python 3.8.5
@Description : 
"""
import argparse
import logging
import os
import signal
import sys
from concurrent import futures

import grpc
from loguru import logger

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASE_DIR)

from user_srv.proto import user_pb2_grpc
from user_srv.handler.user import UserServicer
from common.grpc_health.v1 import health_pb2_grpc
from common.grpc_health.v1 import health
from common.register.consul import ConsulRegister
from user_srv.settings import settings


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
        level="DEBUG"
    )
    # grpc服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册用户服务
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    # 注册健康检查服务
    health_pb2_grpc.add_HealthServicer_to_server(health.HealthServicer(), server)
    # 绑定端口
    server.add_insecure_port(f'{args.host}:{args.port}')

    # 主进程退出信号监听 并优雅退出
    signal.signal(signal.SIGINT, on_exit)               # Control + C
    signal.signal(signal.SIGTERM, on_exit)              # kill
    logger.info(f"启动服务：{args.host}:{args.port}")
    server.start()

    # 注册服务
    logger.info(f"注册 {settings.USER_SRV_NAME} 服务到 consul：{settings.CONSUL_HOST}:{settings.CONSUL_PORT}")
    consul_register = ConsulRegister(settings.CONSUL_HOST, settings.CONSUL_PORT)
    if not consul_register.register(
        name=settings.USER_SRV_NAME,
        id=settings.USER_SRV_NAME,
        address=args.host,
        port=args.port,
        tags=settings.USER_SRV_TAGS,
        check=None
    ):
        logger.error(f"注册服务失败！")
        sys.exit(0)
    logger.info(f"注册 {settings.USER_SRV_NAME} 服务成功！")

    logger.info(f"所有服务启动完成!")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
