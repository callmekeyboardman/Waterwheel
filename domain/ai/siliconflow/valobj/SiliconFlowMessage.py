class SiliconFlowMessage:
    _role: str
    _content: str

    def __init__(self, role, content):
        self._role = role
        self._content = content

    def get_content(self):
        return self._content