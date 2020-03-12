import getSession
import getTaskid
import getRyjd
import json

# 绩效面谈
def jxmt(userid,period, hj):
    userid1 = getRyjd.getRyjd(period, 46, hj, userid)
    session2 = getSession.getSession(userid1, hj)
    taskid = getTaskid.getTaskid(userid, 24, period, session2, hj)
    url = hj + "/cloud/review-server/result/communication"
    data = json.dumps({
        "taskId": taskid,
        "targetId": userid,
        "period": period
    })
    headers = {'Content-Type': 'application/json', 'kbn-version': '6.4.3'}
    res = session2.post(url, data=data, headers=headers)
    return userid1 + "绩效面谈： " + res.text

# print(jxmt("H1277", "2020Q2","http://mbo.test.netease.com"))

