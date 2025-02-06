# 居民消费价格指数
def is_cpi1(value):
    return value == 'A01010G01' or value == '居民消费价格指数'


# 不包括食品和能源居民消费价格指数
def is_cpi2(value):
    return value == 'A01010G0D' or value == '不包括食品和能源居民消费价格指数'

# 黄金储备
def is_gold(value):
    return value == 'A0L0401' or value == '黄金储备'
