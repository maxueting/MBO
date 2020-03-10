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
    bloklist = res["data"]["targetBaseInfo"]["blockList"]
    if bloklist[0]["code"] == "0006":
        if bloklist[0]["blockItemList"] == []:
            data = json.dumps({
                "taskId": taskid,
                "period": period,
                "targetId": userid,
                "deptId": deptId,
                "blockList": [{
                    "id": bloklist[0]["id"],
                    "blockItemList": []
                }, {
                    "id": bloklist[1]["id"],
                    "blockItemList": [{
                        "id": bloklist[1]["blockItemList"][0]["id"],
                        "assessSelf": {
                            "id": 3,
                            "assessContent": "zp",
                            "type": 2,
                            "weight": 20
                        }
                    }, {
                        "id": bloklist[1]["blockItemList"][1]["id"],
                        "assessSelf": {
                            "id": 4,
                            "assessContent": "zp",
                            "type": 2,
                            "weight": 5
                        }
                    }, {
                        "id": bloklist[1]["blockItemList"][2]["id"],
                        "assessSelf": {
                            "id": 2,
                            "assessContent": "zp",
                            "type": 2,
                            "weight": 45
                        }
                    }]
                }, {
                    "id": bloklist[2]["id"],
                    "blockItemList": [{
                        "id": bloklist[2]["blockItemList"][0]["id"],
                        "assessSelf": {
                            "id": 2,
                            "assessContent": "zp",
                            "type": 2,
                            "weight": 5
                        }
                    }, {
                        "id": bloklist[2]["blockItemList"][1]["id"],
                        "assessSelf": {
                            "id": 2,
                            "assessContent": "zp",
                            "type": 2,
                            "weight": 5
                        }
                    }]
                }, {
                    "id": bloklist[3]["id"],
                    "blockItemList": [{
                        "id": bloklist[3]["blockItemList"][0]["id"],
                        "assessSelf": {
                            "id": 2,
                            "assessContent": "zp",
                            "type": 2,
                            "weight": 20
                        }
                    }]
                }],
                "performanceAppendixList": []
            })
        else:
            data = json.dumps({
                "taskId": taskid,
                "period": period,
                "targetId": userid,
                "deptId": deptId,
                "blockList": [{
                    "id": bloklist[0]["id"],
                    "blockItemList": [{
                        "id": bloklist[0]["blockItemList"][0]["id"],
                        "assessSelf": {
                            "id": 102,
                            "assessContent": "zp",
                            "type": 1,
                            "weight": 0
                        }
                    }, {
                        "id": bloklist[0]["blockItemList"][1]["id"],
                        "assessSelf": {
                            "id": 102,
                            "assessContent": "zp",
                            "type": 1,
                            "weight": 0
                        }
                    }, {
                        "id": bloklist[0]["blockItemList"][2]["id"],
                        "assessSelf": {
                            "id": 102,
                            "assessContent": "zp",
                            "type": 1,
                            "weight": 0
                        }
                    }]
                }, {
                    "id": bloklist[1]["id"],
                    "blockItemList": [{
                        "id": bloklist[1]["blockItemList"][0]["id"],
                        "assessSelf": {
                            "id": 4,
                            "assessContent": "zp",
                            "type": 2,
                            "weight": 5
                        }
                    }, {
                        "id": bloklist[1]["blockItemList"][1]["id"],
                        "assessSelf": {
                            "id": 4,
                            "assessContent": "zp",
                            "type": 2,
                            "weight": 20
                        }
                    }, {
                        "id": bloklist[1]["blockItemList"][2]["id"],
                        "assessSelf": {
                            "id": 2,
                            "assessContent": "zp",
                            "type": 2,
                            "weight": 45
                        }
                    }]
                }, {
                    "id": bloklist[2]["id"],
                    "blockItemList": [{
                        "id": bloklist[2]["blockItemList"][0]["id"],
                        "assessSelf": {
                            "id": 1,
                            "assessContent": "zp",
                            "type": 2,
                            "weight": 5
                        }
                    }, {
                        "id": bloklist[2]["blockItemList"][1]["id"],
                        "assessSelf": {
                            "id": 3,
                            "assessContent": "zp",
                            "type": 2,
                            "weight": 5
                        }
                    }]
                }, {
                    "id": bloklist[3]["id"],
                    "blockItemList": [{
                        "id": bloklist[3]["blockItemList"][0]["id"],
                        "assessSelf": {
                            "id": 4,
                            "assessContent": "zp",
                            "type": 2,
                            "weight": 20
                        }
                    }]
                }],
                "performanceAppendixList": []
            })
    elif bloklist[0]["code"] == '0007':
        data = json.dumps({
            "taskId": taskid,
            "period": period,
            "targetId": userid,
            "deptId": deptId,
            "blockList": [{
                "id": bloklist[0]["id"],
                "blockItemList": [{
                    "id": bloklist[0]["blockItemList"][0]["id"],
                    "assessSelf": {
                        "id": 5,
                        "assessContent": "11",
                        "type": 2,
                        "weight": 50
                    }
                }, {
                    "id": bloklist[0]["blockItemList"][1]["id"],
                    "assessSelf": {
                        "id": 5,
                        "assessContent": "11",
                        "type": 2,
                        "weight": 20
                    }
                }]
            }, {
                "id": bloklist[1]["id"],
                "blockItemList": [{
                    "id": bloklist[1]["blockItemList"][0]["id"],
                    "assessSelf": {
                        "id": 5,
                        "assessContent": "11",
                        "type": 2,
                        "weight": 5
                    }
                }, {
                    "id": bloklist[1]["blockItemList"][1]["id"],
                    "assessSelf": {
                        "id": 5,
                        "assessContent": "11",
                        "type": 2,
                        "weight": 5
                    }
                }]
            }, {
                "id": bloklist[2]["id"],
                "blockItemList": [{
                    "id": bloklist[2]["blockItemList"][0]["id"],
                    "assessSelf": {
                        "id": 5,
                        "assessContent": "11",
                        "type": 2,
                        "weight": 20
                    }
                }]
            }],
            "performanceAppendixList": []
        })
    headers = {'Content-Type': 'application/json', 'kbn-version': '6.4.3'}
    url = hj + "/cloud/review-server/target/assess/self/submit"
    res1 = session1.post(url, data=data, headers=headers)
    return userid+" 绩效自评： " + res1.text