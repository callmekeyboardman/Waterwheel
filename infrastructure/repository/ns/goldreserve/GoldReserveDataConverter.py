from domain.valobj.ns import NsCode
from domain.valobj.ns.NsReturnData import NsReturnData


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
        if NsCode.is_gold(row_name):
            row_names.append(row_name + '(万盎司)')
            value_list.append(values[i])
    result = {
        'row_names': row_names,
        'col_names': sj_codes,
        'values': value_list
    }
    return result
