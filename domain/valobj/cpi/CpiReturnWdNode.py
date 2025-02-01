class CpiReturnWdNode:
    # 数据
    nodes: []
    # node 的 code,对应 CpiReturnDataNode.wds.valuecode,比如 zb\sj
    wdcode: str
    # node 含义名称,比如 指标\时间
    wdname: str

    def __init__(self, obj: dict):
        self._nodes = obj['nodes']
        self._wdcode = obj['wdcode']
        self._wdname = obj['wdname']

    # 返回 nodes 中的 code - name 键值对
    def node_map(self):
        node_map = dict()
        for node in self._nodes:
            node_map[node['code']] = node['name'].split('(')[0]
        return node_map
