from typing import List

from domain.valobj.goldprice.GoldPriceUsd import GoldPriceUsd


class GoldPriceChartData:
    USD: List[GoldPriceUsd]

    def __init__(self, obj: dict):
        self._USD = []
        for data in obj['USD']:
            self._USD.append(GoldPriceUsd(data))

    def get_usd(self) -> List[GoldPriceUsd]:
        return self._USD
