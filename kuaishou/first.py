from appium import webdriver
import time, random
from kuaishou.config import get_send_str
from kuaishou.swipeutil import SwipeUtils

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.smile.gifmaker'
desired_caps['appActivity'] = 'com.yxcorp.gifshow.HomeActivity'
desired_caps["unicodeKeyboard"] = True,
desired_caps["resetKeyboard"] = True,

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

swipe_util = SwipeUtils(driver)

users = set()


def go_ba_main():
    if "HomeActivity" in driver.current_activity:
        el_containers = driver.find_elements_by_id("com.smile.gifmaker:id/container")
        el_containers[0].click()
        go_comment()
    else:
        driver.start_activity("com.simile.gifmaker", "com.yxcorp.gifshow.HomeActivity")
        go_ba_main()


def go_comment():
    if "PhotoDetailActivity" in driver.current_activity:
        swipe_util.swipe_up()
        time.sleep(0.5)
        el = driver.find_elements_by_name("说点什么...")
        if el:
            el[0].click()
        else:
            time.sleep(0.5)
            driver.keyevent(4)
            time.sleep(0.5)
            swipe_util.swipe_up()
            go_ba_main()

        el_edittexts = driver.find_elements_by_name("说点什么...")
        el_sends = driver.find_elements_by_name("发送")
        if el_edittexts and el_sends:
            el_edittexts[0].send_keys(get_send_str())
            el_sends[0].click()
        driver.keyevent(4)
        time.sleep(0.5)
        swipe_util.swipe_up()
        go_ba_main()
    else:
        driver.keyevent(4)
        go_ba_main()


if __name__ == '__main__':
    try:
        go_ba_main()
    except Exception as e:
        print(e)
    finally:
        driver.quit()
