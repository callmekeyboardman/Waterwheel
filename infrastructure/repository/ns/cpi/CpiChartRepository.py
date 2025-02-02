from decimal import Decimal

import matplotlib

from domain.repository.ns.INsRepository import INsRepository
from domain.valobj.ns.NsReturnData import NsReturnData
from infrastructure.repository.ns.cpi import CpiDataConverter
from infrastructure.utils import plot_util

matplotlib.use('TkAgg')


class CpiChartRepository(INsRepository):

    def save(self, return_data: NsReturnData):
        result = CpiDataConverter.convert(return_data)

        values = result['values']
        zb_names = result['row_names']
        x_points = result['col_names']

        sub = Decimal(10000)
        divide = Decimal(100)

        y_points = []

        y_points1 = []
        for e in values[0]:
            y_points1.append((Decimal(e * 100) - sub) / divide)
        y_points.append(y_points1)

        y_points2 = []
        for e in values[1]:
            y_points2.append((Decimal(e * 100) - sub) / divide)
        y_points.append(y_points2)

        plot_util.draw_plot(x_points, y_points, zb_names,
                            'CPI 趋势图(2021~至今)', '时间(年月)', '同比(%)')
