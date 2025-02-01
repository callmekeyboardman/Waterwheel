# JSON 操作工具类

import json


# 从JSON字符串转换成对象
def read(json_str):
    return json.loads(json_str)


def get_value_from_json_str(json_str, name):
    """
    从JSON字符串转换成对象，并取出指定的值
     INPUT:
     json_str: JSON字符串
     name:要取出的变量名

     OUTPUT:
     变量名的值
    """
    obj = json.loads(json_str)
    if obj is not None:
        return obj[name]
    else:
        return None


# 把对象转换成JSON字符串
def write(obj):
    """
    把对象转换成JSON字符串
     INPUT:
     obj: 对象

     OUTPUT:
     JSON字符串
    """
    return json.dumps(obj, ensure_ascii=False)


def load_json_file(path):
    """
    从json文件中，读取json对象
     INPUT:
     path: json文件路径

     OUTPUT:
     JSON中的对象
    """
    with open(path, 'r', encoding="utf-8", errors='ignore') as f:
        data = json.load(f)
        return data
