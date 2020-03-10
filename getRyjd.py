import getSession
import json



# 通过老赵账号的人员进度获取当前操作人,tabid: 目标制定39，目标审核40
def getRyjd(period, tabid, hj, userid):
    # 登录H17767,获取session
    session1 = getSession.getSession("H17767", hj)
    # 人员进度接口，获取审核人userID
    url = hj + "/cloud/review-server/progress/list"
    data = {"menuId": 33, "period": period, "searchWord": userid, "deptId": "", "tabId": tabid, "currentPage": 1,
            "pageSize": 20}
    res1 = session1.get(url=url, params=data)
    res2 = res1.text
    jres = json.loads(res2)
    if jres["data"]["totalResults"] == 0:
        userid1 = 1
    else:
        userid1 = jres["data"]["result"]["empList"][0]["opUserList"][0]["id"]
    return userid1