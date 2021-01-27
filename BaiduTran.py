"""
百度翻译api
"""
# /usr/bin/env python
# coding=utf8

import json
import http.client  # 修改引用的模块
import hashlib  # 修改引用的模块
from urllib import parse
import random


def translation(content):
    """
    调用百度翻译api的翻译模块
    :param content:
    :return:
    """
    appid = '20180228000128863'  # 你的appid
    secretKey = 'J2QqfxFcfCD7uGcAU_UX'  # 你的密钥

    url = '/api/trans/vip/translate'
    q = content
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)

    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    url = url + '?appid=' + appid + '&q=' + parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
    httpClient = None
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', url)
        response = httpClient.getresponse()

        # 转码
        html = response.read().decode('utf-8')
        html = json.loads(html)
        dst = html["trans_result"][0]["dst"]
        return dst
    except Exception as e:
        return e
    finally:
        if httpClient:
            httpClient.close()


if __name__ == '__main__':
    translation("hello")
