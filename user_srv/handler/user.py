# -*- coding: utf-8 -*-
"""
@Author      : Xiangnan
@Time        : 2021/7/12 14:10
@File        : user.py
@Version     : python 3.8.5
@Description : 
"""
import time
from datetime import date

import grpc
from loguru import logger
from peewee import DoesNotExist
from passlib.hash import pbkdf2_sha256
from google.protobuf import empty_pb2

from user_srv.model.models import User
from user_srv.proto import user_pb2, user_pb2_grpc


class UserServicer(user_pb2_grpc.UserServicer):
    """用户服务"""

    @staticmethod
    def convert_user_to_rsp(user):
        """转换 user 对象"""
        user_info_rsp = user_pb2.UserInfoResponse()
        user_info_rsp.id = user.id
        user_info_rsp.passWord = user.password
        user_info_rsp.mobile = user.mobile
        user_info_rsp.role = user.role
        if user.nickname:
            user_info_rsp.nickName = user.nickname
        if user.gender:
            user_info_rsp.gender = user.gender
        if user.birthday:
            user_info_rsp.birthDay = int(time.mktime(user.birthday.timetuple()))
        return user_info_rsp

    @logger.catch
    def GetUserList(self, request: user_pb2.PageInfo, context):
        """获取用户列表"""
        logger.info(f"请求用户列表：page: {request.pn}, size: {request.pSize}")
        rsp = user_pb2.UserListResponse()

        users = User.select()
        rsp.total = users.count()

        start = 0
        per_pages_nums = 10
        if request.pSize:
            per_pages_nums = request.pSize
        if request.pn:
            start = per_pages_nums * (request.pn - 1)
        users = users.limit(per_pages_nums).offset(start)
        for user in users:
            rsp.data.append(self.convert_user_to_rsp(user))
        return rsp

    @logger.catch
    def GetUserById(self, request: user_pb2.IdRequest, context):
        """通过 id 查询用户"""
        logger.info(f"通过 id 查询用户：id: {request.id}")
        try:
            user = User.get(User.id == request.id)
            return self.convert_user_to_rsp(user)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在！")
            return user_pb2.UserInfoResponse()

    @logger.catch
    def GetUserByMobile(self, request: user_pb2.MobileRequest, context):
        """通过 mobile 查询用户"""
        logger.info(f"通过 mobile 查询用户：mobile: {request.mobile}")
        try:
            user = User.get(User.mobile == request.mobile)
            return self.convert_user_to_rsp(user)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在!")
            return user_pb2.UserInfoResponse()

    @logger.catch
    def CreateUser(self, request: user_pb2.CreateUserInfo, context):
        """创建用户"""
        logger.info(f"创建用户: mobile: {request.mobile}")
        try:
            User.get(User.mobile == request.mobile)
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("用户已存在!")
            return user_pb2.UserInfoResponse()
        except DoesNotExist as e:
            pass

        user = User()
        user.nickname = request.nickName
        user.mobile = request.mobile
        user.password = pbkdf2_sha256.hash(request.passWord)
        user.save()

        return self.convert_user_to_rsp(user)

    @logger.catch
    def UpdateUser(self, request: user_pb2.UpdateUserInfo, context):
        """更新用户"""
        logger.info(f"更新用户: name: {request.nickName}")
        try:
            user = User.get(User.id == request.id)
            user.nickname = request.nickName
            user.gender = request.gender
            user.birthday = date.fromtimestamp(user.birthDay)
            user.save()
            return empty_pb2.Empty()
        except DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在！")
            return user_pb2.UserInfoResponse()

    @logger.catch
    def CheckPassWord(
        self,
        request: user_pb2.PassWordCheckRequest,
        context
    ) -> user_pb2.PassWordCheckResponse:
        """校验密码"""
        logger.info(f"校验密码: password: {request.password}")
        return user_pb2.PassWordCheckResponse(
            success=pbkdf2_sha256.verify(request.password, request.encryptedPassword)
        )
