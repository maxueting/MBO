import getSession
import json



# 发起考评
def fqkp(period, userid, hj):
    session = getSession.getSession("H17767", hj)
    url = hj + "/cloud/review-server/progress/startEvaluate"
    data = json.dumps({
        "period": period,
        "userIdList": [userid]
    })
    headers = {'Content-Type': 'application/json', 'kbn-version': '6.4.3'}
    res = session.post(url, data=data, headers=headers)
    return "H17767"+" 发起考评： "+res.text