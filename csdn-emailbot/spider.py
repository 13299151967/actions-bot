#!/bin/python
#Coding="utf-8"
import requests
import time


def spider():
    click_url = 'https://88697c.asia/Plan/autoStatus'
    log_url = 'https://88697c.asia/Plan/doLogin'
    data = {'username': 'dy1396',
            'passwd': 'a12345'}
    headers_log = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.100 Safari/537.36 '

    }  # 加入请求头
    response = requests.post(log_url, data=data, headers=headers_log)
    if response.text == '1':
        print('登录成功')
    else:
        print(response)
    click_data = {'status': '1',
                  'rtype': '762',
                  'typename': '幸运赛车'}
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.100 Safari/537.36 '
        , 'Cookie': response.headers['set-cookie']
    }  # 加入请求头
    count = 0
    while True:
        res = requests.post(click_url, data=click_data, headers=headers)
        count = count + 1
        print(res.text, '请求次数', count)
        time.sleep(0.65)
        if res.text == '1':
            print('状态已修改')
            break


if __name__ == '__main__':
    spider()


