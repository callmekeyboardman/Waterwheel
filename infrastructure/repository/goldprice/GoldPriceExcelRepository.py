from domain.repository.goldprice.IGoldPriceRepository import IGoldPriceRepository
from domain.valobj.goldprice.GoldPriceChartData import GoldPriceChartData
from infrastructure.repository.data import data_info
from infrastructure.repository.goldprice import GoldPriceDataConverter
from infrastructure.utils import excel_util


class GoldPriceExcelRepository(IGoldPriceRepository):

    def save(self, return_data: GoldPriceChartData):
        result = GoldPriceDataConverter.convert(return_data)
        # 保存数据
        excel_util.export(data_info.path(), "黄金价格(近5年)",
                          result['row_names'], result['col_names'], result['values'])
