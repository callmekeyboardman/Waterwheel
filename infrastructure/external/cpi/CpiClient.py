import datetime
import logging
import time
from datetime import datetime

import requests

from domain.external.ICpiClient import ICpiClient
from infrastructure.external.cpi.CpiReturnResponse import CpiReturnResponse
from infrastructure.utils import json_util


class CpiClient(ICpiClient):
    PATH = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=[]&dfwds=%s&k1=%s"

    def read_cpi_data(self):
        result = requests.get(self.url())
        response = CpiReturnResponse(json_util.read(result.text))

        if not response.is_ok():
            logging.error("[CpiClient] 查询数据异常 " + response.returncode)
            raise Exception("[CpiClient] 查询数据异常")
        return response

    def url(self):
        value_codes = []
        cur_year = datetime.now().year

        i = 2021
        while i <= cur_year:
            value_codes.append(str(i))
            i = i + 1

        # 要查询的时间和指标
        dfwd1 = {'wdcode': 'zb', 'valuecode': 'A01010G'}
        dfwd2 = {'wdcode': 'sj', 'valuecode': ','.join(value_codes)}
        dfwds = [dfwd1, dfwd2]
        # 当前毫秒时间戳
        k1 = int(time.time() * 1000)
        url = self.PATH % (json_util.write(dfwds), k1)
        return url
