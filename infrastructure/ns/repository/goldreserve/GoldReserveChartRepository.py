from decimal import Decimal

import matplotlib

from domain.ns.repository.INsRepository import INsRepository
from domain.ns.valobj.NsReturnData import NsReturnData
from infrastructure.ns.repository.goldreserve import GoldReserveDataConverter
from infrastructure.utils import plot_util

matplotlib.use('TkAgg')


class GoldReserveChartRepository(INsRepository):

    def save(self, return_data: NsReturnData):
        result = GoldReserveDataConverter.convert(return_data)

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
                if e == 0:
                    e = value[i - 1]
                tmp_y_points.append(Decimal(e * 100) / divide)
            y_points.append(tmp_y_points)

        plot_util.draw_plot(x_points, y_points, zb_names,
                            '黄金储备(近20年)', '时间(年)', '储备量(万盎司)')
