import getRyjd
import getSession
import json




#结果审核
def jgsh(period, userid, hj):
    for i in range(10):
        # 登录审核人账号获取uid,
        userid1 = getRyjd.getRyjd(period, 40, hj, userid)
        if userid1 == 1:
            break
        else:
            session2 = getSession.getSession(userid1, hj)
            # 审核通过
            url = hj + "/cloud/review-server/review/submit"
            data = json.dumps({
                "deptIds": ["D103MNG"],
                "period": period,
                "taskDefinitionKey": "RESULT_REVIEW_SECOND",
                "deptId": "D103MNG",
                "scope": "0"
            })
            headers = {'Content-Type': 'application/json', 'kbn-version': '6.4.3'}
            res = session2.post(url, data=data, headers=headers)
            print(userid + "结果审核： " + res.text)


