import random


# first = ["你好啊!    ", "hello  ", "哈喽   "]
# second = ["想约吗?    ", "想交个朋友吗?     ", "想找个磕泡泡的      ", "想找个哄睡的?       "]
# third = ["要会玩的   ", "要会疼人的      ", "要成年哦     "]
# four = ["加我吧   ", "加我V     ", "加我微   "]
# five = ["acyy1314a   ", "acyy1314a    ", "acyy1314a  "]


def get_send_str():
    # send_str = "".join(
    #     [random.choice(first), random.choice(second), random.choice(third), random.choice(four),
    #      random.choice(five)])
    return "不好意思, 深夜打扰了, 成人交友需要吗? 定期组织线上, 线下同城活动! 加我V:acyy1314a        拉你进群,如有打扰,请多多包涵{}, 谢谢{}".format(
        chr(random.randint(1, 122)), chr(random.randint(1, 122)))


print(get_send_str())
