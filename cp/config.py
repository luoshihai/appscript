import random

# first = ["你好啊!    ", "hello  ", "哈哈哈   "]
# second = ["想赚钱吗?    ", "每天不贪稳定收入 ", "我收徒弟.稳赚不亏  ", "想轻松月入过万吗?  "]
# third = ["看我简介   ", "看我个人中心    ", "看我个人信息  "]
# four = ["有我联系方式!   ", "有我扣哦   !    ", "有我威信哦!  "]
# strs = ["最近分手了  有想处cp的小哥哥吗?  来场不分手的恋爱  加V: rfv2048", "家里总是催, 想租个男友回家 有愿意的吗?  加V: rfv2048"]
# sts = ["家里总是催, 想租个男友回家 有愿意的吗?  加V: libao300521", "最近分手了  有想处cp的小哥哥吗?  来场不分手的恋爱 +v: libao300521"
#     , "找个小哥哥网恋,要会疼人的, 可以奔现的来, 加V: libao300521"]
sts = ["日赚五百到一千, 想做的加头像", "免费提供精准计划, 日赚一百到一千, 想做的加头像", "只需要一个手机,日赚一百到一千,想做的加头像"]


def get_send_str():
    send_str = random.choice(sts)
    return send_str
