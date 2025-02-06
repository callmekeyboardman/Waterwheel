from domain.goldprice.valobj.GoldPriceChartData import GoldPriceChartData


class GoldPriceReturnResponse:
    chartData: GoldPriceChartData

    def __init__(self, obj: dict):
        self._chartData = GoldPriceChartData(obj['chartData'])

    def get_chart_data(self) -> GoldPriceChartData:
        return self._chartData
