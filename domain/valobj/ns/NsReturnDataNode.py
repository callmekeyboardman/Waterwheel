class NsReturnDataNode:
    # code，由 wds 中的指标 code 和 时间 code 拼接而成，比如 zb.A01010G01_sj.202412
    code: str
    # 数据
    data: {}
    # wds 包含两个字段：valuecode 是 node 的 code，wdcode 是 node code 的中文含义，比如 zb 指标\sj 时间
    wds: []

    def __init__(self, obj: dict):
        self._code = obj['code']
        self._data = obj['data']
        self._wds = obj['wds']

    # 返回具体的数值，小数
    def get_data(self):
        return float(self._data['data'])

    # node 的 code
    def get_zb_code(self):
        wd = self._wds[0]
        return wd['valuecode']

    # 所属的时间 code，比如 '202412'
    def get_sj_code(self):
        wd = self._wds[1]
        return wd['valuecode']
