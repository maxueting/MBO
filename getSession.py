import requests

# 获取session


def getSession(userid, hj):

    url = hj + "/cloud/base-server/login/" + userid + "/mbo_13"  # 这里只有url，字符串格式
    session = requests.session()
    response = session.get(url)
    return session
