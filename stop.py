import json


# 如果当前接口返回不是200就执行下一个人
def stop(str):
    re = str.rfind("200", 0, len(str))
    if re == -1:
        return 0
    else:
        return 1