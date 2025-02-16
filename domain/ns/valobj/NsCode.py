# 居民消费价格指数
def is_cpi1(value):
    return value == 'A01010G01' or value == '居民消费价格指数(上年同月=100)'


# 不包括食品和能源居民消费价格指数
def is_cpi2(value):
    return value == 'A01010G0D' or value == '不包括食品和能源居民消费价格指数(上年同月=100)'

# 黄金储备
def is_gold(value):
    return value == 'A0L0401' or value == '黄金储备'

# 货币(M1)供应量_同比增长
def is_m1(value):
    return value == 'A0D0104' or value == '货币(M1)供应量_同比增长'

# (M2)供应量_同比增长
def is_m2(value):
    return value == 'A0D0102' or value == '货币和准货币(M2)供应量_同比增长'
