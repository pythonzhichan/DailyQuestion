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
    s = "__biz=MjM5MzgyODQxMQ==&mid=2650367644&idx=1&sn=9951edf4e9bfebcdaa7dd66a639befea&chksm=be9cddc889eb54de36a00865dcd15f9cf906d1868430dd62f1fe550b55e713b333344811e717&scene=27#wechat_redirect"
    print(str_to_dict(s, join_symbol="&", split_symbol="="))