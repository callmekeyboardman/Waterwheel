from decimal import Decimal

import matplotlib

from domain.repository.cpi.ICpiRepository import ICpiRepository
from domain.valobj.cpi.CpiReturnData import CpiReturnData
from infrastructure.utils import plot_util

matplotlib.use('TkAgg')


class CpiChartRepository(ICpiRepository):

    def save(self, return_data: CpiReturnData):
        values = return_data.get_values()
        zb_names = return_data.get_zb_names()
        x_points = return_data.get_sj_codes()

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
