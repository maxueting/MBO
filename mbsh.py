import getSession
import getTaskid
import getRyjd
import json


# 目标审核
def mbsh(userid,period, hj):
    str1 = []  # list有序，可修改
    for i in range(2):
        # 登录审核人账号获取session
        userid1 = getRyjd.getRyjd(period, 40, hj, userid)
        if userid1 == 1:
            break
        else:
            session2 = getSession.getSession(userid1, hj)
            # 调用todo接口获取taskid（之前要是获取了这里可以传入）,审核tab=20
            taskid = getTaskid.getTaskid(userid, 20, period, session2, hj)
            # 审核通过
            url = hj + "/cloud/review-server/target/reviewSubmit"
            data = json.dumps({
                "taskId": taskid,
                "targetId": userid,
                "period": period
            })
            headers = {'Content-Type': 'application/json', 'kbn-version': '6.4.3'}
            res = session2.post(url, data=data, headers=headers)
            str1.insert(i, userid1 + " 目标审核： "+res.text)
    return str1