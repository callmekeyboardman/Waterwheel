import requests

from domain.external.ai.IAiClient import IAiClient
from infrastructure.external.ai.deepseek.DeepSeekAiResponse import DeepSeekAiResponse
from infrastructure.utils import json_util

URL = "https://api.deepseek.com/chat/completions"
# 替换成自己的
APP_KEY = 'sk-xxx'

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + APP_KEY
}

PAY_LOAD = {
    "model": "deepseek-chat",
    "frequency_penalty": 0,
    "max_tokens": 4096,
    "presence_penalty": 0,
    "response_format": {
        "type": "text"
    },
    "stop": None,
    "stream": False,
    "stream_options": None,
    "temperature": 1,
    "top_p": 1,
    "tools": None,
    "tool_choice": "none",
    "logprobs": False,
    "top_logprobs": None
}


class DeepSeekAiClient(IAiClient):
    _messages = []

    def chat(self, prompt: str):
        payload = self.payload(prompt)

        response = requests.request("POST", URL, headers=HEADERS, data=payload)

        res = DeepSeekAiResponse(json_util.read(response.text))

        message = res.get_message()
        if message is None:
            return None
        self._messages.append({"role": "user", "content": message.get_content()})
        return message

    def payload(self, prompt: str):
        self._messages.append({"role": "user", "content": prompt})
        PAY_LOAD['messages'] = self._messages
        return json_util.write(PAY_LOAD)
