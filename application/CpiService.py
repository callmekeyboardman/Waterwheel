import logging

from infrastructure.ns.external.CpiClient import CpiClient
from infrastructure.ns.repository.cpi.CpiChartRepository import CpiChartRepository
from infrastructure.ns.repository.cpi.CpiExcelRepository import CpiExcelRepository

# CPI 统计数据
if __name__ == "__main__":
    cpiClient = CpiClient()
    excelRepository = CpiExcelRepository()
    chartRepository = CpiChartRepository()
    try:
        # 查询数据
        return_data = cpiClient.read_data()
        # 输出为 excel
        excelRepository.save(return_data)
        # 绘制图像并输出
        chartRepository.save(return_data)
    except Exception as ex:
        logging.exception(ex)
