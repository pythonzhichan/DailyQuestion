def sub_dict(data, keys):
    """
    获取字典对象的子字典
    :param data: 源字典
    :param keys: 需要提取key列表
    :return:dict
    """
    return {key: data[key] for key in data if key in keys}


def str_to_dict(headers):
    """
    将"Host: mp.weixin.qq.com"格式的字符串转换成字典类型
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
