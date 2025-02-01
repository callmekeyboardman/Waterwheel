# 是否是 居民消费价格指数
def is_cpi1(code):
    return code == 'A01010G01'


# 不包括食品和能源居民消费价格指数
def is_cpi2(code):
    return code == 'A01010G0D'
