import logging
import time

import requests

from domain.ns.external.INsClient import INsClient
from infrastructure.ns.NsReturnResponse import NsReturnResponse
from infrastructure.utils import json_util


class M1M2Client(INsClient):
    PATH = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=[]&dfwds=%s&k1=%s"

    def read_data(self):
        result = requests.get(self.url())
        response = NsReturnResponse(json_util.read(result.text))

        if not response.is_ok():
            logging.error("[M1M2Client] 查询数据异常 " + response.returncode)
            raise Exception("[M1M2Client] 查询数据异常")
        return response.returndata

    def url(self):
        # 要查询的时间和指标
        dfwd1 = {'wdcode': 'zb', 'valuecode': 'A0D01'}
        dfwds = [dfwd1]
        # 当前毫秒时间戳
        k1 = int(time.time() * 1000)
        url = self.PATH % (json_util.write(dfwds), k1)
        return url
