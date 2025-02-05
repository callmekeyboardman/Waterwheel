import logging

from infrastructure.external.goldprice.GoldPriceClient import GoldPriceClient
from infrastructure.repository.goldprice.GoldPriceChartRepository import GoldPriceChartRepository
from infrastructure.repository.goldprice.GoldPriceExcelRepository import GoldPriceExcelRepository

# 近5年的黄金价格
if __name__ == "__main__":
    client = GoldPriceClient()
    excelRepository = GoldPriceExcelRepository()
    chartRepository = GoldPriceChartRepository()
    try:
        # 查询数据
        return_data = client.read_data()
        # 输出为 excel
        # excelRepository.save(return_data)
        # 绘制图像并输出
        chartRepository.save(return_data)
    except Exception as ex:
        logging.exception(ex)
