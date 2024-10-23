# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: gen_captcha_v1.py
# @time: 2024/9/19 17:18
from datetime import datetime as dt
import requests
import urllib
import time

url_prefix = "http://passport.linekong.com/genRegRandom.do???????????="
start_cnt = 0
stop_cnt = start_cnt + 100
while True:
    # 时间格式: Thu Sep 19 2024 17:00:00 GMT 0800 (中国标准时间)
    url = url_prefix + dt.now().strftime("%a %b %d %Y %H:%M:%S") + " GMT 0800 (中国标准时间)"
    # 将url进行编码
    url = urllib.parse.quote(url, safe='/:?=&')
    print(url)
    # 下载图片
    response = requests.get(url)
    if response.status_code == 200:
        # 打开文件并写入图片数据
        with open(f'../../data/new_corpus/{start_cnt}.jpg', 'wb') as file:
            file.write(response.content)
        print(f"图片下载成功并保存为{start_cnt}.jpg")
        start_cnt += 1
    else:
        break
    if start_cnt > stop_cnt:
        break
    time.sleep(1)
