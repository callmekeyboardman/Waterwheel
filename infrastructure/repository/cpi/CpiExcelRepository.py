from domain.repository.cpi.ICpiRepository import ICpiRepository
from domain.valobj.cpi.CpiReturnData import CpiReturnData
from infrastructure.repository.data import data_info
from infrastructure.utils import excel_util


class CpiExcelRepository(ICpiRepository):

    # @param CpiReturnResponse 类型
    def save(self, return_data: CpiReturnData):
        # 行名称 指标名称
        row_names = return_data.get_zb_names()
        # 列名称 时间
        col_names = return_data.get_sj_codes()
        # 数据列表
        values = return_data.get_values()
        # 保存数据
        excel_util.export(data_info.path(), "CPI统计数据(2021~至今)", row_names, col_names, values)
