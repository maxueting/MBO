# -*- coding: UTF-8 -*-

import getSession
import getTaskid
import getBlocklist
import json

# 目标制定
def mbzd(period,userid, hj):
    session = getSession.getSession(userid, hj)
    taskid = getTaskid.getTaskid(userid, 19, period, session, hj)
    jmb = getBlocklist.getblocklist(taskid, userid, period, session, hj)
    blockList = jmb["data"]["targetBaseInfo"]["blockList"]
    for i in blockList:
        n = 0
        for j in i["blockItemList"]:
            n = n + j["weight"]
        if n < i["weight"]:
            i["blockItemList"] = [{
                "name": "工作项",
                "weight": i["weight"],
                "documentExplain": "关键指标",
                "documentNorm": "评估标准",
                "modifyStatus": 2,
                "modifyField": "",
                "modifyFields": [""]
            }]
    data = json.dumps({
        "taskId": taskid,
        "performanceIdp": {
            "developmentGoals": "测试",
            "developmentPlan": "测试",
            "resourceSupport": "测试"
        },
        "blockList": blockList,
        "targetAppendixList": [
        ]
    })
    url = hj + "/cloud/review-server/target/submit"
    headers = {'Content-Type': 'application/json', 'kbn-version': '6.4.3'}
    res = session.post(url, data=data, headers=headers)
    return userid+" 目标制定： "+res.text

# mbzd("2020Q1", "H8596", "http://mbo.test.netease.com")
