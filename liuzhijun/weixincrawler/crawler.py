# -*- coding: utf-8 -*-

import html
import json
import logging
import re
import time
from urllib.parse import urlsplit

import requests

import utils
from models import Post

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


class WeiXinCrawler:
    def crawl_latest_10(self):
        """
        爬取最近10条数据
        :return:
        """

        url = "https://mp.weixin.qq.com/mp/profile_ext?" \
              "action=home&" \
              "__biz=MjM5MzgyODQxMQ==&" \
              "devicetype=android-24&" \
              "version=26051633&" \
              "lang=zh_CN&" \
              "nettype=WIFI&" \
              "a8scene=7&" \
              "pass_ticket=oZQqv0KR7zhxAix1SHUFLwI7p%2FiKH2NPWIdEmZidhitAOdpf873t%2BLEZU9Hnxx%2FT&" \
              "wx_header=1"

        headers = """
Host: mp.weixin.qq.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 5.1.1; 2014813 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN
x-wechat-uin: NTI1NDc3NTE4
x-wechat-key: c37a3f1c3525d70e6537599058680a1c1d38d754815c6f101c7bf3fbc5bbcd19f8c54895c965c0d624b36d11da34033eb5109c5e40524df3109f43943505a19d0b3f68bacb0b77cbae35a251a1722f98
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/sharpp,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: rewardsn=1872e6d4042552713dff; wxtokenkey=990d7740963fdbea6cf44ba78c4166b7f9025262edc22a0977c781f8073b54aa; wxuin=525477518; devicetype=android-22; version=26051731; lang=zh_CN; pass_ticket=wxW7ApnFNe01tZe42nkIH5EExbK+YA45O1NzaLk7uLZBPks8RzUA4gzD6hxU9V5n; wap_sid2=CI7NyPoBElxldXVmX1B4VVVJbXdNTnh4SDZ2YXlMcURDWENucDhvWmZoMktqRmQzYWJVRXV6b29TYmJWX2VscG4zekh2ZzVxWVhmcGpraDBLUEg3LTZZNmNXYXl2S1lEQUFBfjCQmMPRBTgMQJRO
Q-UA2: QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.5.23&TBSVC=43602&CO=BK&COVC=043632&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= 2014813 &RL=720*1280&OS=5.1.1&API=22
Q-GUID: 9d4417681f44eeb4410b613d13b788cb
Q-Auth: 31045b957cf33acf31e40be2f3e71c5217597676a9729f1b


    
        """
        headers = utils.str_to_dict(headers)
        response = requests.get(url, headers=headers, verify=False)

        if '<title>验证</title>' in response.text:
            logger.error("无法正确获取内容，请重新获取请求参数和请求头")
            exit()

        rex = "msgList = '({.*?})'"
        pattern = re.compile(pattern=rex, flags=re.S)
        match = pattern.search(response.text)
        if match:
            msg_list = match.group(1)
            logger.info("抓取数据： %s" % msg_list)
            msg_list = html.unescape(html.unescape(msg_list))
            self.save(msg_list)
        else:
            logger.warning("没有找到匹配的数据")

    def crawl_more(self, offset=0):
        """
        爬取更多文章
        :return:
        """
        url = "https://mp.weixin.qq.com/mp/profile_ext?" \
              "action=getmsg&" \
              "__biz=MjM5MzgyODQxMQ==&" \
              "f=json&" \
              "offset={offset}&" \
              "count=10&" \
              "is_ok=1&" \
              "scene=&" \
              "uin=777&" \
              "key=777&" \
              "pass_ticket=lDUqy%2FK9AFwZZVe8RDrxTER0kM1SAjDpAhfBgj2bW4QyP8V2lsi9gMbN%2FTJ0Nq7w&" \
              "wxtoken=&" \
              "appmsg_token=935_GxAo%2BiWnvCj80gcRR5iWbvAetsVErB5CLhSNJg~~&" \
              "x5=1&" \
              "f=json".format(offset=offset)  # appmsg_token 也是临时的

        headers = """
Host: mp.weixin.qq.com
Connection: keep-alive
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Linux; Android 5.1.1; 2014813 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN
Accept: */*
Referer: https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzIwMTc4ODE0Mw==&devicetype=android-22&version=26051731&lang=zh_CN&nettype=WIFI&a8scene=7&session_us=gh_5138cebd4585&pass_ticket=wxW7ApnFNe01tZe42nkIH5EExbK%2BYA45O1NzaLk7uLZBPks8RzUA4gzD6hxU9V5n&wx_header=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: rewardsn=1872e6d4042552713dff; wxtokenkey=990d7740963fdbea6cf44ba78c4166b7f9025262edc22a0977c781f8073b54aa; wxuin=525477518; devicetype=android-22; version=26051731; lang=zh_CN; pass_ticket=wxW7ApnFNe01tZe42nkIH5EExbK+YA45O1NzaLk7uLZBPks8RzUA4gzD6hxU9V5n; wap_sid2=CI7NyPoBElxNWnRoazhJNk5CQkdYQ3NBRXZBNmVYbDVncS1yVkdsVjFQYUpCU3J6UGZ1WmxubC1wT3p4WkE4ZFY0dnRpaDdlZnJ1ank4dkdZbXpnNUd2V2hpbjNQS2NEQUFBfjCimMPRBTgMQJRO
Q-UA2: QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.5.23&TBSVC=43602&CO=BK&COVC=043632&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= 2014813 &RL=720*1280&OS=5.1.1&API=22
Q-GUID: 9d4417681f44eeb4410b613d13b788cb
Q-Auth: 31045b957cf33acf31e40be2f3e71c5217597676a9729f1b




        """
        headers = utils.str_to_dict(headers)
        response = requests.get(url, headers=headers, verify=False)
        result = response.json()
        if result.get("ret") == 0:
            msg_list = result.get("general_msg_list")
            logger.info("抓取数据：offset=%s, data=%s" % (offset, msg_list))
            self.save(msg_list)
            # 递归调用
            has_next = result.get("can_msg_continue")
            if has_next == 1:
                next_offset = result.get("next_offset")
                # TODO 等待时间做成可配置
                time.sleep(2)
                self.crawl_more(next_offset)
        else:
            # 错误消息
            # {"ret":-3,"errmsg":"no session","cookie_count":1}
            logger.error("无法正确获取内容，请重新获取请求参数和请求头")
            exit()

    @staticmethod
    def save(msg_list):
        """
         msg_list 是字符串
        "{\"list\":[{\"comm_msg_info\":{\"id....
        还需要经过字符反转义后，再用json转换成字典
        """
        # TODO 处理多图文 multi_app_msg_item_list
        msg_list = msg_list.replace("&quot;", "\\\"").replace("\/", "/")
        data = json.loads(msg_list)
        posts = data.get("list")
        for item in posts:
            msg_info = item.get("app_msg_ext_info")
            if msg_info:
                keys = ('title', 'author', 'content_url', 'digest', 'cover', 'source_url')
                sub_data = utils.sub_dict(item.get("app_msg_ext_info"), keys)
                post = Post(**sub_data)
                logger.info('save data %s ' % post.title)
                try:
                    post.save()
                except Exception as e:
                    logger.error("保存失败 data=%s" % post.to_json(), exc_info=True)
            else:
                logger.warning(u"此消息不是图文推送，data=%s" % json.dumps(item.get("comm_msg_info")))

    def comments(self):
        url = "https://mp.weixin.qq.com/mp/appmsg_comment?" \
              "action=getcomment&" \
              "scene=0&" \
              "__biz=MjM5MzgyODQxMQ==&" \
              "appmsgid=2650367634&idx=1&" \
              "comment_id=4200886237&" \
              "offset=0&" \
              "limit=100&" \
              "uin=777&" \
              "key=777&" \
              "pass_ticket=wxW7ApnFNe01tZe42nkIH5EExbK%25252BYA45O1NzaLk7uLZBPks8RzUA4gzD6hxU9V5n&" \
              "wxtoken=772433544&" \
              "devicetype=android-22&" \
              "clientversion=26051731&" \
              "appmsg_token=935_y3k7aPYswY7Sxv5NfnJQ5P3s7pyh0cCESH2HBO6tiDh-AT2w546J0z2TWJSUNeRHZ5jZ4VP1ACqFq58R&x5=1&" \
              "f=json"

    def detail(self, article_url):
        # 文章链接
        article_url = "https://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&" \
                      "mid=2650367634&" \
                      "idx=1&" \
                      "sn=ec23c954f7adad842d706c2ec687a35e&" \
                      "chksm=be9cddc689eb54d07cd27f260f8ce7bf48d5702dc59a7f9b32725a7fd02d8b4a34f58382e4f5&" \
                      "scene=0&" \
                      "ascene=7&" \
                      "devicetype=android-22&" \
                      "version=26051731&" \
                      "nettype=WIFI&" \
                      "abtest_cookie=AwABAAoADAANAAkAJIgeALuIHgDZiB4A4YgeAPyIHgANiR4A74keAPqJHgAJih4AAAA%3D&" \
                      "lang=zh_CN&" \
                      "pass_ticket=wxW7ApnFNe01tZe42nkIH5EExbK%2BYA45O1NzaLk7uLZBPks8RzUA4gzD6hxU9V5n&" \
                      "wx_header=1"

        header = """
Host: mp.weixin.qq.com
Cookie: devicetype=iOS10.3.3; lang=zh_CN; pass_ticket=bh2aZVyo+yUXTHI+3G7VDrZTFJH7e41TRdHFcHjOjyqrCJe2rpXirBD4QSKU2maB; version=16060021; wap_sid2=CIDUopEDElxKMk5jQVZpM3lWd3RVQXVZYmV1QVA5Z3l3d3hWdFJGQzNhV3BuU2VxOEN2NEtyaVQ5QVlIc2FMVFZlV1VRRnJlZzZyTjlXNHU0MWFpcFpkUHI5R21GYWNEQUFBfjDYhMnRBTgMQJRO; wxuin=841525760; wxtokenkey=a401a4f12436d7404b2488792b57e05efdb4a67082b39db7405eaf1b43d8bd79; ua_id=seRYVLVNcjYoZPzpAAAAACA8ySAXhkrd89FL3uvLbt8=; _scan_has_moon=1; pt2gguin=o0253421576; ptcz=3d9558280f480d9453cc13b78b32059793c778a1e8aa723ce7b2f5e9744f606b; pgv_pvid=7330882815; pgv_pvi=8857346048; sd_cookie_crttime=1510571099034; sd_userid=34241510571099034; pvid=6161617834; RK=7JMfU7Y+Gq
X-WECHAT-KEY: 63f29c76b0873f93d1e09f3041a4fee49f792cb4ccca7588574e6f054f357a611cacf9e5787641eae77bc1fd78d80f5c713d53a79e144091a768ec05fcf75e3ba88681ccaa05fdba037fc9b60cc2f86a
X-WECHAT-UIN: ODQxNTI1NzYw
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN
Accept-Language: zh-cn
Accept-Encoding: gzip, deflate
Connection: keep-alive





        """

        print(article_url)
        response = requests.get(article_url, headers=utils.str_to_dict(header))
        print(response.text)
        appmsg_token, = utils.extract_text(response.text, r"appmsg_token.*?\"(\S+)\"")
        print(appmsg_token)
        response.text

        import urllib
        print(urllib.parse.urlsplit(article_url).query)
        article_url = "http://mp.weixin.qq.com/s?" \
                      "__biz=MjM5MzgyODQxMQ==&" \
                      "mid=2650367644&idx=1&sn=9951edf4e9bfebcdaa7dd66a639befea&chksm=be9cddc889eb54de36a00865dcd15f9cf906d1868430dd62f1fe550b55e713b333344811e717&scene=27#wechat_redirect"
        data_url = "https://mp.weixin.qq.com/mp/getappmsgext"

        data_url = "https://mp.weixin.qq.com/mp/getappmsgext"
        # appmsg_token = "935_NOFCGGSMbypif53YGURwVY2zSD6xcJ6N_0kYBbA3uOc7G6f172hKMrEYEuF2aoAgCZfZqy2vfiqpaOKH"

        data_param = {'__biz': 'MjM5MzgyODQxMQ==',
                      'appmsg_type': '9',
                      'mid': '2650367644',  # 可能是微信文章ID
                      'sn': '9951edf4e9bfebcdaa7dd66a639befea',
                      'idx': '1', 'scene': '27',
                      'ct': '1513035896',
                      'abtest_cookie': 'AwABAAoADAANAAoAJIgeAEyIHgBiiB4A2ogeAPyIHgAOiR4Ab4keAPCJHgD4iR4AB4oeAAAA',
                      'devicetype': 'iOS10.3.3', 'version': '/mmbizwap/zh_CN/htmledition/js/appmsg/index393966.js',
                      'f': 'json',
                      'r': '0.4737616995159224', 'is_need_ad': '1', 'comment_id': '4200886237', 'is_need_reward': '1',
                      'both_ad': '0', 'reward_uin_count': '27', 'msg_daily_idx': '1', 'is_original': '0', 'uin': '777',
                      'key': '777',
                      'pass_ticket': 'bh2aZVyo%25252ByUXTHI%25252B3G7VDrZTFJH7e41TRdHFcHjOjyqrCJe2rpXirBD4QSKU2maB',
                      'wxtoken': '1082715157', 'clientversion': '16060021',
                      'appmsg_token': '935_ale1QIchYa5yhL23YfFID3P9orUrZgludl8x0DM-Kzji1H3GmguOr5xpUVCpsKh1G5EmVd2msa4m2dRq',
                      'x5': '0'}

        # data_param = {
        #     'appmsg_type': '9',
        #     #   'abtest_cookie': 'AwABAAoADAANAAkAJIgeALuIHgDZiB4A4YgeAPyIHgANiR4A74keAPqJHgAJih4AAAA=',
        #     'f': 'json',
        #     'r': '0.6902087163157813',
        #     'is_need_reward': '1',
        #     'both_ad': '0',
        #     'reward_uin_count': '24',
        #     'msg_daily_idx': '1',
        #     'is_original': '0',
        #     'uin': '777',
        #     'clientversion': '26051731',
        #     'appmsg_token': appmsg_token,
        #     'x5': '1'}

        # article_param = utils.str_to_dict(urlsplit(article_url).query, "&", "=")
        # data_param.update(article_param)

        body = "is_only_read=1&req_id=1412MureIWcNGlE3ILXVOGp2&" \
               "pass_ticket={pass_ticket}".format(pass_ticket=data_param.get("pass_ticket"))

        headers = """

Host: mp.weixin.qq.com
Accept: */*
X-Requested-With: XMLHttpRequest
Accept-Language: zh-cn
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://mp.weixin.qq.com
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN
Connection: keep-alive
Referer: https://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650367634&idx=1&sn=ec23c954f7adad842d706c2ec687a35e&chksm=be9cddc689eb54d07cd27f260f8ce7bf48d5702dc59a7f9b32725a7fd02d8b4a34f58382e4f5&scene=27&ascene=7&devicetype=iOS10.3.3&version=16060021&nettype=WIFI&abtest_cookie=AwABAAoADAANAAoAJIgeAEyIHgBiiB4A2ogeAPyIHgAOiR4Ab4keAPCJHgD4iR4AB4oeAAAA&lang=zh_CN&fontScale=100&pass_ticket=bh2aZVyo%2ByUXTHI%2B3G7VDrZTFJH7e41TRdHFcHjOjyqrCJe2rpXirBD4QSKU2maB&wx_header=1
Content-Length: 149
Cookie: devicetype=iOS10.3.3; lang=zh_CN; pass_ticket=bh2aZVyo+yUXTHI+3G7VDrZTFJH7e41TRdHFcHjOjyqrCJe2rpXirBD4QSKU2maB; version=16060021; wap_sid2=CIDUopEDElxKMk5jQVZpM3lWd3RVQXVZYmV1QVA3TUdNVktTLVVrQTV4Q3dRWkI4Vkh5aXJKbDBsZlM1ZEFlWS1IWnpqWl8wQzhoeUtZR0xRQXh3ZHB1d3IwRDVMS2NEQUFBfjDihMnRBTgNQAE=; wxtokenkey=a733e2774b3089c814379cad23098030c1568e435e09146d5595c8a044f1770b; wxuin=841525760; ua_id=seRYVLVNcjYoZPzpAAAAACA8ySAXhkrd89FL3uvLbt8=; _scan_has_moon=1; pt2gguin=o0253421576; ptcz=3d9558280f480d9453cc13b78b32059793c778a1e8aa723ce7b2f5e9744f606b; pgv_pvid=7330882815; pgv_pvi=8857346048; sd_cookie_crttime=1510571099034; sd_userid=34241510571099034; pvid=6161617834; RK=7JMfU7Y+Gq







        """
        headers = utils.str_to_dict(headers)
        response = requests.post(data_url, headers=headers, data=body, params=data_param, verify=False)
        result = response.json()
        print(result)


if __name__ == '__main__':
    crawler = WeiXinCrawler()
    crawler.detail(None)
    # crawler.crawl_latest_10()
    # crawler.crawl_more()
