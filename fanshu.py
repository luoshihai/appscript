# coding=utf-8
from appium import webdriver
import time, random

from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.fanshu.xiaozu'
desired_caps['appActivity'] = 'com.fanshu.daily.FSMain'
desired_caps["unicodeKeyboard"] = True,
desired_caps["resetKeyboard"] = True,

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

first = ["你好啊!    ", "hello  ", "哈喽   "]
second = ["网恋吗?    ", "处CP吗? ", "处对象吗?  ", "交个朋友好吗?  "]
third = ["这个不经常上   ", "这个不经常用    ", "这个聊天不方便    "]
four = ["加我微  acyy1314a     ", "加我威  acyy1314a     ", "加我V  acyy1314a     "]


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


def swipe_down(t=1000):
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.25)
    y2 = int(l[1] * 0.75)
    driver.swipe(x1, y1, x1, y2, t)


num = (0.65, 0.75, 0.85)


def swipe_up(t=1000):
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.25)
    y2 = int(l[1] * random.choice(num))
    driver.swipe(x1, y2, x1, y1, t)


conment_name = set()


def dump_to_chat(el_avor):
    el_avor.click()
    el_sixin = driver.find_elements_by_name("私信")
    if el_sixin:
        el_sixin[0].click()

        el_iv = driver.find_elements_by_id("com.fanshu.xiaozu:id/iv_userhead")
        if not el_iv:
            send_str = "".join(
                [random.choice(first), random.choice(second), random.choice(third), random.choice(four),
                 str(random.randint(0, 126))])
            driver.find_element_by_id("com.fanshu.xiaozu:id/et_sendmessage").send_keys(send_str)
            # driver.set_value(driver.find_element_by_id("com.fanshu.xiaozu:id/et_sendmessage"), send_str)
            el_send = driver.find_elements_by_id("com.fanshu.xiaozu:id/btn_send")
            if el_send:
                el_send[0].click()
        else:
            el_title = driver.find_elements_by_id("com.fanshu.xiaozu:id/title")
            if el_title:
                conment_name.add(el_title[0].text)
        driver.keyevent(4)
    driver.keyevent(4)


def dump_to_comment():
    time.sleep(1)
    el_rls = driver.find_element_by_class_name("android.widget.ListView").find_elements_by_class_name(
        "android.widget.RelativeLayout")
    if el_rls:
        el_comment = el_rls[0].find_element_by_id("com.fanshu.xiaozu:id/tab_comment")
        if el_comment:
            el_comment.find_element_by_id("com.fanshu.xiaozu:id/tab_icon").click()
            time.sleep(0.5)
            # el_coments_img = driver.find_element_by_class_name("android.widget.ListView").find_elements_by_id(
            #     "com.fanshu.xiaozu:id/user_img")
            el_comment_views = driver.find_elements_by_id("com.fanshu.xiaozu:id/comment_view")
            if el_comment_views:
                for i in range(len(el_comment_views)):
                    el_comment_name = el_comment_views[i].find_elements_by_id("com.fanshu.xiaozu:id/user_name")

                    if el_comment_name:
                        if el_comment_name[0].text in conment_name:
                            continue
                        else:
                            conment_name.add(el_comment_name[0].text)
                    else:
                        continue

                    el_avor = el_comment_views[i].find_elements_by_id("com.fanshu.xiaozu:id/user_img")
                    try:
                        if el_avor:
                            dump_to_chat(el_avor[0])
                    except NoSuchElementException as e:
                        continue
                # for 循环完成
                driver.keyevent(4)
                swipe_up()
                time.sleep(1)
                dump_to_comment()
            else:
                driver.keyevent(4)
                swipe_up()
                time.sleep(1)
                dump_to_comment()
        else:
            swipe_up()
            time.sleep(1)
            dump_to_comment()
    else:
        swipe_up()
        time.sleep(1)
        dump_to_comment()


try:
    time.sleep(1)
    dump_to_comment()
except Exception as e:
    print(e)
finally:
    driver.quit()
