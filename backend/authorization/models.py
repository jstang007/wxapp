# -*- encoding=utf8 -*-


from django.db import models


class User(models.Model):
    # 微信的openid是长度为32的字符串
    open_id = models.CharField(max_length=32, unique=True)
    # 用户名
    nickname = models.CharField(max_length=256)
    # 关注的城市
    focus_cities = models.TextField(default='[]')
    # 关注的星座
    focus_constellations = models.TextField(default='[]')
    # 关注的股票
    focus_stocks = models.TextField(default='[]')
