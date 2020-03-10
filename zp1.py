import getSession
import getTaskid
import getBlocklist
import json

# 自评
def zp(period, userid, hj):
    session1 = getSession.getSession(userid, hj)
    taskid = getTaskid.getTaskid(userid, 19, period, session1, hj)
    res = getBlocklist.getblocklist(taskid, userid, period, session1, hj)
    deptId = res["data"]["taskInfo"]["deptId"]
    blockList = res["data"]["targetBaseInfo"]["blockList"]
    blockList1 = []
    n = 0
    for i in blockList:
        blockList1.append({"id": i["id"], "blockItemList": []})

        for j in i["blockItemList"]:
            if i["blockItemList"] != []:
                blockList1[n]["blockItemList"].append({
                    "id": j["id"],
                    "assessSelf": {
                        "id": 4,
                        "assessContent": "自评",
                        "type": 2,
                        "weight": j["weight"]
                    }
                })
        n = n + 1
    # print(blockList1)
    data = json.dumps({
        "taskId": taskid,
        "period": period,
        "targetId": userid,
        "deptId": deptId,
        "blockList": blockList1,
        "performanceAppendixList": []
    })
    # print(data)


    headers = {'Content-Type': 'application/json', 'kbn-version': '6.4.3'}
    url = hj + "/cloud/review-server/target/assess/self/submit"
    res1 = session1.post(url, data=data, headers=headers)
    return userid + " 绩效自评： " + res1.text

# zp("2020Q1", "H17786", "http://mbo.test.netease.com")