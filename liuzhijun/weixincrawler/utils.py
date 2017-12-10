def sub_dict(data, keys):
    """
    获取字典对象的子字典
    :param data: 源字典
    :param keys: 需要提取key列表
    :return:dict
    """
    return {key: data[key] for key in data if key in keys}
