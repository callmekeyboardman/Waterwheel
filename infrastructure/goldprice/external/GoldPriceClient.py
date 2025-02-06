from datetime import datetime

import requests

from domain.goldprice.external.IGoldPriceClient import IGoldPriceClient
from infrastructure.goldprice.external.GoldPriceReturnResponse import GoldPriceReturnResponse
from infrastructure.utils import json_util


class GoldPriceClient(IGoldPriceClient):
    # 价格表，单位 美元/盎司
    PATH = "https://fsapi.gold.org/api/goldprice/v11/chart/price/usd/oz/%s,%s"

    def read_data(self):
        result = requests.get(self.url())
        response = GoldPriceReturnResponse(json_util.read(result.text))
        return response.get_chart_data()

    def url(self):
        # 要查询的时间
        today = datetime.now().date()
        day1 = datetime(today.year, today.month, today.day)
        day2 = datetime(today.year - 5, today.month, today.day)

        url = self.PATH % (int(day2.timestamp() * 1000), int(day1.timestamp() * 1000))
        return url
