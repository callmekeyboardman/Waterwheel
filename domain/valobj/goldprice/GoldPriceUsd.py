from datetime import datetime


class GoldPriceUsd:
    time_stamp: int
    value: float

    def __init__(self, obj: []):
        self.time_stamp = obj[0]
        self.value = obj[1]

    def get_time_name(self):
        date_time = datetime.fromtimestamp(self.time_stamp / 1000)
        return date_time.strftime("%Y年%m月%d日")

    def get_time_stamp(self) -> int:
        return self.time_stamp
