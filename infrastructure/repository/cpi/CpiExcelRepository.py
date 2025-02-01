from domain.repository.cpi.ICpiRepository import ICpiRepository
from infrastructure.external.cpi.CpiReturnResponse import CpiReturnResponse
from infrastructure.repository.data import data_info
from infrastructure.utils import excel_util


class CpiExcelRepository(ICpiRepository):

    # @param CpiReturnResponse 类型
    def save(self, response: CpiReturnResponse):
        # 数据 map
        cpi_data_map = response.cpi_data_map()
        # 行名称 指标名称
        row_names = response.cpi_zb_names(cpi_data_map)
        # 列名称 时间
        col_names = response.cpi_sj_names(cpi_data_map)

        values = []
        for value in cpi_data_map.values():
            sub_value = []
            for data in value:
                sub_value.append(data['value'])
            values.append(sub_value)
        # 保存数据
        excel_util.export(data_info.path(), "CPI统计数据(2021~至今)", row_names, col_names, values)
