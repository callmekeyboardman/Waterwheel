import logging

from infrastructure.external.ns.cpi.CpiClient import CpiClient
from infrastructure.repository.ns.cpi.CpiChartRepository import CpiChartRepository
from infrastructure.repository.ns.cpi.CpiExcelRepository import CpiExcelRepository

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
