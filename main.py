# -*- coding: UTF-8 -*-

import logging.handlers
import mbfq
import mbzd1
import mbsh
import fqkp
import zp1
import kp1
import Getlogfilename
import os
import jgsh
import time

LOG_FILE = Getlogfilename.getlogfileName()  # 获取log文件名
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
fmt = '%(asctime)s - %(message)s'
formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter
logger = logging.getLogger('log')  # 获取名为log的logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)


# 读取工号文件
try:
    # 填写读取工号文件地址，执行环境，当前周期
    pwd = os.getcwd() + '\\' + 'userID.txt'
    f = open(pwd, 'r')
    hj = "http://mbo.test.netease.com"
    period = "2020Q2"
    str = f.read()
    str_list = str.split()


    for userid in str_list:
        logger.info("----------------------------------------"+userid+"----------------------------------------")
        print("----------------------------------------"+userid+"----------------------------------------")
        try:
            fqm = mbfq.mbfq(period, userid, hj)
            print(fqm)
            logger.info(fqm)
            if fqm.rfind("200") == -1:
                continue

            zd = mbzd1.mbzd(period, userid, hj)
            print(zd)
            logger.info(zd)
            if zd.rfind("200") == -1:
                continue

            for i in mbsh.mbsh(userid, period, hj):
                logger.info(i)
                print(i)
                if i.rfind("200") == -1:
                    continue

            fqk = fqkp.fqkp(period, userid, hj)
            print(fqk)
            logger.info(fqk)
            if fqk.rfind("200") == -1:
                continue

            zzp = zp1.zp(period, userid, hj)
            print(zzp)
            logger.info(zzp)
            if zzp.rfind("200") == -1:
                continue

            kkp = kp1.kp(period, userid, hj)
            print(kkp)
            logger.info(kkp)
            if kkp.rfind("200") == -1:
                continue

        except Exception as e:
            print(userid+"流程异常")
            logger.info(e)
            logger.info(userid+" 流程异常，跳过")
            pass
        continue

    time.sleep(1)

    for userid in str_list:
        logger.info("--------------------------------------员工"+userid+"所在的部门开始审核--------------------------------------")
        print("--------------------------------------员工"+userid+"所在的部门开始审核--------------------------------------")

        for i in jgsh.jgsh(period, hj, userid):
            logger.info(i)
            print(i)





# 关闭文件
finally:
    if f:
        f.close()

