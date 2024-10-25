# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: gen_captcha_v2.py
# @time: 2024/10/23 13:35
from random import random
import requests
import urllib

url_prefix = "http://sec.yoka.com/checkcode/fetch_image.php?checkkey=455a50197d20d808150c11175430b037f178a5bf13e1e338561aea8ef3aa0068&1729670850436"
start_cnt = 0
stop_cnt = start_cnt + 3000
while True:
    url = url_prefix # + str(random())
    # 将url进行编码
    url = urllib.parse.quote(url, safe='/:?=&')
    # print(url)
    # 添加请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    # 下载图片
    response = requests.get(url, headers=headers)
    # print(response.text)
    if response.status_code == 200:
        # 打开文件并写入图片数据
        with open(f'../../data/4char_corpus/{start_cnt}.jpg', 'wb') as file:
            file.write(response.content)
        print(f"图片下载成功并保存为{start_cnt}.jpg")
        start_cnt += 1
        print(f"当前已下载{start_cnt}张图片")
    else:
        break
    if start_cnt > stop_cnt:
        break
