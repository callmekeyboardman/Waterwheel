import re


# 转换 财联社 的url，从 移动端地址转成 web 地址
# 示例输入：https://api3.cls.cn/share/article/1943407?sv=8.5.3&app=cailianpress&os=android
# 示例输出：https://www.cls.cn/detail/1943407
def convert_cls(url: str):
    match = re.search(r'/article/(\d+)', url)
    article_id = match.group(1)
    return "https://www.cls.cn/detail/" + article_id


if __name__ == '__main__':
    print(convert_cls("https://api3.cls.cn/share/article/1943407?sv=8.5.3&app=cailianpress&os=android"))
