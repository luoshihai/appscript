from appium import webdriver
import time, random
from tieba.config import get_send_str
from tieba.swipeutil import SwipeUtils

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.baidu.tieba'
desired_caps['appActivity'] = 'com.baidu.tieba.tblauncher.MainTabActivity'
desired_caps["unicodeKeyboard"] = True,
desired_caps["resetKeyboard"] = True,

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

swipe_util = SwipeUtils(driver)

users = set()


def start():
    if driver.current_activity == ".tblauncher.MainTabActivity":
        pass
    else:
        driver.start_activity("com.baidu.tieba", "com.baidu.tieba.tblauncher.MainTabActivity")
    time.sleep(2)
    driver.find_element_by_name("进吧").click()
    driver.find_element_by_name("双色球").click()
    go_ba_main()


def go_ba_main():
    if driver.current_activity == ".frs.FrsActivity":
        el_normal_roots = driver.find_elements_by_id("com.baidu.tieba:id/card_home_page_normal_thread_root")
        if el_normal_roots:
            el_comments = el_normal_roots[0].find_elements_by_id("com.baidu.tieba:id/thread_info_commont_container")
            if el_comments:
                el_comments[0].click()
                go_comment()
            else:
                swipe_util.swipe_up()
                go_ba_main()
        else:
            swipe_util.swipe_up()
            go_ba_main()
    else:
        start()


def go_comment():
    if driver.current_activity == ".pb.pb.main.PbActivity":
        time.sleep(0.5)
        el_tem = driver.find_elements_by_name("说说你的看法…")
        if el_tem:
            el_tem[0].click()
            el_edittexts = driver.find_elements_by_name("说说你的看法…")
            el_sends = driver.find_elements_by_name("发布")
            if el_edittexts and el_sends:
                el_edittexts[0].send_keys(get_send_str())
                el_sends[0].click()
            driver.keyevent(4)
            time.sleep(0.5)
            swipe_util.swipe_up()
            go_ba_main()
        else:
            driver.keyevent(4)
            time.sleep(0.5)
            swipe_util.swipe_up()
            go_ba_main()

    else:
        driver.keyevent(4)
        time.sleep(0.5)
        swipe_util.swipe_up()
        go_ba_main()



if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print(e)
    finally:
        driver.quit()
