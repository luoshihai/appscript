from appium import webdriver
import time, random
from appscript.wubaicaipiao.config import get_send_str
from appscript.wubaicaipiao.swipeutil import SwipeUtils
from appscript.wubaicaipiao.redisutils import insert_str

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.esun.ui'
desired_caps['appActivity'] = 'com.esun.mainact.home.HomeMainFragmentActivity'
desired_caps["unicodeKeyboard"] = True,
desired_caps["resetKeyboard"] = True,
desired_caps["sessionOverride"] = True,
desired_caps["appWaitActivity"] = 'com.esun.mainact.home.HomeMainFragmentActivity'

driver = webdriver.Remote('http://localhost:45724/wd/hub', desired_caps)

swipe_util = SwipeUtils(driver)


# users = set()


def start():
    el_m = driver.find_elements_by_name("社区")
    if el_m:
        el_m[0].click()
        go_ba_main()
    else:
        driver.start_activity('com.esun.ui', "com.esun.mainact.home.HomeMainFragmentActivity")
        start()


def go_ba_main():
    time.sleep(2)
    ef_texts = driver.find_elements_by_id("com.esun.ui:id/square_content")
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
        driver.start_activity('com.esun.ui', "com.esun.mainact.home.HomeMainFragmentActivity")
        start()


def go_comment():
    el_edit = driver.find_elements_by_id("com.esun.ui:id/squaredetail_comment_tv")

    if el_edit:
        el_edit[0].click()
    else:
        driver.start_activity('com.esun.ui', "com.esun.mainact.home.HomeMainFragmentActivity")
        start()

    el_ed = driver.find_elements_by_id("com.esun.ui:id/squaredetail_comment_et")
    el_send = driver.find_elements_by_id("com.esun.ui:id/comment_confirm_tv")
    if el_ed and el_send:
        el_ed[0].send_keys(get_send_str())
        el_send[0].click()
        driver.keyevent(4)
        driver.back()
        time.sleep(0.5)

    else:
        driver.start_activity('com.esun.ui', "com.esun.mainact.home.HomeMainFragmentActivity")
        start()


if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print(e)
        driver.start_activity('com.esun.ui', "com.esun.mainact.home.HomeMainFragmentActivity")
        start()
