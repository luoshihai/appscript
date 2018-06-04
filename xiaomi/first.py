from appium import webdriver
import time, random
from appscript.xiaomi.config import get_send_str
from appscript.xiaomi.swipeutil import SwipeUtils
import sys

sys.setrecursionlimit(1000000)
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.wld.net'
desired_caps['appActivity'] = 'com.wld.net.MainActivity'
desired_caps["unicodeKeyboard"] = True,
desired_caps["resetKeyboard"] = True,
desired_caps["sessionOverride"] = True,
desired_caps["appWaitActivity"] = 'com.wld.net.MainActivity'

driver = webdriver.Remote('http://localhost:45724/wd/hub', desired_caps)

swipe_util = SwipeUtils(driver)

users = set()

def restart():
    driver.start_activity("com.wld.net", "com.wld.net.MainActivity")
    start()

def start():
    el_shangquan = driver.find_elements_by_name("商圈")
    if el_shangquan:
        el_shangquan[0].click()
        time.sleep(3)
        go_ba_main()
    else:
        # print("商圈没找到")
        restart()

def go_ba_main():
    el_shangquan = driver.find_elements_by_id("com.wld.net:id/tv_comment")
    if el_shangquan:
        el_shangquan[0].click()
        time.sleep(0.5)
        go_comment()
    else:
        print("评论没找到39")
        restart()

def go_comment():

    el_bg = driver.find_elements_by_id("com.wld.net:id/input_comment_dialog_bg")
    if el_bg:
        el_bg[0].click()

    el_name = driver.find_elements_by_name("蜜友9037900085")
    if el_name:
        driver.keyevent(4)
        time.sleep(0.5)
        swipe_util.swipe_up()
        go_ba_main()
    else:
        el_shuo = driver.find_elements_by_name("说点什么吧")
        time.sleep(0.5)
        if el_shuo:
            el_shuo[0].click()
        el_ping = driver.find_elements_by_name("评论")
        el_send = driver.find_elements_by_name("发表")
        if el_ping and el_send:
            el_ping[0].send_keys(get_send_str())
            el_send[0].click()
            time.sleep(0.5)
            driver.keyevent(4)
            driver.back()
            swipe_util.swipe_up()
            go_ba_main()
        else:
            print("评论发表没找到65")
            # restart()
            driver.keyevent(4)
            driver.back()
            go_ba_main()



if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        # print(e)
        restart()
