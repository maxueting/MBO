import json

# 进入这个人的绩效模板获取blockList
def getblocklist(taskid,userid,period,session,hj):
    url = hj+"/cloud/review-server/target/view"
    data = {"taskId": taskid, "targetId": userid, "period": period}
    res = session.get(url=url, params=data)
    res1 = res.text
    jres = json.loads(res1)
    # print("我获取到了该员工的绩效模板")
    return jres