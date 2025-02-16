from domain.ns.repository.INsRepository import INsRepository
from domain.ns.valobj.NsReturnData import NsReturnData
from infrastructure.data import data_info
from infrastructure.ns.repository.cpi import CpiDataConverter
from infrastructure.utils import excel_util


class CpiExcelRepository(INsRepository):

    def save(self, return_data: NsReturnData):
        result = CpiDataConverter.convert(return_data)
        # 保存数据
        excel_util.export(data_info.path(), "CPI统计数据(2021~至今)",
                          result['row_names'], result['col_names'], result['values'])