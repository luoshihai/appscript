import random

first = ["你好啊!    ", "hello   ", "哈哈哈   "]
second = ["想赚钱做兼职吗?     ", "想赚钱? 每天不贪稳定收入   ", "收徒弟, 每天赚点小钱   ", "想赚钱吗? 每天几百稳定收入!  "]
third = ["加我联系方式     ", "加我哦    ", "加我吧   "]
four = ["看我昵称        ", "看名字            ", "我的名字               "]
five = (".", "..", "...", "....", ".....", "-_-", "_-_")


def get_send_str():
    send_str = "".join(
        [random.choice(first), random.choice(second), random.choice(third), random.choice(four), random.choice(five)])
    return send_str


# print(get_send_str())
