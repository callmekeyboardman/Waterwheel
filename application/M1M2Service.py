import logging

from infrastructure.ns.external.M1M2Client import M1M2Client
from infrastructure.ns.repository.m1m2.M1M2ChartRepository import M1M2ChartRepository
from infrastructure.ns.repository.m1m2.M1M2ExcelRepository import M1M2ExcelRepository

# M1\M2 统计数据
if __name__ == "__main__":
    cpiClient = M1M2Client()
    excelRepository = M1M2ExcelRepository()
    chartRepository = M1M2ChartRepository()
    try:
        # 查询数据
        return_data = cpiClient.read_data()
        # 输出为 excel
        excelRepository.save(return_data)
        # 绘制图像并输出
        chartRepository.save(return_data)
    except Exception as ex:
        logging.exception(ex)
