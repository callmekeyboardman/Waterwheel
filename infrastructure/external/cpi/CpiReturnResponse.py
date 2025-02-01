from domain.valobj.cpi.CpiReturnData import CpiReturnData


class CpiReturnResponse:
    # 200 表示成功
    returncode: int
    returndata: CpiReturnData

    def __init__(self, obj: dict):
        self._returncode = obj['returncode']
        self._returndata = CpiReturnData(obj['returndata'])

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
    def returndata(self, returndata: CpiReturnData):
        self._returndata = returndata

    # 是否成功
    def is_ok(self):
        return self._returncode == 200

    # 返回cpi数据 map
    # key: zb
    # value: list[data]
    def cpi_data_map(self):
        return_data = self._returndata
        value_map = dict()
        for data_node in return_data.datanodes:
            if data_node.is_cpi1() or data_node.is_cpi2():
                zb_code = data_node.get_zb_code()
                if zb_code not in value_map:
                    value_map[zb_code] = []
                data = {
                    'zb': zb_code,
                    'sj': data_node.get_sj_code(),
                    'value': data_node.get_data()
                }
                value_map[zb_code].append(data)
        # 同一个指标下的数据,按照时间排序
        for key in value_map.keys():
            value_list = value_map[key]
            sorted_list = sorted(value_list, key=lambda x: x['sj'])
            value_map[key] = sorted_list
        return value_map

    # 返回cpi数据的 指标名称列表
    # @param cpi_data_map() 方法返回的结果
    def cpi_zb_names(self, cpi_data_map: dict):
        return_data = self._returndata

        zb_codes = cpi_data_map.keys()

        zb_names = []
        for zb_code in zb_codes:
            for wd_node in return_data.wdnodes:
                node_map = wd_node.node_map()
                if zb_code in node_map:
                    zb_names.append(node_map[zb_code])
                    break
        return zb_names

    # 返回cpi数据的 时间列表
    # @param cpi_data_map() 方法返回的结果
    def cpi_sj_names(self, cpi_data_map: dict):
        return_data = self._returndata
        # 取出其中一个数据的 sj 列表即可
        sj_codes = []
        for key in cpi_data_map.keys():
            value_list = cpi_data_map[key]
            for data in value_list:
                sj_codes.append(data['sj'])
            break
        sj_names = []
        for sj_code in sj_codes:
            for wd_node in return_data.wdnodes:
                node_map = wd_node.node_map()
                if sj_code in node_map:
                    sj_names.append(node_map[sj_code])
                    break
        return sj_names
