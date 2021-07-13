# -*- coding: utf-8 -*-
"""
@Author      : Xiangnan
@Time        : 2021/7/12 14:42
@File        : user.py
@Version     : python 3.8.5
@Description : 
"""
import grpc

from user_srv.proto import user_pb2, user_pb2_grpc


class UserTest:
    def __init__(self):
        # 连接grpc服务器
        channel = grpc.insecure_channel("127.0.0.1:8078")
        self.stub = user_pb2_grpc.UserStub(channel)

    def user_list(self):
        rsp: user_pb2.UserListResponse = self.stub.GetUserList(user_pb2.PageInfo(pn=2, pSize=2))
        print(rsp.total)
        for user in rsp.data:
            print(user.mobile, user.birthDay)

    def get_user_by_id(self, _id):
        rsp: user_pb2.UserInfoResponse = self.stub.GetUserById(user_pb2.IdRequest(id=_id))
        print(rsp.mobile)


if __name__ == '__main__':
    user_test = UserTest()
    # user_test.user_list()
    user_test.get_user_by_id(1)
