# **coding: UTF-8**
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser

from django.db import models

# Create your models here.


# User模块，包含里主键ID、密码（password）、最后一次登录时间（last_login）、用户名（username）、用户邮箱（email）、帐号创建时间（creat_time）、用户类型(admin_type)
class User(AbstractBaseUser):
    ADMIN_TYPE_CHOICES = (
        (0,"普通用户"),
        (2,"普通管理员"),
        (3,"超级管理员"),
    )

    # 用户名
    usrname = models.CharField("用户名",max_length=30, unique=True)
    # 用户邮箱
    email = models.EmailField("邮箱",max_length=254, blank=True, null=True)
    # 用户注册时间
    create_time = models.DateTimeField("注册时间",auto_now_add=True, null=True)
    # 0代表是普通用户，2代表是普通管理员，3代表是超级管理员
    admin_type = models.IntegerField("用户类型",default=0, choices=ADMIN_TYPE_CHOICES)
    # 账户余额
    balance = models.FloatField("账户余额", default=0)

    class Meta:
        db_table = "user"