# !/usr/bin/env python3
# coding:utf-8
"""
@Author : Lucky Jason
@Email  : LuckyJasonone@gmail.com
@Description : 下载海报,拼接成小熊
@Starting time : 2020/7/9
@Completion time : null
"""
import os
from urllib import request
import threading
from PIL import Image
import numpy as np
import cv2
from spider import get_data, save_history
from urllib.error import URLError
import json
import sys


def download_one_picture(save_path):
    global image_urls
    global lock
    while True:
        lock.acquire()
        if len(image_urls) == 0:
            lock.release()
            return None
        else:
            filename = os.path.join(save_path, str(len(image_urls)) + '.jpg')
            url = image_urls.pop()
            lock.release()
            # 下载图片,保存本地
            try:
                request.urlretrieve(url, filename=filename)
            except URLError:
                print('ERROR:此海报下载失败，链接为{}'.format(url))


def download_picture(save_path=None):
    if not save_path:
        save_path = os.path.join(os.path.abspath('.'), "images")
    if not os.path.isdir(save_path):
        os.mkdir(save_path)
    threads = []
    for x in range(5):
        consumer = threading.Thread(target=download_one_picture, args=(save_path,))
        threads.append(consumer)
        consumer.start()
    # 等待所有线程结束
    for t in threads:
        t.join()
    return save_path


def get_rgb(img_path):
    """
    计算单张图片的平均rgb
    :param img_path:
    :return: <rgb:tuple>
    """
    img = cv2.imread(img_path, 1)
    r = int(np.mean(img[:, :, 0]))
    g = int(np.mean(img[:, :, 1]))
    b = int(np.mean(img[:, :, 2]))
    rgb = (r, g, b)
    return rgb


def mean_rbg(image):  # 计算图片平均rgb
    rgb = np.array(image)
    r = int(round(np.mean(rgb[:, :, 0])))
    g = int(round(np.mean(rgb[:, :, 1])))
    b = int(round(np.mean(rgb[:, :, 2])))
    return r, g, b


def most_suit_img(rgb, all_mean_rgb):
    """
    进行对比，找出最合适的海报
    :param rgb:
    :param all_mean_rgb:
    :return: <img_id:int>
    """
    min_range = 200000
    img_id = 0
    for i, one in enumerate(all_mean_rgb):
        tmp = (one[0] - rgb[2]) ** 2 + (one[1] - rgb[1]) ** 2 + (one[2] - rgb[1])
        if tmp < min_range:
            min_range = tmp
            img_id = i
    return img_id + 1


def create_bear_picture(images_path, mode_path, picture_size, little_size, all_mean_rgb):
    """

    :param images_path:
    :param mode_path:
    :param picture_size:
    :param little_size:
    :return:
    """
    row = picture_size[0]  # 每行多少个海报
    col = picture_size[1]  # 每列多少个海报
    suit_size = (little_size * row, little_size * col)  # 图片最终的像素size
    mode_img = Image.open(mode_path)
    mode_img = mode_img.resize(suit_size)
    picture = Image.new('RGBA', suit_size)

    for i in range(row):
        for j in range(col):
            # 模板剪切用于对比的某个区域
            cut_box = (i * little_size, j * little_size, (i + 1) * little_size, (j + 1) * little_size)
            cut_img = mode_img.crop(cut_box)

            tmp_rgb = mean_rbg(cut_img)
            img_id = most_suit_img(tmp_rgb, all_mean_rgb)

            img = Image.open(os.path.join(images_path, '{}.jpg'.format(img_id))).convert('RGBA')
            img = img.resize((little_size, little_size))
            picture.paste(img, cut_box)

    picture.save("result.png")


if __name__ == '__main__':
    # 获取数据
    data = get_data()

    # 保存数据
    path = save_history(data)
    print("数据保存在{}目录下.".format(path))

    # 下载海报
    image_urls = []
    for history in data["观看历史"]:
        image_urls.append(history["image_url"])
    lock = threading.Lock()
    image_path = download_picture()

    # 下载用户头像
    request.urlretrieve(data['用户头像'], filename=os.path.join(os.path.abspath('.'), "portrait.jpg"))

    # 拼接小熊
    cur_path = os.path.abspath('.')
    images_path = os.path.join(cur_path, 'images')
    mode_path = os.path.join(cur_path, 'bear.jpg')
    num = 105 // 5
    picture_size = (num, num)
    little_size = 1600 // num
    all_mean_rgb = []
    for img in os.listdir(images_path):
        img_path = os.path.join(images_path, img)
        all_mean_rgb.append(get_rgb(img_path))
    create_bear_picture(images_path, mode_path, picture_size, little_size, all_mean_rgb)
