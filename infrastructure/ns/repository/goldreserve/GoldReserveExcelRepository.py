from domain.ns.repository.INsRepository import INsRepository
from domain.ns.valobj.NsReturnData import NsReturnData
from infrastructure.data import data_info
from infrastructure.ns.repository.goldreserve import GoldReserveDataConverter
from infrastructure.utils import excel_util


class GoldReserveExcelRepository(INsRepository):

    def save(self, return_data: NsReturnData):
        result = GoldReserveDataConverter.convert(return_data)
        # 保存数据
        excel_util.export(data_info.path(), "黄金储备(近20年)",
                          result['row_names'], result['col_names'], result['values'])
