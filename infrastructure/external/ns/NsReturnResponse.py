from domain.valobj.ns.NsReturnData import NsReturnData


class NsReturnResponse:
    # 200 表示成功
    returncode: int
    returndata: NsReturnData

    def __init__(self, obj: dict):
        self._returncode = obj['returncode']
        self._returndata = NsReturnData(obj['returndata'])

    @property
    def returncode(self):
        return self._returncode

    @returncode.setter
    def returncode(self, returncode: int):
        self._returncode = returncode

    @property
    def returndata(self):
        return self._returndata

    @returndata.setter
    def returndata(self, returndata: NsReturnData):
        self._returndata = returndata

    # 是否成功
    def is_ok(self):
        return self._returncode == 200
