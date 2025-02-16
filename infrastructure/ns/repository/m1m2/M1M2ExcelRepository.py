from domain.ns.repository.INsRepository import INsRepository
from domain.ns.valobj.NsReturnData import NsReturnData
from infrastructure.data import data_info
from infrastructure.ns.repository.cpi import CpiDataConverter
from infrastructure.ns.repository.m1m2 import M1M2DataConverter
from infrastructure.utils import excel_util


class M1M2ExcelRepository(INsRepository):

    def save(self, return_data: NsReturnData):
        result = M1M2DataConverter.convert(return_data)
        # 保存数据
        excel_util.export(data_info.path(), "M1M2月度同比增速(%)",
                          result['row_names'], result['col_names'], result['values'])