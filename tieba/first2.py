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
        el_items = driver.find_elements_by_id("com.baidu.tieba:id/pb_floor_item_layout")
        if el_items:
            if len(el_items) > 7:  # 大于7个 请求两次
                cylce_user_image(el_items)
                swipe_util.swipe_up()
                time.sleep(0.5)
                el_items = driver.find_elements_by_id("com.baidu.tieba:id/pb_floor_item_layout")
                time.sleep(0.5)
                cylce_user_image(el_items)
            else:  # 小于7个请求一次
                cylce_user_image(el_items)
            driver.keyevent(4)
            time.sleep(1)
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


def cylce_user_image(el_items):
    for i in range(len(el_items)):
        el_usernames = el_items[i].find_elements_by_id("com.baidu.tieba:id/view_user_name")
        el_user_images = el_items[i].find_elements_by_id("com.baidu.tieba:id/normal_user_photo")
        if el_usernames and el_user_images:
            if el_usernames[0] in users:
                continue
            else:
                el_user_images[0].click()
                go_user_detail()
        else:
            continue


def go_user_detail():
    if driver.current_activity == ".personPolymeric.PersonPolymericActivity":
        time.sleep(0.5)
        driver.tap([(624, 50)])
        go_chat()
    else:
        # driver.keyevent(4)
        # time.sleep(0.5)
        go_comment()


def go_chat():
    if driver.current_activity == ".imMessageCenter.im.chat.PersonalChatActivity":
        el_user_chat = driver.find_elements_by_id("com.baidu.tieba:id/img_msgitem_photo")
        if el_user_chat:
            users.add(driver.find_elements_by_id("com.baidu.tieba:id/personal_lbs_title_name")[0].text)
            driver.keyevent(4)
            time.sleep(0.5)
            driver.keyevent(4)
        else:
            el_edittext = driver.find_elements_by_class_name("android.widget.EditText")
            el_send = driver.find_elements_by_name("发送")
            if el_edittext and el_send:
                el_edittext[0].send_keys(get_send_str())
                el_send[0].click()
                users.add(driver.find_elements_by_id("com.baidu.tieba:id/personal_lbs_title_name")[0].text)
            driver.keyevent(4)
            time.sleep(0.5)
            driver.keyevent(4)
    else:
        driver.keyevent(4)
        go_user_detail()


if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print(e)
    finally:
        driver.quit()
