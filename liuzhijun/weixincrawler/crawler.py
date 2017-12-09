# -*- coding: utf-8 -*-
__author__ = "liuzhijun"

import requests


def crawl():
    url = "https://mp.weixin.qq.com/mp/profile_ext" \
          "?action=home" \
          "&__biz=MjM5MzgyODQxMQ==" \
          "&scene=124&devicetype=android-24&version=26051633" \
          "&lang=zh_CN" \
          "&nettype=WIFI" \
          "&a8scene=3" \
          "&pass_ticket=MXADI5SFjXvX7DFPRuUEJhWHEWvRha2x1Re%2BoJkveUxIonMfnxY1kM9cOPmm6JRxs" \
          "&wx_header=1"

    headers = """
Host: mp.weixin.qq.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 7.0; M1 E Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN
x-wechat-uin: NTI1NDc3NTE4
x-wechat-key: b6f571a259216ac8d51aaa5003f0834cac6508e76c877091c89f4c762cb75c478076429b3bdf9b51980e7105b887eceaf23a2480871c5f08e6162d297f7bee4c6ce4a94b1591446f68db276ba0686991
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/sharpp,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: rewardsn=bfcf84efa5c0e2d0cc3b; wxtokenkey=bacede7644d9c17f50857845a11030d0b2cd3a03f466643202911d67d086fee4; wxuin=525477518; pass_ticket=MXADI5SFjXvX7DFPRuUEJhWHEWvRha2x1Re+oJkveUxIonMfnxY1kM9cOPmm6JRx; wap_sid2=CI7NyPoBElxwOS1rSVprUGpYUjYwdXduOUpDblZlY3RaUXIyaFhyODRzN2NRTkhrNS1ZazhfNzhNMkJhMUpkYnEteThMcG15MWVWNEFrSGJGTjE2Njg1czJzX2xSS1VEQUFBfjDLvY3RBTgNQJVO
Q-UA2: QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.5.22&TBSVC=43602&CO=BK&COVC=043632&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= M1E &RL=1080*1920&OS=7.0&API=24
Q-GUID: 0fd685fa8c515a30dd9f7caf13b788cb
Q-Auth: 31045b957cf33acf31e40be2f3e71c5217597676a9729f1b

    """
    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    data = extract_data(response.text)
    for item in data:
        print(item)


def extract_data(html_content):
    """
    从html页面中提取历史文章数据
    :param html_content 页面源代码
    :return: 历史文章列表
    """
    import re
    import html
    import json

    rex = "msgList = '({.*?})'"
    pattern = re.compile(pattern=rex, flags=re.S)
    match = pattern.search(html_content)
    if match:
        data = match.group(1)
        data = html.unescape(data)
        data = json.loads(data)
        articles = data.get("list")
        for item in articles:
            print(item)
        return articles


def headers_to_dict(headers):
    """
    将字符串
    '''
    Host: mp.weixin.qq.com
    Connection: keep-alive
    Cache-Control: max-age=
    '''
    转换成字典类型
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        h = h.strip()
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers


if __name__ == '__main__':
    crawl()
