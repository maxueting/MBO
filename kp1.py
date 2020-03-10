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
    for i in blockList:
        




    headers = {'Content-Type': 'application/json', 'kbn-version': '6.4.3'}
    url = hj + "/cloud/review-server/target/assess/main/submit"
    res1 = session.post(url, data=data, headers=headers)
    return userid1 + " 绩效考评： " + res1.text