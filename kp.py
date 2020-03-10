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
                        "assessMain": {
                            "id": 2,
                            "assessContent": "cs",
                            "type": 2,
                            "weight": 20
                        }
                    }, {
                        "id": bloklist[1]["blockItemList"][1]["id"],
                        "assessMain": {
                            "id": 4,
                            "assessContent": "cs",
                            "type": 2,
                            "weight": 5
                        }
                    }, {
                        "id": bloklist[1]["blockItemList"][2]["id"],
                        "assessMain": {
                            "id": 2,
                            "assessContent": "cs",
                            "type": 2,
                            "weight": 45
                        }
                    }]
                }, {
                    "id": bloklist[2]["id"],
                    "blockItemList": [{
                        "id": bloklist[2]["blockItemList"][0]["id"],
                        "assessMain": {
                            "id": 3,
                            "assessContent": "cs",
                            "type": 2,
                            "weight": 5
                        }
                    }, {
                        "id": bloklist[2]["blockItemList"][1]["id"],
                        "assessMain": {
                            "id": 4,
                            "assessContent": "cs",
                            "type": 2,
                            "weight": 5
                        }
                    }]
                }, {
                    "id": bloklist[3]["id"],
                    "blockItemList": [{
                        "id": bloklist[3]["blockItemList"][0]["id"],
                        "assessMain": {
                            "id": 2,
                            "assessContent": "cs",
                            "type": 2,
                            "weight": 20
                        }
                    }]
                }],
                "strength": "cs",
                "weakness": "cs",
                "developOption": "cs",
                "evaluateLevel": "A",
                "finalScore": 2.25,
                "suggestLevel": "C"
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
                        "assessMain": {
                            "id": 101,
                            "assessContent": "cs ",
                            "type": 1,
                            "weight": 0
                        }
                    }, {
                        "id": bloklist[0]["blockItemList"][1]["id"],
                        "assessMain": {
                            "id": 101,
                            "assessContent": "cs",
                            "type": 1,
                            "weight": 0
                        }
                    }, {
                        "id": bloklist[0]["blockItemList"][2]["id"],
                        "assessMain": {
                            "id": 101,
                            "assessContent": "cs",
                            "type": 1,
                            "weight": 0
                        }
                    }]
                }, {
                    "id": bloklist[1]["id"],
                    "blockItemList": [{
                        "id": bloklist[1]["blockItemList"][0]["id"],
                        "assessMain": {
                            "id": 2,
                            "assessContent": "cs",
                            "type": 2,
                            "weight": 20
                        }
                    }, {
                        "id": bloklist[1]["blockItemList"][1]["id"],
                        "assessMain": {
                            "id": 4,
                            "assessContent": "cs",
                            "type": 2,
                            "weight": 5
                        }
                    }, {
                        "id": bloklist[1]["blockItemList"][2]["id"],
                        "assessMain": {
                            "id": 2,
                            "assessContent": "cs",
                            "type": 2,
                            "weight": 45
                        }
                    }]
                }, {
                    "id": bloklist[2]["id"],
                    "blockItemList": [{
                        "id": bloklist[2]["blockItemList"][0]["id"],
                        "assessMain": {
                            "id": 3,
                            "assessContent": "cs",
                            "type": 2,
                            "weight": 5
                        }
                    }, {
                        "id": bloklist[2]["blockItemList"][1]["id"],
                        "assessMain": {
                            "id": 4,
                            "assessContent": "cs",
                            "type": 2,
                            "weight": 5
                        }
                    }]
                }, {
                    "id": bloklist[3]["id"],
                    "blockItemList": [{
                        "id": bloklist[3]["blockItemList"][0]["id"],
                        "assessMain": {
                            "id": 2,
                            "assessContent": "cs",
                            "type": 2,
                            "weight": 20
                        }
                    }]
                }],
                "strength": "cs",
                "weakness": "cs",
                "developOption": "cs",
                "yearEndAbility": 101,
                "yearEndLevel": "S",
                "evaluateLevel": "A",
                "yearSuggestScore": "A",
                "yearEndScore": 4.25,
                "adviceAbility": 101,
                "finalScore": 2.25,
                "suggestLevel": "C"
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
                "assessMain": {
                    "id": 4,
                    "assessContent": "测试",
                    "type": 2,
                    "weight": 50
                }
            }, {
                "id": bloklist[0]["blockItemList"][1]["id"],
                "assessMain": {
                    "id": 3,
                    "assessContent": "测试",
                    "type": 2,
                    "weight": 20
                }
            }]
        }, {
            "id": bloklist[1]["id"],
            "blockItemList": [{
                "id": bloklist[1]["blockItemList"][0]["id"],
                "assessMain": {
                    "id": 2,
                    "assessContent": "测试",
                    "type": 2,
                    "weight": 5
                }
            }, {
                "id": bloklist[1]["blockItemList"][1]["id"],
                "assessMain": {
                    "id": 1,
                    "assessContent": "测试",
                    "type": 2,
                    "weight": 5
                }
            }]
        }, {
            "id": bloklist[2]["id"],
            "blockItemList": [{
                "id": bloklist[2]["blockItemList"][0]["id"],
                "assessMain": {
                    "id": 5,
                    "assessContent": "测试",
                    "type": 2,
                    "weight": 20
                }
            }]
        }],
        "strength": "测试",
        "weakness": "测试",
        "developOption": "测试",
        "evaluateLevel": "B+",
        "finalScore": 3.75,
        "suggestLevel": "B+",
    })
    headers = {'Content-Type': 'application/json', 'kbn-version': '6.4.3'}
    url = hj + "/cloud/review-server/target/assess/main/submit"
    res1 = session.post(url, data=data, headers=headers)
    return userid1+" 绩效考评： " + res1.text