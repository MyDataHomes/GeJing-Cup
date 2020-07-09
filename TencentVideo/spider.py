#!/usr/bin/env python3
# coding:utf-8
"""
@Author : Lucky Jason
@Email  : LuckyJasonone@gmail.com
@Description : main.py
@Starting time : 2020/7/8
@Completion time : null
"""
import time
import json
import re
import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions


def get_data():
    """
    使用selenium获取观看历史和用户名
    :return: <data:dict>
    """
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(options=option)

    # 用户登录(默认驱动文件已经配置到了环境变量中)
    driver.get('https://v.qq.com/biu/u/history/')

    # 轮询检测,登录是否成功
    while True:
        time.sleep(0.2)
        num = len(driver.get_cookies())
        if num > 16:  # 数量不定,一般为9-15个,超过16个则一定有登录成功的cookie存在
            break

    # 取消过滤已看完
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/span[1]').click()

    # 调用js,刷新页面吗,使观看历史全部显示
    js_get_height = "return action=document.body.scrollHeight"
    while True:
        height = driver.execute_script(js_get_height)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        if height == driver.execute_script(js_get_height):
            break

    # 获取用户名和头像
    name = driver.find_element_by_xpath('//*[@id="side_nav"]/div[1]/div[2]/span').text
    portrait_url = driver.find_element_by_xpath('//*[@id="side_nav"]/div[1]/div[1]/img').get_property('src')

    # 获取观看历史,并关闭浏览器
    items = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[2]/div')
    history = []
    for item in items:
        innerHTML = item.get_attribute('innerHTML')
        pattern = r'.*?src="(?P<image_url>.*?)".*?title="(?P<drama_name>.*?)".*?<span>(?P<played>.*?)</span>'
        result = re.search(pattern, innerHTML, re.S)
        if result:
            history.append({
                'drama_name': result.group('drama_name'),
                'image_url': 'https:' + result.group('image_url'),
                'played': result.group('played')
            })
    driver.quit()
    return {
        "用户名": name,
        "用户头像": portrait_url,
        "观看历史": history,
    }


def save_history(history):
    """
    格式化输出到json文件
    :param history: <dict>
    :return: <dir_path:str>
    """
    dir_path = os.path.join(os.path.abspath('.'), "data")
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    with open(os.path.join(dir_path, "data.json"), "w", encoding='utf-8') as f:
        json.dump(history, f, indent=2, sort_keys=True, ensure_ascii=False)
    return os.path.join(dir_path, "data.json")


# def get_picture(data):
#     portrait_url = data["用户头像"]
#     image_urls = []
#     for history in data["观看历史"]:
#         image_urls.append(history["image_url"])
