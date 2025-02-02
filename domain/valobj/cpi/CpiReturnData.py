from typing import List

from domain.valobj.cpi.CpiReturnDataNode import CpiReturnDataNode
from domain.valobj.cpi.CpiReturnWdNode import CpiReturnWdNode


class CpiReturnData:
    # 总数
    _hasdatacount: int
    # 数据集，按照月份，从当前月向前排序
    _datanodes: List[CpiReturnDataNode]
    # 指标集
    _wdnodes: List[CpiReturnWdNode]

    _cpi_data_map: dict
    _zb_names: []
    _sj_codes: []
    _values: []

    def __init__(self, obj: dict):
        self._hasdatacount = obj['hasdatacount']

        datanodes = []
        for datanode in obj['datanodes']:
            datanodes.append(CpiReturnDataNode(datanode))
        self._datanodes = datanodes

        wdnodes = []
        for wdnode in obj['wdnodes']:
            wdnodes.append(CpiReturnWdNode(wdnode))
        self._wdnodes = wdnodes

        self._init_data()

    def _init_data(self):
        self._init_cpi_data_map()
        self._init_zb_names()
        self._init_sj_names()
        self._init_values()

    # 返回cpi数据 map
    # key: zb
    # value: list[data]
    def _init_cpi_data_map(self):
        self._cpi_data_map = dict()

        for data_node in self._datanodes:
            if data_node.is_cpi1() or data_node.is_cpi2():
                zb_code = data_node.get_zb_code()
                if zb_code not in self._cpi_data_map:
                    self._cpi_data_map[zb_code] = []
                data = {
                    'zb': zb_code,
                    'sj': data_node.get_sj_code(),
                    'value': data_node.get_data()
                }
                self._cpi_data_map[zb_code].append(data)
        # 同一个指标下的数据,按照时间排序
        for key in self._cpi_data_map.keys():
            value_list = self._cpi_data_map[key]
            sorted_list = sorted(value_list, key=lambda x: x['sj'])
            self._cpi_data_map[key] = sorted_list

    # 返回cpi数据的 指标名称列表
    def _init_zb_names(self):
        zb_codes = self._cpi_data_map.keys()

        self._zb_names = []
        for zb_code in zb_codes:
            for wd_node in self._wdnodes:
                node_map = wd_node.node_map()
                if zb_code in node_map:
                    self._zb_names.append(node_map[zb_code])
                    break

    # 返回cpi数据的 时间列表
    def _init_sj_names(self):
        # 取出其中一个数据的 sj 列表即可
        self._sj_codes = []
        for key in self._cpi_data_map.keys():
            value_list = self._cpi_data_map[key]
            for data in value_list:
                self._sj_codes.append(data['sj'])
            break
        self._sj_codes = sorted(self._sj_codes)

    def _init_values(self):
        self._values = []
        for value in self._cpi_data_map.values():
            sub_value = []
            for data in value:
                sub_value.append(data['value'])
            self._values.append(sub_value)

    def get_zb_names(self):
        return self._zb_names

    def get_sj_codes(self):
        return self._sj_codes

    def get_values(self):
        return self._values
