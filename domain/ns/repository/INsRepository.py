# 读取 cpi 数据，读取2021~当前的CPI数据
from abc import abstractmethod, ABC

from domain.ns.valobj import NsReturnData


class INsRepository(ABC):

    # 把数据写入
    @abstractmethod
    def save(self, return_data: NsReturnData):
        pass
