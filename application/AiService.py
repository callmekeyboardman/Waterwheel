import textwrap

# from infrastructure.ai.deepseek.external.DeepSeekAiClient import DeepSeekAiClient
from infrastructure.ai.siliconflow.external.SiliconFlowAiClient import SiliconFlowAiClient

# client = DeepSeekAiClient()
client = SiliconFlowAiClient()


def print_text(text):
    print(text)
    print("------------------------------------")


def print_message():
    content = message.get_content()
    wrapped_text = textwrap.fill(content, width=50)
    print_text(wrapped_text)


if __name__ == "__main__":
    print_text("给小A发消息,按回车结束,输入 end 结束对话.")
    while True:
        input_text = input('input:')
        if input_text.strip() == "end":
            print_text("结束对话")
            break
        message = client.chat(input_text)
        if message is None:
            print_text('服务器繁忙,结束对话,请稍后再试')
            break
        print_message()
