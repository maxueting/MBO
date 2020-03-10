# -*- coding: UTF-8 -*-
import json
import getSession
import mbfq
import mbzd
import mbsh
import fqkp
import zp
import kp

# 获取某部门某周期下所有初始状态的员工ID


def getUserid(dept, period, hj):
    session = getSession.getSession("h17767", hj)
    url = hj + "/cloud/base-server/auth/exportUserId/" + dept + "/" + period
    res = session.get(url)
    ures = res.text
    jres = json.loads(ures)
    userid = jres["data"]
    uuserid = userid.replace("[", "", 2)
    uuuserid = uuserid.replace("]", "", 2)
    str_list = uuuserid.split(", ")
    return str_list


dept = "D002001070"
hj = "http://mbo.beta.netease.com"
period = "2019Q3"
str_list = getUserid(dept, period, hj)

for userid in str_list:
    print("----------------------------------------" + userid + "----------------------------------------")
    try:
        fqm = mbfq.mbfq(period, userid, hj)
        print(fqm)
        if fqm.rfind("200") == -1:
            continue

        zd = mbzd.mbzd(period, userid, hj)
        print(zd)
        if zd.rfind("200") == -1:
            continue

        for i in mbsh.mbsh(userid, period, hj):
            print(i)
            if i.rfind("200") == -1:
                continue

        fqk = fqkp.fqkp(period, userid, hj)
        print(fqk)
        if fqk.rfind("200") == -1:
            continue

        zzp = zp.zp(period, userid, hj)
        print(zzp)
        if zzp.rfind("200") == -1:
            continue

        kkp = kp.kp(period, userid, hj)
        print(kkp)
        if kkp.rfind("200") == -1:
            continue

    except Exception as e:
        print(e)
        print(userid + " 流程异常，跳过")
        pass
    continue
