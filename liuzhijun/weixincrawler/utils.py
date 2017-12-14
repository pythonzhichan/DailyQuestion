import re


def sub_dict(data, keys):
    """
    获取字典对象的子字典
    :param data: 源字典
    :param keys: 需要提取key列表
    :return:dict
    """
    return {key: data[key] for key in data if key in keys}


def str_to_dict(s, join_symbol="\n", split_symbol=":"):
    """
    key与value通过split_symbol连接， key,value 对之间使用join_symbol连接
    例如： a=b&c=d   join_symbol是&, split_symbol是=
    :param s: 原字符串
    :param join_symbol: 连接符
    :param split_symbol: 分隔符
    :return: 字典
    """
    s_list = s.split(join_symbol)
    data = dict()
    for item in s_list:
        item = item.strip()
        if item:
            k, v = item.split(split_symbol, 1)
            data[k] = v.strip()
    return data


def extract_text(text, rex):
    """
    根据正则表达式提取文本
    :param text:  原文本
    :param rex: 正则
    :return:
    """

    pattern = re.compile(rex, re.S)
    match = pattern.search(text)
    if match:
        return match.groups()


def xx(s):
    return s.replace("&", "&\"\\\n\"")


if __name__ == '__main__':
    s = "__biz=MjM5MzgyODQxMQ==&appmsg_type=9&mid=2650367634&sn=ec23c954f7adad842d706c2ec687a35e&idx=1&scene=27&title=%E2%80%9C%E7%BD%91%E7%BA%A2%E2%80%9D%20%20Python%EF%BC%8C%08%E7%96%AF%E7%8B%82%E6%89%93%20call&ct=1513035896&abtest_cookie=AwABAAoADAANAAoAJIgeAEyIHgBiiB4A2ogeAPyIHgAOiR4Ab4keAPCJHgD4iR4AB4oeAAAA&devicetype=iOS10.3.3&version=/mmbizwap/zh_CN/htmledition/js/appmsg/index393966.js&f=json&r=0.4737616995159224&is_need_ad=1&comment_id=4200886237&is_need_reward=1&both_ad=0&reward_uin_count=27&msg_daily_idx=1&is_original=0&uin=777&key=777&pass_ticket=bh2aZVyo%25252ByUXTHI%25252B3G7VDrZTFJH7e41TRdHFcHjOjyqrCJe2rpXirBD4QSKU2maB&wxtoken=1082715157&devicetype=iOS10.3.3&clientversion=16060021&appmsg_token=935_ale1QIchYa5yhL23YfFID3P9orUrZgludl8x0DM-Kzji1H3GmguOr5xpUVCpsKh1G5EmVd2msa4m2dRq&x5=0&f=json"
    print(str_to_dict(s, join_symbol="&", split_symbol="="))