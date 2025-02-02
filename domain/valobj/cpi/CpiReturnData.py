from typing import List

from domain.valobj.cpi.CpiReturnDataNode import CpiReturnDataNode
from domain.valobj.cpi.CpiReturnWdNode import CpiReturnWdNode


class CpiReturnData:
    # 总数
    hasdatacount: int
    # 数据集，按照月份，从当前月向前排序
    datanodes: List[CpiReturnDataNode]
    # 指标集
    wdnodes: List[CpiReturnWdNode]

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

    @property
    def hasdatacount(self):
        return self._hasdatacount

    @hasdatacount.setter
    def hasdatacount(self, hasdatacount: int):
        self._hasdatacount = hasdatacount

    @property
    def datanodes(self):
        return self._datanodes

    @datanodes.setter
    def datanodes(self, datanodes: List[CpiReturnDataNode]):
        self._datanodes = datanodes

    @property
    def wdnodes(self):
        return self._wdnodes

    @wdnodes.setter
    def wdnodes(self, wdnodes: List[CpiReturnWdNode]):
        self._wdnodes = wdnodes

    # 返回cpi数据 map
    # key: zb
    # value: list[data]
    def cpi_data_map(self):
        value_map = dict()
        for data_node in self.datanodes:
            if data_node.is_cpi1() or data_node.is_cpi2():
                zb_code = data_node.get_zb_code()
                if zb_code not in value_map:
                    value_map[zb_code] = []
                data = {
                    'zb': zb_code,
                    'sj': data_node.get_sj_code(),
                    'value': data_node.get_data()
                }
                value_map[zb_code].append(data)
        # 同一个指标下的数据,按照时间排序
        for key in value_map.keys():
            value_list = value_map[key]
            sorted_list = sorted(value_list, key=lambda x: x['sj'])
            value_map[key] = sorted_list
        return value_map

    # 返回cpi数据的 指标名称列表
    # @param cpi_data_map() 方法返回的结果
    def cpi_zb_names(self, cpi_data_map: dict):
        zb_codes = cpi_data_map.keys()

        zb_names = []
        for zb_code in zb_codes:
            for wd_node in self.wdnodes:
                node_map = wd_node.node_map()
                if zb_code in node_map:
                    zb_names.append(node_map[zb_code])
                    break
        return zb_names

    # 返回cpi数据的 时间列表
    # @param cpi_data_map() 方法返回的结果
    def cpi_sj_names(self, cpi_data_map: dict):
        # 取出其中一个数据的 sj 列表即可
        sj_codes = []
        for key in cpi_data_map.keys():
            value_list = cpi_data_map[key]
            for data in value_list:
                sj_codes.append(data['sj'])
            break
        sj_names = []
        for sj_code in sj_codes:
            for wd_node in self.wdnodes:
                node_map = wd_node.node_map()
                if sj_code in node_map:
                    sj_names.append(node_map[sj_code])
                    break
        return sj_names
