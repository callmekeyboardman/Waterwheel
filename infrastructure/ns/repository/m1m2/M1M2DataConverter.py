from domain.ns.valobj import NsCode
from domain.ns.valobj.NsReturnData import NsReturnData


def convert(return_data: NsReturnData):
    # 行数据 指标名称
    zb_names = return_data.get_zb_names()
    # 列数据 时间
    sj_codes = return_data.get_sj_codes()
    # 数据列表
    values = return_data.get_values()

    row_names = []
    value_list = []

    for i in range(len(zb_names)):
        row_name = zb_names[i]
        if NsCode.is_m1(row_name):
            row_names.append("M1增速(%)")
            value_list.append(__round(values[i]))
        elif NsCode.is_m2(row_name):
            row_names.append("M2增速(%)")
            value_list.append(__round(values[i]))

    result = {
        'row_names': row_names,
        'col_names': sj_codes,
        'values': value_list
    }
    return result


def __round(values: []):
    tmp = []
    # 对数据做四舍五入
    for value in values:
        tmp.append(round(value, 1))
    return tmp
