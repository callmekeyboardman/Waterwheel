import os


# 获取当前文件所在的路径
def path():
    # 获取当前文件的绝对路径
    current_path = os.path.abspath(__file__)
    # 获取当前文件所在目录的路径
    return os.path.dirname(current_path)
