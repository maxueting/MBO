import getSession
import json


# 目标发起
def mbfq(period,userid, hj):
    session = getSession.getSession("H17767", hj)
    data = json.dumps({
        "period": period,
        "userIdList": [userid]
    })
    headers = {'Content-Type': 'application/json', 'kbn-version': '6.4.3'}
    url = hj + "/cloud/review-server/progress/startTargetSet"
    res = session.post(url, data=data, headers=headers)
    return "H17767" + " 目标发起： " + res.text