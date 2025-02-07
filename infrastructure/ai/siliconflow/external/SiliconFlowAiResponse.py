from domain.ai.siliconflow.valobj.SiliconFlowMessage import SiliconFlowMessage


class SiliconFlowChoice:
    _finish_reason: str
    _message: SiliconFlowMessage

    def __init__(self, obj: dict):
        self._finish_reason = obj["finish_reason"]

        message = obj["message"]
        self._message = SiliconFlowMessage(message["role"], message["content"])

    def get_message(self) -> SiliconFlowMessage:
        return self._message


class SiliconFlowAiResponse:
    _id: str
    _created: int
    _choices: [SiliconFlowChoice]

    def __init__(self, obj: dict):
        self._id = obj['id']
        self._created = obj['created']

        self._choices = []
        for choice in obj['choices']:
            self._choices.append(SiliconFlowChoice(choice))

    def get_message(self) -> SiliconFlowMessage | None:
        if len(self._choices) == 0:
            return None
        return self._choices[0].get_message()
