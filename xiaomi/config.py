import random

# first = ["你好啊!    ", "hello  ", "哈哈哈   "]
# second = ["想赚钱吗?    ", "每天不贪稳定收入 ", "我收徒弟.稳赚不亏  ", "想轻松月入过万吗?  "]
# third = ["看我简介   ", "看我个人中心    ", "看我个人信息  "]
# four = ["有我联系方式!   ", "有我扣哦   !    ", "有我威信哦!  "]
strs = ["你好,我想了解下产品 ,加我Vx: rfv2048", "我想咨询下这款产品, 加我Vx: rfv2048"]
# "最近分手了  有想处cp的小哥哥吗?  来场不分手的恋爱  vx: rfv2048"

def get_send_str():
    # send_str = "".join(
    #     [random.choice(first), random.choice(second), random.choice(third), random.choice(four),
    #      str(random.randint(0, 126))])
    send_str = random.choice(strs)
    return send_str

