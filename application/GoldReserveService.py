import logging

from infrastructure.ns.external.GoldReserveClient import GoldReserveClient
from infrastructure.ns.repository.goldreserve.GoldReserveChartRepository import GoldReserveChartRepository
from infrastructure.ns.repository.goldreserve.GoldReserveExcelRepository import GoldReserveExcelRepository

# 黄金储备
if __name__ == "__main__":
    client = GoldReserveClient()
    excelRepository = GoldReserveExcelRepository()
    chartRepository = GoldReserveChartRepository()
    try:
        # 查询数据
        return_data = client.read_data()
        # 输出为 excel
        excelRepository.save(return_data)
        # 绘制图像并输出
        chartRepository.save(return_data)
    except Exception as ex:
        logging.exception(ex)
