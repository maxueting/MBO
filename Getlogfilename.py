#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import datetime
import sys


def getlogfileName():
    # 创建log文件夹 在当前目录下os.getcwd()
    pwdir = os.getcwd() + '\\' + 'log'
    # 判断文件夹是否已存在
    isExists = os.path.exists(pwdir)
    if not isExists:
        os.makedirs(pwdir)
    # 年-月-日
    dayTime = datetime.datetime.now().strftime('%Y-%m-%d')
    pwd = os.getcwd() + '\\' + 'log' + '\\' + dayTime + '.txt'
    isExists = os.path.exists(pwd)
    if not isExists:
        f = open(pwd, 'w')
        f.close()
    return pwd
