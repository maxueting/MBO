import getBlocklist
import getTaskid
import getSession
import getRyjd
import json


# 考评
def kp(period, userid, hj):
    # 登录老赵账号获取考评人userID，考评tabID=43
    userid1 = getRyjd.getRyjd(period, 43, hj, userid)
    session = getSession.getSession(userid1, hj)
    # 获取taskID,考评tab=21
    taskid = getTaskid.getTaskid(userid, 21, period, session, hj)
    res = getBlocklist.getblocklist(taskid, userid, period, session, hj)
    deptId = res["data"]["taskInfo"]["deptId"]
    blocklist = res["data"]["targetBaseInfo"]["blockList"]
    blockList1 = []
    n = 0
    for i in blocklist:
        blockList1.append({"id": i["id"], "blockItemList": []})

        for j in i["blockItemList"]:
            if i["blockItemList"] != []:
                if i["type"] == 1:
                    blockList1[n]["blockItemList"].append({
                        "id": j["id"],
                        "assessMain": {
                            "id": 101,
                            "assessContent": "考评",
                            "type": 1,
                            "weight": j["weight"]
                        }
                    })
                else:
                    blockList1[n]["blockItemList"].append({
                        "id": j["id"],
                        "assessMain": {
                            "id": 4,
                            "assessContent": "考评",
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
        "strength": "考评",
        "weakness": "考评",
        "developOption": "考评",
        "yearEndAbility": 101,
        "yearEndLevel": "B+",
        "evaluateLevel": "A",
        "yearSuggestScore": "A",
        "yearEndScore": 4.25,
        "adviceAbility": 101,
        "finalScore": 4,
        "suggestLevel": "A"
    })
    # print(data)

    headers = {'Content-Type': 'application/json', 'kbn-version': '6.4.3'}
    url = hj + "/cloud/review-server/target/assess/main/submit"
    res1 = session.post(url, data=data, headers=headers)
    return userid1 + " 绩效考评： " + res1.text

# print(kp("2020Q1", "H6836", "http://mbo.test.netease.com"))