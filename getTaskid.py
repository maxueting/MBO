import json

# 请求我的待办接口获取taskID,自评tabID=19
def getTaskid(userid, tabid, period, session, hj):
    data = {"tabId": tabid, "pageSize": "20", "currentPage": "1"}
    res = session.get(url=hj+"/cloud/review-server/task/todo", params=data)
    todo = res.text
    # print(todo)
    jtodo = json.loads(todo)
    for i in jtodo["data"]["result"]:
        if (i["currentPeriod"] == period) & (i["taskInfo"]["taskTarget"]["id"] == userid):
            return i["taskInfo"]["id"]