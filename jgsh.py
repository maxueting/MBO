import getRyjd
import getSession
import json

# 结果审核


def jgsh(period, hj,  userid):

    str1 = []
    str2 = [userid+"结果审核：该员工所在部门已审核完成或未进入审核阶段"]
    for n in range(100):
        # 登录审核人账号获取uid,
        userid1 = getRyjd.getRyjd(period, 45, hj, userid)
        if userid1 == 1:
            if str1 == []:
                return str2
            else:
                return str1
        else:
            session2 = getSession.getSession(userid1, hj)
            data = {"tabId": "23", "pageSize": "20", "currentPage": "1"}
            res = session2.get(url=hj + "/cloud/review-server/task/todo", params=data)
            todo = res.text

            jtodo = json.loads(todo)
            for i in jtodo["data"]["result"]:
                if i["currentPeriod"] == period:
                    taskDefinitionKey = i["currentNode"]["id"]
                    deptid = i["taskInfo"]["deptId"]
            # 审核通过
            url = hj + "/cloud/review-server/review/submit"
            data = json.dumps({
                "deptIds": [deptid],
                "period": period,
                "taskDefinitionKey": taskDefinitionKey,
                "deptId": deptid,
                "scope": "0"
            })
            headers = {'Content-Type': 'application/json', 'kbn-version': '6.4.3'}
            res = session2.post(url, data=data, headers=headers)
            str1.insert(n, userid1 + "结果审核： " + res.text)


# print(jgsh("2020Q2", "http://mbo.test.netease.com", "H11795"))