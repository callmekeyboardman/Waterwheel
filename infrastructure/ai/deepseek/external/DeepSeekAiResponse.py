from domain.ai.deepseek.valobj.DeepSeekMessage import DeepSeekMessage


class DeepSeekChoice:
    _index: int
    _finish_reason: str
    _message: DeepSeekMessage

    def __init__(self, obj: dict):
        self._index = obj["index"]
        self._finish_reason = obj["finish_reason"]

        message = obj["message"]
        self._message = DeepSeekMessage(message["role"], message["content"])

    def get_message(self) -> DeepSeekMessage:
        return self._message


class DeepSeekAiResponse:
    _id: str
    _created: int
    _choices: [DeepSeekChoice]

    def __init__(self, obj: dict):
        self._id = obj['id']
        self._created = obj['created']

        self._choices = []
        for choice in obj['choices']:
            self._choices.append(DeepSeekChoice(choice))

    def get_message(self) -> DeepSeekMessage | None:
        if len(self._choices) == 0:
            return None
        return self._choices[0].get_message()
