import logging

from infrastructure.external.cpi.CpiClient import CpiClient
from infrastructure.repository.cpi.CpiChartRepository import CpiChartRepository
from infrastructure.repository.cpi.CpiExcelRepository import CpiExcelRepository

# main函数
if __name__ == "__main__":
    cpiClient = CpiClient()
    excelRepository = CpiExcelRepository()
    chartRepository = CpiChartRepository()
    try:
        # 查询数据
        return_data = cpiClient.read_cpi_data()
        # 输出为 excel
        excelRepository.save(return_data)
        # 绘制图像并输出
        chartRepository.save(return_data)
    except Exception as ex:
        logging.exception(ex)
