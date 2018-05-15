from appium import webdriver
import time, random
from appscript.bilin.config import get_send_str
from appscript.bilin.swipeutil import SwipeUtils

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.bilin.huijiao.activity'
desired_caps['appActivity'] = 'com.bilin.huijiao.ui.maintabs.MainActivity'
desired_caps["unicodeKeyboard"] = True,
desired_caps["resetKeyboard"] = True,
desired_caps["sessionOverride"] = True,
desired_caps["appWaitActivity"] = 'com.bilin.huijiao.ui.maintabs.MainActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

swipe_util = SwipeUtils(driver)

users = set()


def go_main():
    if "MainActivity" in driver.current_activity:
        el_zaixians = driver.find_elements_by_name("在线的人")
        if el_zaixians:
            el_zaixians[0].click()
            go_online()
        else:
            check_view()
    else:
        driver.start_activity("com.bilin.huijiao.activity", "com.bilin.huijiao.ui.maintabs.MainActivity")


is_last = None


def go_online():
    try:
        if "OnlineMoreActivity" in driver.current_activity:
            el_names = driver.find_elements_by_id("com.bilin.huijiao.activity:id/tv_nickname")
            global is_last
            if el_names:
                for el in el_names:
                    if el.text in users:
                        continue
                    else:
                        el.click()
                        time.sleep(0.5)
                        go_userinfo(el)
                print(is_last)
                print(el_names[0].text)
                if is_last == el_names[0].text:
                    driver.start_activity("com.bilin.huijiao.activity", "com.bilin.huijiao.ui.maintabs.MainActivity")
                    go_main()
                    return
                is_last = el_names[0].text
                swipe_util.swipe_up()
                time.sleep(2)
                swipe_util.swipe_up()
                go_online()
            else:
                check_view()
        else:
            check_view()
    except Exception as e:
        driver.start_activity("com.bilin.huijiao.activity", "com.bilin.huijiao.ui.maintabs.MainActivity")
        go_main()


def go_userinfo(name):
    try:
        if "AudioRoomActivity" in driver.current_activity:
            users.add(name)
            driver.keyevent(4)
            time.sleep(0.4)
            el_quit = driver.find_elements_by_id("com.bilin.huijiao.activity:id/ib_cfpoq_quit")
            if el_quit:
                el_quit[0].click()
        elif "FriendUserInfoActivity" in driver.current_activity:
            el_zhaohu = driver.find_elements_by_name("打招呼")
            if el_zhaohu:
                el_zhaohu[0].click()
                time.sleep(0.4)
                go_chat()
                driver.keyevent(4)

        elif "MyUserInfoActivity" in driver.current_activity:
            driver.keyevent(4)
        else:
            check_view()
    except Exception as e:
        driver.start_activity("com.bilin.huijiao.activity", "com.bilin.huijiao.ui.maintabs.MainActivity")
        go_main()


def go_chat():
    try:
        if "ChatActivity" in driver.current_activity:
            el_avatar = driver.find_elements_by_id("com.bilin.huijiao.activity:id/chat_item_avatar")
            el_tilte = driver.find_elements_by_id("com.bilin.huijiao.activity:id/actionbar_tv_title")
            if el_avatar:
                if el_tilte:
                    users.add(el_tilte[0].text)
                    driver.keyevent(4)
                    time.sleep(0.4)
                    driver.keyevent(4)
                    return
                else:
                    check_view()

            el_edittexts = driver.find_elements_by_name("输入想说的内容")
            if el_edittexts:
                el_edittexts[0].send_keys(get_send_str())
            else:
                check_view()
            el_sends = driver.find_elements_by_id("com.bilin.huijiao.activity:id/iv_action")
            if el_sends:
                el_sends[0].click()
                users.add(el_tilte[0].text)
            else:
                check_view()
            driver.keyevent(4)
            driver.back()
            time.sleep(2)
            driver.keyevent(4)
        else:
            check_view()
    except Exception as e:
        driver.start_activity("com.bilin.huijiao.activity", "com.bilin.huijiao.ui.maintabs.MainActivity")
        go_main()


def check_view():
    if "MainActivity" in driver.current_activity:
        go_main()
    elif "OnlineMoreActivity" in driver.current_activity:
        go_online()
    elif "FriendUserInfoActivity" in driver.current_activity:
        driver.keyevent(4)
        time.sleep(1)
        check_view()
    elif "ChatActivity" in driver.current_activity:
        driver.keyevent(4)
        time.sleep(1)
        check_view()
    else:
        driver.keyevent(4)
        time.sleep(1)
        check_view()


if __name__ == '__main__':
    try:
        go_main()
    except Exception as e:
        driver.start_activity("com.bilin.huijiao.activity", "com.bilin.huijiao.ui.maintabs.MainActivity")
        go_main()
