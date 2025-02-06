from decimal import Decimal

import matplotlib

from domain.goldprice.repository.IGoldPriceRepository import IGoldPriceRepository
from domain.goldprice.valobj.GoldPriceChartData import GoldPriceChartData
from infrastructure.goldprice.repository import GoldPriceDataConverter
from infrastructure.utils import plot_util

matplotlib.use('TkAgg')


class GoldPriceChartRepository(IGoldPriceRepository):

    def save(self, return_data: GoldPriceChartData):
        result = GoldPriceDataConverter.convert(return_data)

        values = result['values']
        zb_names = result['row_names']
        x_points = result['col_names']

        divide = Decimal(100)

        y_points = []

        for value in values:
            tmp_y_points = []
            for i in range(len(value)):
                e = value[i]
                # 如果为0，使用前一年的值代替
                tmp_y_points.append(Decimal(e * 100) / divide)
            y_points.append(tmp_y_points)

        plot_util.draw_simple_plot(x_points, y_points, zb_names,
                                   '黄金价格(近5年)', '时间(年-月)', '价格(美元/盎司)')
