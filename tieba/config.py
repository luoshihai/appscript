import random

first = ["你好啊!    ", "hello  ", "哈哈哈   "]
second = ["想赚钱吗?    ", "每天不贪稳定收入 ", "我收徒弟.稳赚不亏  ", "想轻松月入过万吗?  "]
third = ["看我简介   ", "看我个人中心    ", "看我个人信息  "]
four = ["有我联系方式!   ", "有我扣哦   !    ", "有我威信哦!  "]


def get_send_str():
    send_str = "".join(
        [random.choice(first), random.choice(second), random.choice(third), random.choice(four),
         str(random.randint(0, 126))])
    return send_str
