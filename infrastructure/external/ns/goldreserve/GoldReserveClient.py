import logging
import time

import requests

from domain.external.ns.INsClient import INsClient
from infrastructure.external.ns.NsReturnResponse import NsReturnResponse
from infrastructure.utils import json_util


class GoldReserveClient(INsClient):
    PATH = ("https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=["
            "]&dfwds=%s&k1=%s&h=1")

    def read_data(self):
        result = requests.get(self.url())
        response = NsReturnResponse(json_util.read(result.text))

        if not response.is_ok():
            logging.error("[GoldReserveClient] 查询数据异常 " + response.returncode)
            raise Exception("[GoldReserveClient] 查询数据异常")
        return response.returndata

    def url(self):
        # 要查询的时间和指标
        dfwd1 = {'wdcode': 'zb', 'valuecode': 'A0L04'}
        dfwd2 = {'wdcode': 'sj', 'valuecode': 'LAST20'}
        dfwds = [dfwd1, dfwd2]
        # 当前毫秒时间戳
        k1 = int(time.time() * 1000)
        url = self.PATH % (json_util.write(dfwds), k1)
        return url
