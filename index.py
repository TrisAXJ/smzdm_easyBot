#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Desc: 本脚本用于smzdm签到
API： 
GET https://zhiyou.smzdm.com/user/checkin/jsonp_checkin?callback=jQuery1124017478852004010437_1631422603307&_=1631422603315

'''

import requests
import time
import json
import random

banner = f'''
    +----------------------------------------------------------------+
    |                        smzdm simple bot                        |
    +----------------------------------------------------------------+
    Project      : smzdm simple bot
    Author       : trisaxj
    ------------------------------------------------------------------'''

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Referer": "https://www.smzdm.com/",
    "Cookie": "******",  # ***替换为你的cookie
}

# 签到
def smzdm_sign_in():
    try:
        url = "https://zhiyou.smzdm.com/user/checkin/jsonp_checkin"
        params = {
            "callback": "myCalback",
            "_": int(time.time()*1000)
        }
        
        # 发送一个get请求
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding

        # 由于返回的是JSONP数据，所以不能用response.json()来解析
        content = response.text
        # 截取JSONP中的JSON数据
        data = json.loads(content[content.find("{"):content.rfind(")")])

        if data.get("error_code") == 0:
            print("张大妈签到成功！！！总签到天数：", data.get("data").get("checkin_num"))
        else:
            print("签到失败，原因：", data.get("error_msg"))
    except Exception as e:
        print("张大妈签到出现错误；", e)

def main():
    print(banner)
    time.sleep(3)
    t = random.randint(5,60)
    print('Sleep {time} s...'.format(time = t))
    time.sleep(t)
    print("-------------------张大妈签到开始-------------------")
    smzdm_sign_in()
    print("-------------------张大妈签到结束-------------------")

def main_handler(event, context):
    main()

'''
if __name__ == "__main__":
    main()
'''