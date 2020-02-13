# -*- coding:utf-8 -*-
# import json
# str = '{"cities": ["深圳", "广州"]}'
# str = json.loads(str)
# print(type(str))
# print(str)
# lists = str.get('cities')
# print(lists)
# ===========================================================
import requests
import re

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
# url = 'https://www.baidu.com/s?wd=103.225.206.22'
# resp = requests.get(url, headers=headers)
# text = resp.text
# area = re.findall(r'<span class="c-gap-right">IP地址:.*?</span>(.*?)</td>', text, re.DOTALL)[0]
# print(area)
# =============================================================
# import time
# import eventlet  # 导入eventlet这个模块
# eventlet.monkey_patch()   # 必须加这条代码
# with eventlet.Timeout(2, False):   # 设置超时时间为2秒
#    print('这条语句正常执行')
#    time.sleep(4)
#    print('没有跳过这条输出')
# print('跳过了输出')
# ==============================================================
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# path = os.path.join(BASE_DIR, 'db.sqlite3')
# print(os.path.exists(path))
#
# ==============================================================

