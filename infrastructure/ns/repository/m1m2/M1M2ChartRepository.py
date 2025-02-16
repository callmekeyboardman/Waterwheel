import matplotlib

from domain.ns.repository.INsRepository import INsRepository
from domain.ns.valobj.NsReturnData import NsReturnData
from infrastructure.ns.repository.m1m2 import M1M2DataConverter
from infrastructure.utils import plot_util

matplotlib.use('TkAgg')


class M1M2ChartRepository(INsRepository):

    def save(self, return_data: NsReturnData):
        result = M1M2DataConverter.convert(return_data)

        values = result['values']
        zb_names = result['row_names']
        x_points = result['col_names']

        y_points = [values[0], values[1]]

        plot_util.draw_plot(x_points, y_points, zb_names,
                            'M1M2月度同比增速(%)', '时间(年月)', '同比(%)')
