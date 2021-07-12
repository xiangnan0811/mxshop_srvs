# -*- coding: utf-8 -*-
"""
@Author      : Xiangnan
@Time        : 2021/7/12 14:10
@File        : user.py
@Version     : python 3.8.5
@Description : 
"""
import time

import grpc

from user_srv.model.models import User
from user_srv.proto import user_pb2, user_pb2_grpc


class UserServicer(user_pb2_grpc.UserServicer):
    """获取用户列表"""
    def GetUserList(self, request: user_pb2.PageInfo, context):
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
            rsp.data.append(user_info_rsp)
        return rsp


