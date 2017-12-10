# -*- coding: utf-8 -*-

import requests
import re
import html
import json

import logging

import utils
from models import Post

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)



class WeiXinCrawler:
    def crawl_latest(self):
        """
        爬取最近10条数据
        :return:
        """

        url = "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MzgyODQxMQ==&devicetype=android-24&version=26051633&lang=zh_CN&nettype=WIFI&a8scene=7&pass_ticket=oZQqv0KR7zhxAix1SHUFLwI7p%2FiKH2NPWIdEmZidhitAOdpf873t%2BLEZU9Hnxx%2FT&wx_header=1"

        headers = """
Host: mp.weixin.qq.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 7.0; M1 E Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN
x-wechat-uin: NzYyMTk0MjA5
x-wechat-key: 975b1bc3eea469ca48adb5bdc7b380088863ee0cda506dfa74011ea3eb53607dabcca528e640c56c406259315cb4c7a8b357c0c790b9583c225d2279c17d0d596293d45d6d2e91567048a130eab6d080
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/sharpp,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: rewardsn=16d9a36f4e4e74794662; wxtokenkey=b19d70f2914f54856f9c62b7d8f1000ef682e08aef1686dad9b3e2a35cf1c96a; wxuin=762194209; devicetype=android-24; version=26051633; lang=zh_CN; pass_ticket=oZQqv0KR7zhxAix1SHUFLwI7p/iKH2NPWIdEmZidhitAOdpf873t+LEZU9Hnxx/T; wap_sid2=CKHSuOsCElx2bndhQnhwbVhpOVZaTFFnYWVvZnBXbld5elVsdnJwN1UxNWp5UVBKUWJVblZpV29VRlhRT1JyMjFsV3BtT2xFaFJwN2RmTUVQQWxDVl8yeXZBRmc4NllEQUFBfjCwmLXRBTgMQJRO
Q-UA2: QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.5.22&TBSVC=43602&CO=BK&COVC=043632&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= M1E &RL=1080*1920&OS=7.0&API=24
Q-GUID: 0fd685fa8c515a30dd9f7caf13b788cb
Q-Auth: 31045b957cf33acf31e40be2f3e71c5217597676a9729f1b
    
    
        """
        headers = utils.str_to_dict(headers)
        response = requests.get(url, headers=headers, verify=False)

        if '<title>验证</title>' in response.text:
            logging.error("无法正确获取内容，请用最新的请求参数和请求头替换headers")
            exit()

        data = self.extract_data(response.text)
        for item in data:
            keys = ('title', 'author', 'content_url', 'digest', 'cover', 'source_url')
            sub_data = utils.sub_dict(item.get("app_msg_ext_info"), keys)
            post = Post(**sub_data)
            logger.debug(post.to_json())
            post.save()

    def extract_data(self, html_content):
        """
        从html页面中提取历史文章数据
        :param html_content 页面源代码
        :return: 历史文章列表
        """

        rex = "msgList = '({.*?})'"
        pattern = re.compile(pattern=rex, flags=re.S)
        match = pattern.search(html_content)
        if match:
            data = match.group(1)
            data = html.unescape(html.unescape(data)).replace("\/", "/")
            logger.info("抓取数据： %s" % data)
            data = json.loads(data)
            articles = data.get("list")
            return articles
        else:
            return []


if __name__ == '__main__':
    crawler = WeiXinCrawler()
    crawler.crawl_latest()
