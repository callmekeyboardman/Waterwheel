import requests

from domain.ai.IAiClient import IAiClient
from infrastructure.ai.deepseek.external.DeepSeekAiResponse import DeepSeekAiResponse
from infrastructure.utils import json_util

URL = "https://api.siliconflow.cn/v1/chat/completions"
# 替换成自己的
APP_KEY = 'sk-xxx'

HEADERS = {
    "Authorization": 'Bearer ' + APP_KEY,
    "Content-Type": "application/json"
}

PAY_LOAD = {
    "model": "deepseek-ai/DeepSeek-V3",
    "stream": False,
    "max_tokens": 512,
    "stop": None,
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50,
    "frequency_penalty": 0.5,
    "n": 1,
    "response_format": {"type": "text"},
    "tools": None
}


class SiliconFlowAiClient(IAiClient):
    _messages = []

    def chat(self, prompt: str):
        payload = self.payload(prompt)

        response = requests.request("POST", URL, headers=HEADERS, data=payload)

        res = DeepSeekAiResponse(json_util.read(response.text))

        message = res.get_message()
        if message is None:
            return None
        return message

    def payload(self, prompt: str):
        self._messages = []
        self._messages.append({"role": "user", "content": prompt})
        PAY_LOAD['messages'] = self._messages
        return json_util.write(PAY_LOAD)
