from appium import webdriver
import time, random
from appscript.cp.config import get_send_str
from appscript.cp.swipeutil import SwipeUtils
from appscript.cp.redisutils import insert_str

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.xiaoyu.rightone'
desired_caps['appActivity'] = 'com.xiaoyu.rightone.features.main.view.MainActivity'
desired_caps["unicodeKeyboard"] = True,
desired_caps["resetKeyboard"] = True,
desired_caps["sessionOverride"] = True,
desired_caps["appWaitActivity"] = 'com.xiaoyu.rightone.features.main.view.MainActivity'

driver = webdriver.Remote('http://localhost:45724/wd/hub', desired_caps)

swipe_util = SwipeUtils(driver)


# users = set()


def start():
    el_m = driver.find_elements_by_id("com.xiaoyu.rightone:id/bottom_button_moment")
    if el_m:
        el_m[0].click()
        go_ba_main()
    else:
        driver.start_activity('com.xiaoyu.rightone', "com.xiaoyu.rightone.features.main.view.MainActivity")
        start()


def go_ba_main():
    time.sleep(3)
    ef_texts = driver.find_elements_by_id("com.xiaoyu.rightone:id/moment_text")
    if ef_texts:
        for e in ef_texts:
            if insert_str(e.text) == 1:
                # users.add(e.text)
                e.click()
                time.sleep(0.5)
                go_comment()

        swipe_util.swipe_up()
        time.sleep(1)
        go_ba_main()
    else:
        driver.start_activity('com.xiaoyu.rightone', "com.xiaoyu.rightone.features.main.view.MainActivity")
        start()


def go_comment():
    el_edit = driver.find_elements_by_id("com.xiaoyu.rightone:id/moment_details_comment_edit")
    el_send = driver.find_elements_by_id("com.xiaoyu.rightone:id/moment_details_comment_send")

    if el_edit and el_send:
        el_edit[0].send_keys(get_send_str())
        el_send[0].click()
        driver.keyevent(4)
        time.sleep(0.5)

    else:
        driver.start_activity('com.xiaoyu.rightone', "com.xiaoyu.rightone.features.main.view.MainActivity")
        start()


if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print(e)
        driver.start_activity('com.xiaoyu.rightone', "com.xiaoyu.rightone.features.main.view.MainActivity")
        start()
