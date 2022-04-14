#! /usr/bin/python3
# encoding = utf-8
import requests
from bs4 import BeautifulSoup


def login():
    """
    模拟WakaTime登录流程，登录需要两步先获取csrftoken字段，登录模拟时发送该字段过去
    :return:
    """
    login_url = 'https://wakatime.com/login'
    proxies = {
        "http": "http://192.168.0.166:3128",
        "https": "http://192.168.0.166:3128"
    }
    headers = {
        'method': 'GET',
        'path': '/login',
        'scheme': 'https',
        'authority': 'wakatime.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip,deflate,br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    print("获取必要的登录参数ing....")
    login_content = requests.get(login_url, headers=headers, proxies=proxies)
    login_soup = BeautifulSoup(login_content.content, 'html.parser')
    login_form_horizontal = login_soup.select(".form-horizontal")[0]
    crsf_token = login_form_horizontal.input.get("value")
    login_headers = {
        'authority': 'wakatime.com',
        'method': 'POST',
        'path': '/login',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh - CN, zh;q = 0.9',
        'cache-control': 'max - age = 0',
        'content-length': '93',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://wakatime.com',
        'referer': 'https://wakatime.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0(WindowsNT6.1;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome / 63.0.3239.132Safari / 537.36'
    }
    user_email = '323@qq.com'
    user_password = '1232132'
    data = {
        'csrftoken': crsf_token,
        'email': user_email,
        'password': user_password
    }
    cookies = requests.utils.dict_from_cookiejar(login_content.cookies)
    print("模拟登录ing....")
    login_after_content = requests.post(login_url, proxies=proxies, headers=login_headers, data=data, cookies=cookies)
    login_after_soup = BeautifulSoup(login_after_content.content, 'html.parser')
    print(login_after_soup.select("#flash-error"))

if __name__ == '__main__':
    login()

"""
WakaTime 登录流程模拟
1. 获取csrftoken
请求方法：get
请求头
:authority:wakatime.com
:method:GET
:path:/login
:scheme:https
accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding:gzip, deflate, br
accept-language:zh-CN,zh;q=0.9
upgrade-insecure-requests:1
user-agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36


2. 模拟登录  带session
请求方法：post
请求头
:authority:wakatime.com
:method:POST
:path:/login
:scheme:https
accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding:gzip, deflate, br
accept-language:zh-CN,zh;q=0.9
cache-control:max-age=0
content-length:93
content-type:application/x-www-form-urlencoded
cookie:csrftoken=6d8f2398efbd82691f8427c464ecd15972e7526b; session=.eJwFwU0OgyAQBtC7fGs2UuTvMqTCTDWlkszIynj3vnejsJDuyPzuSgZVha_xpRMZvkW2rxSJtxatTwtHZ0N13lFty5qCpbBav8FgyPEpQkwiJMjn7N1gXr-iY0olRb6f5w9x_yOX.DVBbhQ.AhQNMLBDLxc-Tt7V16gT8fwN9v0
origin:https://wakatime.com
referer:https://wakatime.com/
upgrade-insecure-requests:1
user-agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36

data：
csrftoken=6d8f2398efbd82691f8427c464ecd15972e7526b&email=25985%40qq.com&password=8888888
"""