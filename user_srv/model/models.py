# -*- coding: utf-8 -*-
"""
@Author      : Xiangnan
@Time        : 2021/7/1 12:43
@File        : models.py
@Version     : python 3.8.5
@Description : 
"""
from peewee import *
from user_srv.settings import settings


class BaseModel(Model):
    class Meta:
        database = settings.DB


class User(BaseModel):
    # 用户模型
    GENDER_CHOICES = (
        ('female', '女'),
        ('male', '男'),
        ('unknown', '未知'),
    )

    ROLE_CHOICES = (
        (1, '普通用户'),
        (2, '管理员'),
    )
    mobile = CharField(max_length=11, index=True, unique=True, verbose_name="手机号")
    password = CharField(max_length=200, verbose_name="密码")  # 1.密码密文 2.密文不可反解
    nickname = CharField(max_length=20, null=True, verbose_name="昵称")
    head_url = CharField(max_length=200, null=True, verbose_name="头像")
    birthday = DateField(null=True, verbose_name="生日")
    address = CharField(max_length=200, null=True, verbose_name="地址")
    desc = TextField(null=True, verbose_name="个人简介")
    gender = CharField(max_length=7, choices=GENDER_CHOICES, null=True, verbose_name="性别")
    role = IntegerField(default=1, choices=ROLE_CHOICES, verbose_name="用户角色")


if __name__ == '__main__':
    settings.DB.create_tables([User])
