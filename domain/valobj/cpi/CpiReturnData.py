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
